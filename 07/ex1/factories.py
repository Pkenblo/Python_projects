from ex0.factories import CreatureFactory

from ._creatures import Bulbasur, Dracoleon, Eve, Venusaur


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Bulbasur:
        return Bulbasur()

    def create_evolved(self) -> Venusaur:
        return Venusaur()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Eve:
        return Eve()

    def create_evolved(self) -> Dracoleon:
        return Dracoleon()
