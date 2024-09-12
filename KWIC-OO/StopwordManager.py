from pathlib import Path
from typing import Set


class StopwordManager:
    
    def __init__(self, stoplist: Path):
        self._stopwords = self._load_stopwords(stoplist)

    def _load_stopwords(self, stoplist: Path) -> Set[str]:
        """Loads stopwords from the given file, ensuring data integrity."""
        with open(stoplist, 'r') as file:
            return {line.strip().lower() for line in file.readlines()}

    def is_stopword(self, word: str) -> bool:
        """Checks if the given word is a stopword."""
        return word.lower() in self._stopwords
