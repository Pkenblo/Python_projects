import random

ach = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
]


def gen_player_achievements() -> set[str]:
    n_ach = random.randint(0, 7)
    return set(random.sample(ach, n_ach))


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")

    all_distinct = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {all_distinct}\n")

    common = alice.intersection(bob, charlie, dylan)
    print(f"Common achievements: {common}\n")

    print(f"Only Alice has: {alice.difference(bob.union(charlie, dylan))}")
    print(f"Only Bob has: {bob.difference(alice.union(charlie, dylan))}")
    print(f"Only Charlie has: {charlie.difference(alice.union(bob, dylan))}")
    print(f"Only Dylan has: {dylan.difference(alice.union(bob, charlie))}\n")

    master_set = set(ach)
    print(f"Alice is missing: {master_set.difference(alice)}")
    print(f"Bob is missing: {master_set.difference(bob)}")
    print(f"Charlie is missing: {master_set.difference(charlie)}")
    print(f"Dylan is missing: {master_set.difference(dylan)}")


if __name__ == "__main__":
    main()
