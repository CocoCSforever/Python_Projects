from text_cleaner import TextCleaner
from ngram_frequencies import NgramFrequencies


def main():
    tc = TextCleaner("corpse_bride.txt")
    text = tc.read_file()
    unigrams_freq = NgramFrequencies(1)
    unigrams_freq.set_up(text)

    bigrams_freq = NgramFrequencies(2)
    bigrams_freq.set_up(text)

    trigrams_freq = NgramFrequencies(3)
    trigrams_freq.set_up(text)

    print("Top 10 unigrams:")
    unigrams_freq.print_top_n_freqs(10)
    print("Top 10 bigrams:")
    bigrams_freq.print_top_n_freqs(10)
    print("Top 10 trigrams:")
    trigrams_freq.print_top_n_freqs(10)


main()
