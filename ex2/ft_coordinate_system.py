import sys


def input_parser(input_str: str) -> tuple | None:
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


def main() -> None:
    print("=== Game Coordinate System ===")
    input_str = input("Enter new coordinates as floats in format 'x,y,z': ")
    print (f"{input_parser(input_str)}")


if __name__ == "__main__":
    main()
