import random


def get_initial_names() -> list[str]:
    return ["Alice", "bob", "Charlie", "dylan", "Emma",
            "Gregory", "john", "kevin", "Liam"]


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    names = get_initial_names()
    print(f"Initial list of players: {names}")

    cap_names = [name.capitalize() for name in names]
    print(f"New list with all names capitalized: {cap_names}")

    only_cap = [name for name in names if name == name.capitalize()]
    print(f"New list of capitalized names only: {only_cap}")

    scores = {name: random.randint(0, 999) for name in cap_names}
    print(f"\nScore dict: {scores}")
    avg = sum(scores.values()) / len(scores)
    print(f"Score average is: {round(avg, 2)}")
    high_scores = {k: scores[k] for k in scores if scores[k] > avg}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
