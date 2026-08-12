class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int
    ) -> None:
        self._name = name
        self._height = 0.0
        self._age_days = 0

        self.set_height(height)
        self.set_age(age_days)

    def show(self) -> None:
        print(
            f"{self._name}: {self._height:.1f}cm, "
            f"{self._age_days} days old"
        )

    def age(self) -> None:
        self._age_days += 1

    def grow(self, amount: float = 0.8) -> None:
        self._height += amount

    def set_height(self, height: float) -> None:
        if height < 0:
            print(
                f"{self._name}: "
                "Error, height can't be negative"
            )
            print("Height update rejected")
            return
        self._height = height

    def set_age(self, age_days: int) -> None:
        if age_days < 0:
            print(
                f"{self._name}: "
                "Error, age can't be negative"
            )
            print("Age update rejected")
            return
        self._age_days = age_days

    def get_age(self) -> int:
        return self._age_days

    def get_height(self) -> float:
        return self._height


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        color: str,
        is_blooming: bool = False
    ) -> None:
        super().__init__(name, height, age_days)
        self._color = color
        self._is_blooming = is_blooming

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")

        if self._is_blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")

    def bloom(self) -> None:
        self._is_blooming = True


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        trunk_diameter: float,
        produces_shade: bool = False
    ) -> None:
        super().__init__(name, height, age_days)
        self._trunk_diameter = trunk_diameter
        self._produces_shade = produces_shade

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        self._produces_shade = True
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height:.1f}cm long and "
            f"{self._trunk_diameter:.1f}cm wide."
        )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        harvest_season: str,
        nutritional_value: float = 0.0
    ) -> None:
        super().__init__(name, height, age_days)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value:g}")

    def age(self) -> None:
        super().age()
        self._nutritional_value += 0.5

    def grow(self, amount: float = 2.1) -> None:
        super().grow(amount)
        self._nutritional_value += 0.5


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()

    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("")

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("")

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()

    print("[make tomato grow and age for 20 days]")

    for _ in range(20):
        tomato.grow()
        tomato.age()

    tomato.show()
