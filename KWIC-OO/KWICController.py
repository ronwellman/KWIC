from pathlib import Path
from TextManager import TextManager
from StopwordManager import StopwordManager
from KWICManager import KWICManager
from KWICSorter import KWICSorter
from KWICOutput import KWICOutput


class KWICController:

    def __init__(self, input_file: Path, stoplist_file: Path, output_file: Path):
        self._text_manager = TextManager(input_file)
        self._stopword_manager = StopwordManager(stoplist_file)
        self._output_file = output_file

    def process(self):
        # Step 1: Load and process the text
        lines = self._text_manager.get_lines()

        # Step 2: Generate circular shifts, filtering stopwords
        kwic_manager = KWICManager(lines, self._stopword_manager)
        shifts = kwic_manager.generate_shifts()

        # Step 3: Sort the shifts
        sorter = KWICSorter(shifts)
        sorted_shifts = sorter.sort_shifts()

        # Step 4: Output the sorted shifts
        output = KWICOutput(sorted_shifts, self._output_file)
        output.to_console()  # Optional: Output to console
        output.to_file()  # Save to file
