from ex0._creature import Creature

from ._capabilities import HealCapability, TransformCapability


class Bulbasur(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Bulbasur", "Grass")

    def attack(self) -> str:
        return "Bulbasur uses Vine Whip!"

    def heal(self, target: object | None = None) -> str:
        _ = target
        return "Bulbasur heals itself for a small amount"


class Venusaur(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Venusaur", "Grass/Fairy")

    def attack(self) -> str:
        return "Venusaur uses Petal Dance!"

    def heal(self, target: object | None = None) -> str:
        _ = target
        return "Venusaur heals itself and others for a large amount"


class Eve(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Eve", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return "Eve performs a boosted strike!"
        return "Eve attacks normally."

    def transform(self) -> str:
        self.is_transformed = True
        return "Eve shifts into a sharper form!"

    def revert(self) -> str:
        self.is_transformed = False
        return "Eve returns to normal."


class Dracoleon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Dracoleon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.is_transformed:
            return "Dracoleon unleashes a devastating dragon strike!"
        return "Dracoleon attacks normally."

    def transform(self) -> str:
        self.is_transformed = True
        return "Dracoleon morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.is_transformed = False
        return "Dracoleon stabilizes its form."
