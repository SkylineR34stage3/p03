import random
import typing


def get_names() -> list[str]:
    return ["alice", "bob", "charlie", "dylan"]


def get_events() -> list[str]:
    return ["run", "eat", "sleep", "grab", "move", "swim", "climb",
            "release", "use"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    names = get_names()
    events = get_events()
    while True:
        yield (random.choice(names), random.choice(events))


def main() -> None:
    print("=== Game Data Stream Processor ===\n")
    g = gen_event()
    for i in range(1000):
        name, event = next(g)
        print(f"Event {i}: Player {name} did action {event}")


if __name__ == "__main__":
    main()
