import sys


if __name__ == "__main__":
    argv = sys.argv
    print("=== Command Quest ===")
    print(f"Program name: {argv[0]}")

    if len(argv) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(argv) - 1}")
        index = 1
        for arg in argv[1:]:
            print(f"Argument {index}: {arg}")
            index += 1

    print(f"Total arguments: {len(argv)}")
