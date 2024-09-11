from collections import defaultdict
from enum import Enum
from .Index import Index


class EventType(Enum):
    NEW_LINE = 1
    OUTPUT = 2


class EventHandler:
    handlers: defaultdict = defaultdict(list)

    def __init__(self, index: Index):
        self.index = index

    def register(self, event_type: EventType, fn) -> None:
        self.handlers[event_type].append(fn)

    def trigger(self, event_type: EventType, line: list[str]) -> None:
        self.index.last_line = line
        for fn in self.handlers[event_type]:
            fn(self.index)


def handle_prep(index: Index) -> None:
    """
    lowercases words within the line
    """
    index.last_line = [line.lower().strip() for line in index.last_line]


def register_prep(handler: EventHandler) -> None:
    """
    registers the prep event
    """
    handler.register(EventType.NEW_LINE, handle_prep)


def handle_shift(index: Index) -> None:
    """
    Pulls out each word as a keyword
    """

    for i, keyword in enumerate(index.last_line):
        if keyword in index.stop_list:
            continue

        left = i - index.context if (i - index.context) > 0 else 0
        temp = index.last_line[left:i]

        # make the keyword stand out for easier identification
        temp.append(keyword.upper())

        temp.extend(index.last_line[i + 1 : i + 1 + index.context])

        index.keywords[keyword].append(" ".join(temp))
        # index.keywords[keyword].append(" ".join(index.last_line))


def register_shift(handler: EventHandler) -> None:
    """
    registers the shift event
    """
    handler.register(EventType.NEW_LINE, handle_shift)


def handle_sort(index: Index) -> None:
    """
    Sorts the keyword entries
    """
    for keyword in index.last_line:
        # temporarily lowercase everything during the sort
        index.keywords[keyword].sort(key=lambda x: [w.lower() for w in x])


def register_sort(handler: EventHandler) -> None:
    """
    registers the sort event
    """
    handler.register(EventType.NEW_LINE, handle_sort)


def handle_output(index: Index) -> None:
    """
    Writes the output to disk
    """
    with open(index.output_file, "w") as f:
        for keyword in sorted(index.keywords):
            for line in index.keywords[keyword]:
                f.write(f"{line}\n")


def register_output(handler: EventHandler) -> None:
    """
    Registers an output event
    """
    handler.register(EventType.OUTPUT, handle_output)
