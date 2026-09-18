from abc import ABC, abstractmethod

from ex0._creature import Creature
from ex1._capabilities import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        raise NotImplementedError

    @abstractmethod
    def act(self, creature: Creature) -> str:
        raise NotImplementedError


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                "Invalid object for this normal strategy"
            )
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )
        transformer = creature
        assert isinstance(transformer, TransformCapability)
        actions = [
            transformer.transform(),
            creature.attack(),
            transformer.revert(),
        ]
        return "\n".join(actions)


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy"
            )
        healer = creature
        assert isinstance(healer, HealCapability)
        actions = [creature.attack(), healer.heal()]
        return "\n".join(actions)
