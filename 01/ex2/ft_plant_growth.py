class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int
    ) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days

    def show(self) -> None:
        print(
            f"{self.name}: {self.height:.1f}cm, "
            f"{self.age_days} days old"
        )

    def age(self) -> None:
        self.age_days += 1

    def grow(self) -> None:
        self.height += 0.8


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")

    rose = Plant("Rose", 25.0, 30)
    initial_height = rose.height
    rose.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()

    weekly_growth = rose.height - initial_height
    print(f"Growth this week: {weekly_growth:.1f}cm")
