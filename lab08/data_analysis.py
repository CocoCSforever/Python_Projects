import re


class DataAnalysis:

    def __init__(self, file):
        self.top_lang_freqs = {}
        self.top_country_tlds_freqs = {}
        self.total = 0
        self.file_data = None
        self.setup(file)

    def setup(self, file_name):
        """Read file and reate a file object"""
        try:
            self.file_data = open(file_name, "r", encoding="utf-8")
        except FileNotFoundError as e:
            print("Can't open", file_name)
            return
        self.read_data()

    def read_data(self):
        """
        create two lists of tuples representing lang_freq
        and country domian_freq in the data
        ordered from highest frequency to lowest.
        """
        self.file_data = self.file_data.read()

        # if use strip and remove the trailing whitespace
        # cannot match \n for the last one
        # be aware of "Māori" and "Irish Gaelic"
        language_list = re.findall(r',([\w ]+)\n', self.file_data)[1:]
        tlds_list = re.findall(r'\.([a-z][a-z]),', self.file_data)
        self.total = len(language_list)

        for i in language_list:
            self.add_x(i, self.top_lang_freqs)
        for i in tlds_list:
            self.add_x(i, self.top_country_tlds_freqs)

        # change dictionary to a sorted list of tuples
        self.top_lang_freqs = self.sort_list(self.top_lang_freqs)
        self.top_country_tlds_freqs =\
            self.sort_list(self.top_country_tlds_freqs)

        # list comprehension for freqs%
        self.top_lang_freqs = [(item, count/self.total)
                               for (item, count) in self.top_lang_freqs]
        self.top_country_tlds_freqs = [(item, count/self.total)
                                       for (item, count)
                                       in self.top_country_tlds_freqs]

    def add_x(self, x, dict):
        """
        add or update (key, value) in dictionary
        """
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1

    def sort_list(self, dict):
        """
        Sort dictionary by freqs and return a list of tuples by sequence
        """
        return sorted(dict.items(),
                      key=lambda x: x[1],
                      reverse=True)

    def top_n_lang_freqs(self, n):
        """
        take a number N as an argument and return
        an N-length sublist of top freqs of language
        """
        return self.top_lang_freqs[:n]

    def top_n_country_tlds_freqs(self, n):
        """
        take a number N as an argument and return
        an N-length sublist of top freqs of country domain
        """
        return self.top_country_tlds_freqs[:n]
