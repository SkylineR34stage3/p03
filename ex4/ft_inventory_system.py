import sys


def argv_parser(argv: list[str]) -> dict[str, int]:
    argv = argv[1:]
    inventory = {}
    for i in argv:
        slot: list[str] = i.split(':')
        if len(slot) == 1:
            print(f"Error - invalid parameter '{i}'")
            continue
        if slot[0] in inventory:
            print(f"Redundant item '{slot[0]}' - discarding")
            continue
        try:
            quantity = int(slot[1])
        except ValueError as e:
            print(f"Quantity error for '{slot[0]}': {e}: '{slot[1]}'")
            continue
        inventory.update({slot[0]: quantity})
    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===\n")
    inventory = argv_parser(sys.argv)
    print(f"Got inventory: {inventory}")


if __name__ == "__main__":
    main()
