import math


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
        input_str = input(
            "Enter new coordinates as floats in format 'x,y,z': "
            )
    except EOFError:
        print("Error occurred: EOFError. Dont input EOF pls")
        return
    return tuple_parser(input_str)


def cal_distance(t0: tuple, t1: tuple) -> float:
    return math.sqrt(
        (t1[0] - t0[0])**2 +
        (t1[1] - t0[1])**2 +
        (t1[2] - t0[2])**2
    )


def display_t1(t1: tuple) -> None:
    print(f"Got a first tuple: {t1}")
    print(f"It includes: X={t1[0]}, Y={t1[1]}, Z={t1[2]}")
    t0 = (0.0, 0.0, 0.0)
    print(f"Distance to center: {round(cal_distance(t0, t1), 4)}\n")


def main() -> None:
    print("=== Game Coordinate System ===\n")
    t1 = input_parser()
    while not t1:
        t1 = input_parser()
    display_t1(t1)


if __name__ == "__main__":
    main()
