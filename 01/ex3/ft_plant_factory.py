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
    print("=== Plant Factory Output ===")

    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]

    for plant in plants:
        print("Created: ", end="")
        plant.show()
