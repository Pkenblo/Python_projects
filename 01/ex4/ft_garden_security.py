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

    def grow(self) -> None:
        self._height += 0.8

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


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)

    print("Plant created: ", end="")
    rose.show()
    print("")

    rose.set_height(25.0)
    print(f"Height updated: {rose.get_height():g}cm")

    rose.set_age(30)
    print(f"Age updated: {rose.get_age()} days")
    print("")
    rose.set_height(-5.0)
    rose.set_age(-10)
    print("")
    print("Current state: ", end="")
    rose.show()
