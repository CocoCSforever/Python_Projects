from word_ladder import WordLadder
from word_ladder_app import load_words


def test_compare_len():
    """Test the compare_len method"""
    wl = WordLadder("earth", "earthen", None)
    assert wl.compare_len() is False
    wl = WordLadder("ocean", "oceanet", None)
    assert wl.compare_len() is False
    wl = WordLadder("earth", "ocean", None)
    assert wl.compare_len() is True


def test_make_ladder():
    """Test the make_ladder method"""
    english_words = load_words()
    wl = WordLadder("earth", "ocean", english_words[len("earth")])
    assert wl.make_ladder().__repr__() == "earth\tbarth\tbarih\tbaris\tbatis\t\
bitis\taitis\tantis\tantas\tantal\tontal\toctal\toctan\tocean\t"
    wl = WordLadder("angel", "devil", english_words[len("angel")])
    assert wl.make_ladder().__repr__() == "angel\tanger\taeger\tleger\tlever\t\
level\tdevel\tdevil\t"
    wl = WordLadder("love", "hate", english_words[len("love")])
    assert wl.make_ladder().__repr__() == "love\thove\thave\thate\t"


def test_check_word():
    """Test the check_word method"""
    english_words = load_words()
    wl = WordLadder("angel", "anger", english_words[len("angel")])
    wl.setup()
    assert wl.check_word("angel", wl.q.peek()) is True
    wl = WordLadder("angel", "areel", english_words[len("angel")])
    wl.setup()
    assert wl.check_word("angel", wl.q.peek()) is None
    wl = WordLadder("angel", "inger", english_words[len("angel")])
    wl.setup()
    assert wl.check_word("angel", wl.q.peek()) is None
    wl = WordLadder("angel", "oriel", english_words[len("angel")])
    wl.setup()
    assert wl.check_word("ariel", wl.q.peek()) is True
