from abc import ABC, abstractmethod
from typing import Any, Protocol


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data: list[tuple[int, str]] = []
        self.rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.data:
            raise Exception("No data available")

        return self.data.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list):
            return all(
                isinstance(item, (int, float))
                for item in data
            )

        return False

    def ingest(
        self,
        data: int | float | list[int | float]
    ) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self.data.append((self.rank, str(item)))
                self.rank += 1
        else:
            self.data.append((self.rank, str(data)))
            self.rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)

        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")

        if isinstance(data, list):
            for item in data:
                self.data.append((self.rank, item))
                self.rank += 1
        else:
            self.data.append((self.rank, data))
            self.rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return self._valid_log(data)

        if isinstance(data, list):
            return all(
                isinstance(item, dict) and self._valid_log(item)
                for item in data
            )

        return False

    def _valid_log(self, data: dict[Any, Any]) -> bool:
        return (
            all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in data.items()
            )
            and "log_level" in data
            and "log_message" in data
        )

    def ingest(
        self,
        data: dict[str, str] | list[dict[str, str]]
    ) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")

        if isinstance(data, list):
            for item in data:
                self._ingest_log(item)
        else:
            self._ingest_log(data)

    def _ingest_log(self, data: dict[str, str]) -> None:
        message = (
            f"{data['log_level']}: "
            f"{data['log_message']}"
        )
        self.data.append((self.rank, message))
        self.rank += 1


class ExportPlugin(Protocol):
    def process_output(
        self,
        data: list[tuple[int, str]]
    ) -> None:
        ...


class CSVExportPlugin:
    def process_output(
        self,
        data: list[tuple[int, str]]
    ) -> None:
        values: list[str] = []

        for _, value in data:
            escaped = value.replace('"', '""')
            if any(char in escaped for char in [",", '"', "\n"]):
                escaped = f'"{escaped}"'
            values.append(escaped)

        print("CSV Output:")
        print(",".join(values))


class JSONExportPlugin:
    def process_output(
        self,
        data: list[tuple[int, str]]
    ) -> None:
        result = "{"

        for index, (item_number, value) in enumerate(data):
            if index > 0:
                result += ", "

            escaped = value
            escaped = escaped.replace("\\", "\\\\")
            escaped = escaped.replace('"', '\\"')
            escaped = escaped.replace("\n", "\\n")
            escaped = escaped.replace("\r", "\\r")
            escaped = escaped.replace("\t", "\\t")

            result += f'"item_{item_number}": "{escaped}"'

        result += "}"

        print("JSON Output:")
        print(result)


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            processed = False

            for processor in self.processors:
                if processor.validate(element):
                    processor.ingest(element)
                    processed = True
                    break

            if not processed:
                print(
                    "DataStream error - Can't process element "
                    f"in stream: {element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self.processors:
            print("No processor found, no data")
            return

        for processor in self.processors:
            name = processor.__class__.__name__

            if name == "NumericProcessor":
                display_name = "Numeric Processor"
            elif name == "TextProcessor":
                display_name = "Text Processor"
            elif name == "LogProcessor":
                display_name = "Log Processor"
            else:
                display_name = name

            print(
                f"{display_name}: total {processor.rank} items "
                f"processed, remaining {len(processor.data)} "
                "on processor"
            )

    def output_pipeline(
        self,
        nb: int,
        plugin: ExportPlugin
    ) -> None:
        for processor in self.processors:
            output_data: list[tuple[int, str]] = []

            for _ in range(nb):
                if not processor.data:
                    break

                output_data.append(processor.output())

            if output_data:
                plugin.process_output(output_data)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")

    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("Registering Processors")

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    data_stream.register_processor(numeric)
    data_stream.register_processor(text)
    data_stream.register_processor(log)

    stream = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected"
            }
        ],
        42,
        ["Hi", "five"]
    ]

    print(f"Send first batch of data on stream: {stream}")
    data_stream.process_stream(stream)
    data_stream.print_processors_stats()

    print(
        "Send 3 processed data from each processor "
        "to a CSV plugin:"
    )

    csv_plugin = CSVExportPlugin()
    data_stream.output_pipeline(3, csv_plugin)
    data_stream.print_processors_stats()

    stream2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash"
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days"
            }
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello"
    ]

    print(f"Send another batch of data: {stream2}")
    data_stream.process_stream(stream2)
    data_stream.print_processors_stats()

    print(
        "Send 5 processed data from each processor "
        "to a JSON plugin:"
    )

    json_plugin = JSONExportPlugin()
    data_stream.output_pipeline(5, json_plugin)
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
