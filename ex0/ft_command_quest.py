import sys


def argv_parser(argv: list[str]) -> None:
    argv_l = len(argv)
    print(f"Program name: {argv[0]}")
    if argv_l == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {argv_l - 1}")
        i = 1
        while (i < argv_l):
            print(f"Argument {i}: {argv[i]}")
            i += 1
    print(f"Total arguments: {argv_l}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    argv_parser(sys.argv)
