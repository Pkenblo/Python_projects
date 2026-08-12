import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <FileName.txt>")
        return
    print("=== Cyber Archives Recovery ===")
    try:
        print(f"Accessing file '{sys.argv[1]}'")
        file = open(sys.argv[1], "r")
    except Exception as e:
        print(f"Error opening file {sys.argv[1]}:", e)
        return
    print_file(file)
    print(f"File '{sys.argv[1]}' closed.")
    file.close()


def print_file(file: typing.IO) -> None:
    print("---")
    print("")
    print(file.read())
    print("")
    print("---")


if __name__ == "__main__":
    main()
