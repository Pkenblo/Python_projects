class Plant:
    class _Statistics:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def add_grow(self) -> None:
            self._grow_calls += 1

        def add_age(self) -> None:
            self._age_calls += 1

        def add_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

    def __init__(
        self,
        name: str,
        height: float,
        age_days: int
    ) -> None:
        self._name = name
        self._height = 0.0
        self._age_days = 0
        self._stats = self._Statistics()

        self.set_height(height)
        self.set_age(age_days)

    def show(self) -> None:
        self._stats.add_show()
        print(
            f"{self._name}: {self._height:.1f}cm, "
            f"{self._age_days} days old"
        )

    def age(self, days: int = 1) -> None:
        self._age_days += days
        self._stats.add_age()

    def grow(self, amount: float = 0.8) -> None:
        self._height += amount
        self._stats.add_grow()

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

    def get_name(self) -> str:
        return self._name

    def display_stats(self) -> None:
        self._stats.display()

    @staticmethod
    def older_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


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
    class _TreeStatistics(Plant._Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def add_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_calls} shade")

    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        trunk_diameter: float,
        produces_shade: bool = False
    ) -> None:
        super().__init__(name, height, age_days)
        self._tree_stats = self._TreeStatistics()
        self._stats = self._tree_stats
        self._trunk_diameter = trunk_diameter
        self._produces_shade = produces_shade

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        self._produces_shade = True
        self._tree_stats.add_shade()
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

    def age(self, days: int = 1) -> None:
        super().age(days)
        self._nutritional_value += 0.5 * days

    def grow(self, amount: float = 2.1) -> None:
        super().grow(amount)
        self._nutritional_value += 0.5


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        color: str,
        seed_count: int = 0
    ) -> None:
        super().__init__(name, height, age_days, color)
        self._seed_count = seed_count

    def bloom(self) -> None:
        super().bloom()
        self._seed_count = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seed_count}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.display_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(
        "Is 30 days more than a year? -> "
        f"{Plant.older_year(30)}"
    )
    print(
        "Is 400 days more than a year? -> "
        f"{Plant.older_year(400)}"
    )

    print("")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_statistics(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("")
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print("")
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)

    print("")
    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_statistics(anonymous)
