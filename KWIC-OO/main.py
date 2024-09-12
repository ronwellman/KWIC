import os
import sys
from KWICController import KWICController

if __name__ == "__main__":
    input_path = "test_input.txt"

    stoplist_path = "stoplist.txt"

    output_path = "index.txt"

    if not os.path.exists(input_path):
        print(f"Input file {input_path} does not exist.")
        sys.exit(1)

    if not os.path.exists(stoplist_path):
        print(f"Stoplist file {stoplist_path} does not exist.")
        sys.exit(1)

    # Create the KWIC controller and process the input file
    controller = KWICController(input_path, stoplist_path, output_path)
    controller.process()