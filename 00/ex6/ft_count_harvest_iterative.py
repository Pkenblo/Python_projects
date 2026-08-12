def ft_count_harvest_iterative() -> None:
    num = int(input("Days until harvest: "))
    for i in range(1, num + 1):
        print(f"Day {i}")
    print("Harvest time!")
