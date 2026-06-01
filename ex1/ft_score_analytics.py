import sys


def argv_parser(argv: list[str]) -> list[int]:
    argv = argv[1:]
    argv_int: list[int] = []
    for i in argv:
        try:
            argv_int.append(int(i))
        except ValueError:
            print(f"Invalid parameter: '{i}'")
    return argv_int


def score_parser(argv: list[int]) -> None:
    max_score = max(argv)
    print(f"\nTotal players:\t{len(argv)}")
    print(f"Total score:\t{sum(argv)}")
    print(f"Average score:\t{round(sum(argv) / len(argv), 1)}")
    print(f"High score:\t{max_score}")
    print(f"Low score:\t{min(argv)}")
    print(f"Score range:\t{max_score - min(argv)}")


def main() -> None:
    print("=== Player Score Analytics ===")
    argv_int = argv_parser(sys.argv)
    if not argv_int:
        print("No scores provided." +
              " Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed: {argv_int}")
        score_parser(argv_int)


if __name__ == "__main__":
    main()
