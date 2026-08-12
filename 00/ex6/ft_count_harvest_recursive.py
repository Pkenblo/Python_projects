def ft_count_harvest_recursive() -> None:
    def print_days(days: int) -> None:
        if days != 1:
            print_days(days - 1)
        print(f"Day {days}")

    days = int(input("Days until harvest: "))
    print_days(days)
    print("Harvest time!")
