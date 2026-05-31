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
            print(f"Quantity error for '{slot[0]}': {e}")
            continue
        inventory.update({slot[0]: quantity})
    return inventory


def get_min_max(inventory: dict[str, int]) -> tuple[str, str]:
    min_key = list(inventory.keys())[0]
    max_key = list(inventory.keys())[0]

    for key in inventory:
        if inventory[key] < inventory[min_key]:
            min_key = key
        if inventory[key] > inventory[max_key]:
            max_key = key

    return (min_key, max_key)


def print_item_stats(inventory: dict[str, int]) -> None:
    item_count = len(inventory)
    total = sum(inventory.values())
    print(f"Total quantity of the {item_count} items: {total}")
    for key in inventory:
        percentage = round((inventory[key] / total) * 100, 1)
        print(f"Item {key} represents {percentage}%")
    min_max = get_min_max(inventory)
    print(
        f"Item most abundant: {min_max[1]}"
        f" with quantity {inventory[min_max[1]]}"
        )
    print(
        f"Item least abundant: {min_max[0]}"
        f" with quantity {inventory[min_max[0]]}"
        )


def main() -> None:
    print("=== Inventory System Analysis ===\n")
    inventory = argv_parser(sys.argv)
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print_item_stats(inventory)


if __name__ == "__main__":
    main()
