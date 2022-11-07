import re


class CharFreqs:
    """Handle counts and frequency
    calculations of characters"""
    def __init__(self):
        self.char_counts = {}
        self.total_count = 0

    def count_line(self, line):
        """Process a line of characters"""
        chars = re.findall(r"\w", line.lower())
        for ch in chars:
            self.add_char(ch)

    def add_char(self, char):
        """Add character to the counts"""
        self.total_count += 1
        if char in self.char_counts.keys():
            self.char_counts[char] += 1
        else:
            self.char_counts[char] = 1

    @property
    def sorted_counts(self):
        """Return list of sorted counts as property"""
        return sorted(
                self.char_counts.items(),
                key=lambda x: x[1],
                reverse=True
            )

    @property
    def char_freqs(self):
        """Return dictionary of frequencies as property"""
        ROUND_PLACES = 2
        # dictionary comprehension
        return {k: round(self.char_counts[k]/self.total_count, ROUND_PLACES)
                for k in self.char_counts.keys()}

    @property
    def sorted_freqs(self):
        """Return list of sorted freqs as property"""
        return sorted(
                self.char_freqs.items(),
                key=lambda x: x[1],
                reverse=True
            )
