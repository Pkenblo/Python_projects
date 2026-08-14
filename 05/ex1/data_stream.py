from abc import ABC, abstractmethod
from typing import Any


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
                message = (
                    f"{item['log_level']}: "
                    f"{item['log_message']}"
                )
                self.data.append((self.rank, message))
                self.rank += 1
        else:
            message = (
                f"{data['log_level']}: "
                f"{data['log_message']}"
            )
            self.data.append((self.rank, message))
            self.rank += 1


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


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")

    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("Registering Numeric Processor")
    numeric = NumericProcessor()
    data_stream.register_processor(numeric)

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

    print("Registering other data processors")
    text = TextProcessor()
    log = LogProcessor()
    data_stream.register_processor(text)
    data_stream.register_processor(log)

    print("Send the same batch again")
    data_stream.process_stream(stream)
    data_stream.print_processors_stats()

    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )

    for _ in range(3):
        numeric.output()

    for _ in range(2):
        text.output()

    log.output()

    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
