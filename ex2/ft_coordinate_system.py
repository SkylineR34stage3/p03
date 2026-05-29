import sys


def tuple_parser(input_str: str) -> tuple | None:
    input_lst = input_str.split(',')
    results = []
    try:
        x, y, z = tuple(input_lst)
    except ValueError:
        print("Invalid syntax")
        return
    try:
        for val in (x, y, z):
            results.append(float(val.strip()))
    except ValueError as e:
        print(f"Error on parameter '{val}': {e}")
        return
    x, y, z = results
    return (x, y, z)


def input_parser() -> tuple | None:
    try:
        input_str = input("Enter new coordinates as floats in format 'x,y,z': ")
    except EOFError:
        print("Error occurred: EOFError. Dont input EOF pls")
        return
    return tuple_parser(input_str)


def main() -> None:
    print("=== Game Coordinate System ===")
    result = input_parser()
    while not result:
        result = input_parser()


if __name__ == "__main__":
    main()
