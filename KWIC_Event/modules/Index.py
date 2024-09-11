from dataclasses import dataclass, field
from collections import defaultdict
from pathlib import Path


@dataclass
class Index:
    """
    Generatic Index object for passing between functions
    """

    # keywords: defaultdict = field(default_factory=lambda: defaultdict(list))
    # last_line: list[str] = field(default_factory=lambda: list)
    # output_file: Path = Path()
    # stop_list: set[str] = field(default_factory=lambda: set)
    # context: int = 5
    keywords: defaultdict
    last_line: list[str]
    output_file: Path
    stop_list: set[str]
    context: int = 5
