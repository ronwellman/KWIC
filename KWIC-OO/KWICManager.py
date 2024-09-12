from typing import List
from StopwordManager import StopwordManager


class KWICManager:

    def __init__(self, lines: List[str], stopword_manager: StopwordManager):
        self._lines = lines
        self._stopword_manager = stopword_manager
        self._shifts = []

    def _filter_stopwords(self, words: List[str]) -> List[str]:

        return [word for word in words if not self._stopword_manager.is_stopword(word)]

    def _generate_circular_shifts(self, words: List[str]) -> List[str]:

        return [" ".join(words[i:] + words[:i]) for i in range(len(words))]

    def generate_shifts(self) -> List[str]:

        for line in self._lines:
            words = line.split()
            filtered_words = self._filter_stopwords(words)
            self._shifts.extend(self._generate_circular_shifts(filtered_words))
        return self._shifts
