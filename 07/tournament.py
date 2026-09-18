from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)

Opponent = tuple[CreatureFactory, BattleStrategy]


def battle(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for first_index in range(len(opponents)):
        for second_index in range(first_index + 1, len(opponents)):
            first_factory, first_strategy = opponents[first_index]
            second_factory, second_strategy = opponents[second_index]
            first = first_factory.create_base()
            second = second_factory.create_base()

            print("* Battle *")
            print(first.describe())
            print("vs.")
            print(second.describe())
            print("now fight!")

            try:
                print(first_strategy.act(first))
                print(second_strategy.act(second))
            except InvalidStrategyError as error:
                print(f"Battle error, aborting tournament: {error}")
                return


def main() -> None:
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Charmileon+Normal), (Healing+Defensive) ]")
    battle(
        [
            (FlameFactory(), normal),
            (HealingCreatureFactory(), defensive),
        ]
    )

    print("Tournament 1 (error)")
    print("[ (Charmileon+Aggressive), (Healing+Defensive) ]")
    battle(
        [
            (FlameFactory(), aggressive),
            (HealingCreatureFactory(), defensive),
        ]
    )

    print("Tournament 2 (multiple)")
    print("[ (Febas+Normal), (Healing+Defensive), "
          "(Transform+Aggressive) ]")
    battle(
        [
            (AquaFactory(), normal),
            (HealingCreatureFactory(), defensive),
            (TransformCreatureFactory(), aggressive),
        ]
    )


if __name__ == "__main__":
    main()
