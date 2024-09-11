#!/usr/bin/env python3
import argparse
import sys

from pathlib import Path
from collections import defaultdict
from modules import (
    EventType,
    EventHandler,
    register_sort,
    register_shift,
    register_prep,
    register_output,
)
from modules.Index import Index


def main(input_file: Path, output_file: Path, stop_list: set[str], context: int):

    index = Index(
        keywords=defaultdict(list),
        last_line=[],
        output_file=output_file,
        stop_list=stop_list,
        context=context,
    )

    event_handler = EventHandler(index)

    # order of registration is important
    register_prep(event_handler)
    register_shift(event_handler)
    register_sort(event_handler)
    register_output(event_handler)

    with open(input_file, "r") as f:
        for line in f.readlines():
            # trigger that a new line has been read
            event_handler.trigger(EventType.NEW_LINE, line.split())

    # trigger that all lines have been read
    event_handler.trigger(EventType.OUTPUT, [])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "Attempt the KWIC with event architecture (observer pattern)"
    )
    parser.add_argument(
        "--input",
        "-i",
        required=True,
        type=str,
        help="input text file to build the index from",
    )
    parser.add_argument(
        "--output",
        "-o",
        required=True,
        type=str,
        help="output text file to write the index to",
    )
    parser.add_argument(
        "--stop_list",
        "-s",
        required=False,
        type=str,
        help="a stop list of words to ignore",
    )
    parser.add_argument(
        "--context",
        "-c",
        required=False,
        type=int,
        default=5,
        help="size of the context round the keyword",
    )

    args = parser.parse_args()

    if args.context < 0:
        print("context must be a positive integer")
        sys.exit(1)

    input_file = Path(args.input)
    output_file = Path(args.output)

    if not input_file.exists():
        print(f"{input_file} does not exist.")
        sys.exit(2)

    if args.stop_list:
        if not Path(args.stop_list).exists():
            print(f"{args.stop_list} does not exist.")
            sys.exit(3)

        with open(args.stop_list, "r") as f:
            stop_list = set((word.strip() for word in f.readlines()))
    else:
        stop_list = set()

    main(input_file, output_file, stop_list, args.context)
