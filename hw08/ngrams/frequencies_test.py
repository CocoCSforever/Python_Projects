from ngram_frequencies import NgramFrequencies


def test_set_up():
    unigrams = NgramFrequencies(1)
    unigrams.set_up("I love coding very much. I love coding.")
    assert unigrams.counts == {'I': 2, 'love': 2, 'coding': 2,
                               'very': 1, 'much': 1}

    unigrams = NgramFrequencies(1)
    unigrams.set_up("\nI love coding very much. I love coding.\n")
    assert unigrams.counts == {'I': 2, 'love': 2, 'coding': 2,
                               'very': 1, 'much': 1}

    bigrams = NgramFrequencies(2)
    bigrams.set_up("\nI love coding very much. I love coding.\n")
    assert bigrams.counts == {'I_love': 2, 'love_coding': 2,
                              'coding_very': 1, 'very_much': 1}


def test_add_item():
    unigrams = NgramFrequencies(1)
    unigrams.add_item("the")
    unigrams.add_item("the")
    unigrams.add_item("be")
    unigrams.add_item("good")
    unigrams.add_item("the")
    assert unigrams.counts == {'the': 3, 'be': 1, 'good': 1}


def test_top_n_counts():
    unigrams = NgramFrequencies(1)
    unigrams.set_up("I love coding very much. I hate coding.")
    assert unigrams.top_n_counts() == [('I', 2), ('coding', 2), ('love', 1),
                                       ('very', 1), ('much', 1), ('hate', 1)]
    unigrams.set_up("hate much hate much hate")
    assert unigrams.top_n_counts() == [('hate', 4), ('much', 3),
                                       ('I', 2), ('coding', 2),
                                       ('love', 1), ('very', 1), ]


def test_top_freqs():
    unigrams = NgramFrequencies(1)
    unigrams.set_up("I love coding very much. I hate coding.")
    assert unigrams.top_n_freqs() == [('I', 0.25), ('coding', 0.25),
                                      ('love', 0.125), ('very', 0.125),
                                      ('much', 0.125), ('hate', 0.125)]
    unigrams.set_up("hate much hate much hate hate\
 hate hate hate very love love")
    assert unigrams.top_n_freqs() == [('hate', 0.4), ('love', 0.15),
                                      ('much', 0.15), ('I', 0.1),
                                      ('coding', 0.1), ('very', 0.1), ]


def test_frequency():
    unigrams = NgramFrequencies(1)
    unigrams.set_up("I love coding very much. I love coding.")
    assert unigrams.frequency('love') == 0.25
    assert unigrams.frequency('very') == 0.125
    assert unigrams.frequency('coding') == 0.25
