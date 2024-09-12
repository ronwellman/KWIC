from typing import List


class KWICSorter:

    def __init__(self, shifts: List[str]):
        self._shifts = shifts

    def sort_shifts(self) -> List[str]:
        return sorted(self._shifts, key = str.casefold)
