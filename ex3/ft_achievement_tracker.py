import random


def gen_player_achievements(pool: list[str]) -> set[str]:
    return set(random.sample(pool, random.randint(6, 18)))


def print_players(names: list[str], achievements: list[set[str]]) -> None:
    for i in range(len(names)):
        print(f"Player {names[i]}: {achievements[i]}")


def print_distinct(achievements: list[set[str]]) -> None:
    print(f"\nAll distinct achievements: {set().union(*achievements)}")


def print_common(achievements: list[set[str]]) -> None:
    print(
        f"\nCommon achievements:"
        f"{achievements[0].intersection(*achievements[1:])}"
        )


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
    print_common(achievements)


if __name__ == "__main__":
    main()
