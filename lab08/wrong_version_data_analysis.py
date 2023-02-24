import re


class DataAnalysis:

    def __init__(self, file):
        # TODO: set up the necessary instance variables
        self.top_lang_freqs = {}
        self.top_country_tlds_freqs = {}
        self.total = 0
        self.country_tlds_total = 0
        self.ROUND = 3
        self.file_data = self.read_data(file)
        self.top_freqs()
        self.smth

    def read_data(self, file_name):
        # TODO: read the data and get the counts
        try:
            return open(file_name, "r", encoding="utf-8")
        except FileNotFoundError as e:
            print("Can't open", file_name)
            return

    def top_freqs(self):
        """
        creat two lists of tuples representing lang_freq
        and country domian_freq in the data
        ordered from highest frequency to lowest.
        """
        self.file_data = self.file_data.read()
        tlds_list = re.findall(r'\.([a-z][a-z]),', self.file_data.strip())
        language_list = re.findall(r',([A-Za-z]+)\n',
                                   self.file_data.strip())[1:]
        self.total = len(language_list)

        for i in tlds_list:
            self.add_x(i, self.top_country_tlds_freqs)
        for i in language_list:
            self.add_x(i, self.top_lang_freqs)
        # print(tlds_list)
        # print(language_list)

        # self.sort_list(self.top_lang_freqs)
        self.top_lang_freqs = self.sort_list(self.top_lang_freqs)
        # print(id(self.top_lang_freqs))
        # self.sort_list(self.top_country_tlds_freqs)
        self.top_lang_freqs = [(item, round(count/self.total, self.ROUND))
                               for (item, count) in self.top_lang_freqs]
        self.top_country_tlds_freqs = [(item,
                                        round(count/self.total,
                                              self.ROUND))
                                       for (item, count)
                                       in self.top_country_tlds_freqs]
        print(self.top_lang_freqs)
        print(self.top_country_tlds_freqs)

    def add_x(self, x, dict):
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1

    def sort_list(self, dict):
        print(dict)
        print(id(dict))
        dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        print(dict)
        print(id(dict))
        print("over")
        return dict

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
