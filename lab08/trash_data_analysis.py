import re


class DataAnalysis:

    def __init__(self, file):
        self.top_lang_freqs = {}
        self.top_country_tlds_freqs = {}
        self.total = 0
        self.ROUND = 3
        self.file_data = self.read_data(file)
        self.setup()

    def read_data(self, file_name):
        # TODO: read the data and get the counts
        try:
            return open(file_name, "r", encoding="utf-8")
        except FileNotFoundError as e:
            print("Can't open", file_name)
            return

    def setup(self):
        """
        create two lists of tuples representing lang_freq
        and country domian_freq in the data
        ordered from highest frequency to lowest.
        """
        # read the first line of fields indication
        self.file_data.readline()

        # read line by line in the file object
        for line in self.file_data:
            email = line.strip().split(",")[3]
            language = line.strip().split(",")[6]
            self.total += 1
            self.add_x(language, self.top_lang_freqs)
            self.check_for_tlds(email)
        self.top_lang_freqs = sorted(self.top_lang_freqs.items(),
                                     key=lambda x: x[1],
                                     reverse=True)
        self.top_country_tlds_freqs = sorted(self.top_country_tlds_freqs.
                                             items(), key=lambda x: x[1],
                                             reverse=True)

        # list comprehension to change dictionary to list of tuples
        self.top_lang_freqs = [(item, round(count/self.total, self.ROUND))
                               for (item, count) in self.top_lang_freqs]
        self.top_country_tlds_freqs = [(item,
                                        round(count/self.total,
                                              self.ROUND))
                                       for (item, count)
                                       in self.top_country_tlds_freqs]

    def check_for_tlds(self, email):
        """
        Check whether the email contains country tlds
        Add tld if True
        """
        email_break = email.rfind('.')
        domain = email[email_break+1:]
        if (len(domain) == 2):
            self.add_x(domain, self.top_country_tlds_freqs)

    def add_x(self, x, dict):
        """
        add or update (key, value) in dictionary
        """
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1

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
