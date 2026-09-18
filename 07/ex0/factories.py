from abc import ABC, abstractmethod

from ._creature import Creature
from ._creatures import Charmileon, Charizard, Febas, Milotic


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Charmileon:
        return Charmileon()

    def create_evolved(self) -> Charizard:
        return Charizard()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Febas:
        return Febas()

    def create_evolved(self) -> Milotic:
        return Milotic()
