import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    initial_players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]
    print(f"Initial list of players: {initial_players}")

    capitalized_players = [name.capitalize() for name in initial_players]
    print(f"New list with all names capitalized: {capitalized_players}")

    already_capitalized = [name for name in initial_players if name.istitle()]
    print(f"New list of capitalized names only: {already_capitalized}")

    score_dct = {name: random.randint(1, 1000) for name in capitalized_players}
    print(f"Score dict: {score_dct}")

    total_score = sum(score_dct.values())
    avg_score = round(total_score / len(score_dct), 2)
    print(f"Score average is {avg_score}")

    high_scores = {
        name: score for name, score in score_dct.items() if score > avg_score
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
