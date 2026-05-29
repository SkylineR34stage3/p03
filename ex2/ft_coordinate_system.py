import math


def tuple_parser(input_str: str) -> tuple[float, float, float] | None:
    input_lst = input_str.split(',')
    results: list[float] = []
    try:
        x, y, z = tuple(input_lst)
    except ValueError:
        print("Invalid syntax")
        return None
    try:
        for val in (x, y, z):
            results.append(float(val.strip()))
    except ValueError as e:
        print(f"Error on parameter '{val.strip()}': {e}")
        return None
    return (results[0], results[1], results[2])


def input_parser() -> tuple[float, float, float] | None:
    try:
        input_str = input(
            "Enter new coordinates as floats in format 'x,y,z': "
            )
    except EOFError:
        print("Error occurred: EOFError. Dont input EOF pls")
        return None
    return tuple_parser(input_str)


def cal_distance(
        t0: tuple[float, float, float],
        t1: tuple[float, float, float]
        ) -> float:
    return round(math.sqrt(
        (t1[0] - t0[0])**2 +
        (t1[1] - t0[1])**2 +
        (t1[2] - t0[2])**2
    ), 4)


def display_t1(t1: tuple[float, float, float]) -> None:
    print(f"Got a first tuple: {t1}")
    print(f"It includes: X={t1[0]}, Y={t1[1]}, Z={t1[2]}")
    t0 = (0.0, 0.0, 0.0)
    print(f"Distance to center: {cal_distance(t0, t1)}\n")


def display_t2(
        t1: tuple[float, float, float],
        t2: tuple[float, float, float]
        ) -> None:
    print(f"Got a second tuple: {t2}")
    print(f"It includes: X={t2[0]}, Y={t2[1]}, Z={t2[2]}")
    print(f"Distance between the 2 sets of coordinates: "
          f"{cal_distance(t1, t2)}")


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    t1 = input_parser()
    while not t1:
        t1 = input_parser()
    display_t1(t1)
    print("Get a second set of coordinates")
    t2 = input_parser()
    while not t2:
        t2 = input_parser()
    display_t2(t1, t2)


if __name__ == "__main__":
    main()
