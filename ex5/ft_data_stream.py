import random
import typing


def get_names() -> list[str]:
    return ["alice", "bob", "charlie", "dylan"]


def get_actions() -> list[str]:
    return ["run", "eat", "sleep", "grab", "move", "swim", "climb",
            "release", "use"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    names = get_names()
    actions = get_actions()
    while True:
        yield (random.choice(names), random.choice(actions))


def get_ten_events() -> list[tuple[str, str]]:
    ten_events: list[tuple[str, str]] = []
    g = gen_event()
    for _ in range(10):
        ten_events.append(next(g))
    return ten_events


def main() -> None:
    print("=== Game Data Stream Processor ===\n")
    g = gen_event()
    for i in range(1000):
        name, action = next(g)
        print(f"Event {i}: Player {name} did action {action}")
    ten_events = get_ten_events()
    print(f"Built list of 10 events: {ten_events}")


if __name__ == "__main__":
    main()
