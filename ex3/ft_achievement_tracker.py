import random


def gen_player_achievements(pool: list[str]) -> set[str]:
    return set(random.sample(pool, random.randint(4, 16)))


def print_players(names: list[str], achievements: list[set[str]]) -> None:
    i = 0
    while i < len(names):
        print(f"Player {names[i]}: {achievements[i]}")
        i += 1


def print_distinct(achievements: list[set[str]]) -> None:
    print(f"\nAll distinct achievements: {set().union(*achievements)}")


def print_common(achievements: list[set[str]]) -> None:
    print(
        f"\nCommon achievements:"
        f"{achievements[0].intersection(*achievements[1:])}\n"
        )


def print_unique(names: list[str], achievements: list[set[str]]) -> None:
    i = 0
    while i < len(names):
        others = set().union(*achievements[:i], *achievements[i+1:])
        print(f"Only {names[i]} has: {achievements[i].difference(others)}")
        i += 1


def print_missing(
        names: list[str],
        achievements: list[set[str]],
        all_achievements: list[str]
        ) -> None:
    i = 0
    print()
    while i < len(names):
        print(
            f"{names[i]} is missing: "
            f"{set(all_achievements) - achievements[i]}"
            )
        i += 1


def main() -> None:
    all_achievements: list[str] = [
        "First Steps", "Speed Runner", "Survivor", "Master Explorer",
        "Treasure Hunter", "Boss Slayer", "Crafting Genius", "World Savior",
        "Unstoppable", "Untouchable", "Sharp Mind", "Strategist",
        "Collector Supreme", "Hidden Path Finder", "True Warrior",
        "Dragon Slayer", "Night Owl", "Lone Wolf", "Team Player",
        "Comeback Kid"
    ]
    names: list[str] = ["Alice", "Bob", "Charlie", "Dylan"]
    achievements: list[set[str]] = []
    for _ in names:
        achievements.append(gen_player_achievements(all_achievements))
    print_players(names, achievements)
    print_distinct(achievements)
    try:
        print_common(achievements)
    except IndexError as e:
        print(f"IndexError occurred: {e}")
    print_unique(names, achievements)
    print_missing(names, achievements, all_achievements)


if __name__ == "__main__":
    main()
