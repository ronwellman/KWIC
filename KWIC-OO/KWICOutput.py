from pathlib import Path
from typing import List

class KWICOutput:

    def __init__(self, sorted_shifts: List[str], output_file: Path):
        self._sorted_shifts = sorted_shifts
        self._output_file = output_file

    def to_console(self):

        print("KWIC Index:")
        for shift in self._sorted_shifts:
            print(shift)

    def to_file(self):

        with open(self._output_file, 'w') as file:
            file.write("\n".join(self._sorted_shifts))
