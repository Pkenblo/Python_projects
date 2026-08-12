def secure_archive(
    file_name: str,
    action: str = "read",
    content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(file_name, "r") as file:
                data = file.read()
            return True, data

        if action == "write":
            with open(file_name, "w") as file:
                file.write(content)
            return True, "Content successfully written to file"

        return False, "Invalid action"

    except Exception as e:
        return False, str(e)


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    print("")

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))
    print("")

    print("Using 'secure_archive' to read from a regular file:")
    success, content = secure_archive("ancient_fragment.txt")
    print((success, content))
    print("")

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", "write", content))


if __name__ == "__main__":
    main()
