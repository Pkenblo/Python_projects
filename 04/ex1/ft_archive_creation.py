import sys


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <FileName.txt>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")

    try:
        print(f"Accessing file '{sys.argv[1]}'")
        file = open(sys.argv[1], "r")
    except Exception as e:
        print(f"Error opening file {sys.argv[1]}:", e)
        return

    text = file.read()
    print_file(text)
    file.close()
    print(f"File '{sys.argv[1]}' closed.\n")

    print("Transform data:")
    ends_with_newline = text.endswith("\n")
    text = text.replace("\n", "#\n")
    if not ends_with_newline and text:
        text += "#"
    print_file(text)

    second_file = input("Enter new file name (or empty): ")

    if not second_file:
        print("Not saving data.")
        return

    try:
        print(f"Saving data to '{second_file}'")
        file = open(second_file, "w")
        file.write(text)
        file.close()
    except Exception as e:
        print(f"Error opening file {second_file}:", e)
        print("Data not saved.")
        return

    print(f"Data saved in file '{second_file}'.")


def print_file(file: str) -> None:
    print("---")
    print("")
    print(file)
    print("")
    print("---")


if __name__ == "__main__":
    main()
