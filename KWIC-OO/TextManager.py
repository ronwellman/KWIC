from pathlib import Path
from typing import List


class TextManager:

    def __init__(self, input_file: Path):
        self._lines = self._load_lines(input_file)

    def _load_lines(self, input_file: Path) -> List[str]:
        with open(input_file, 'r') as file:
            return [line.strip() for line in file.readlines() if line.strip()]

    def get_lines(self) -> List[str]:
        return self._lines
