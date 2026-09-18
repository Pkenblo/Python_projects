from ._creature import Creature


class Charmileon(Creature):
    def __init__(self) -> None:
        super().__init__("Charmileon", "Fire")

    def attack(self) -> str:
        return "Charmileon uses ember!"


class Charizard(Creature):
    def __init__(self) -> None:
        super().__init__("Charizard", "Fire/Flying")

    def attack(self) -> str:
        return "Charizard uses Heat wave!"


class Febas(Creature):
    def __init__(self) -> None:
        super().__init__("Febas", "Water")

    def attack(self) -> str:
        return "Febas uses Water Gun!"


class Milotic(Creature):
    def __init__(self) -> None:
        super().__init__("Milotic", "Water")

    def attack(self) -> str:
        return "Milotic uses Muddy Water!"
