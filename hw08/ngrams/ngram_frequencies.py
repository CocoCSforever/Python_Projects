class NgramFrequencies:
    def __init__(self, n):
        self.counts = {}
        self.top_counts = []
        self.top_freqs = []
        self.total = 0
        self.n = n
        self.ROUND = 3

    def set_up(self, text):
        # get a list of paragraphs
        text = text.split("\n")
        for para in text:
            # get a list of sentence
            sentence_list = para.split(".")
            for sentence in sentence_list:
                words = sentence.strip().split()
                for i in range(0, len(words)+1-self.n):
                    item = ''
                    for j in range(self.n):
                        item = item + '_' + words[i+j]
                    self.add_item(item[1:])
        self.top_n_counts()
        self.top_n_freqs()

    def add_item(self, item):
        self.total += 1
        if item in self.counts:
            self.counts[item] += 1
        else:
            self.counts[item] = 1

    def top_n_counts(self, n=None):
        """Returns a list of items sorted on the count,
        with the most frequent first"""
        self.top_counts = sorted(self.counts.items(),
                                 key=lambda x: x[1],
                                 reverse=True)
        return self.top_counts[:n]

    def top_n_freqs(self, n=None):
        """Returns a similar list as above,
        but with frequencies instead of counts"""
        self.top_freqs = [(item, round(count/self.total, self.ROUND))
                          for (item, count) in self.top_counts]
        return self.top_freqs[:n]

    def print_top_n_freqs(self, n=-1):
        for tuple in self.top_freqs[:n]:
            print("\t", tuple)

    def frequency(self, item):
        """Takes an item and returns its frequency"""
        return self.counts[item]/self.total
