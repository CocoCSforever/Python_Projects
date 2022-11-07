from character_freqs import CharFreqs


def test_constructor():
    """Test the constructor"""
    char_freqs = CharFreqs()
    empty_count = 0
    assert char_freqs.total_count == empty_count
    assert char_freqs.char_counts == {}


def test_count_line():
    """Test the count line method"""
    char_freqs = CharFreqs()
    char_freqs.count_line("ab;A")
    count_a = 2
    count_b = 1
    assert char_freqs.char_counts['a'] == count_a
    assert char_freqs.char_counts['b'] == count_b
    assert ';' not in char_freqs.char_counts.keys()

    char_freqs = CharFreqs()
    char_freqs.count_line("\n")
    assert len(char_freqs.char_counts.keys()) == 0


def test_sorted_counts_property():
    """Test the sorted_counts property"""
    char_freqs = CharFreqs()
    char_freqs.count_line("aba")
    count_a = 2
    number_of_counts = 2
    assert char_freqs.sorted_counts[0][0] == 'a'
    assert char_freqs.sorted_counts[0][1] == count_a
    assert len(char_freqs.sorted_counts) == number_of_counts


def test_char_freqs():
    """Test the sorted frequencies prroperty"""
    char_freqs = CharFreqs()
    char_freqs.count_line("aba")
    freq_a = 2/3
    precision = 2
    assert char_freqs.char_freqs['a'] == round(freq_a, precision)
