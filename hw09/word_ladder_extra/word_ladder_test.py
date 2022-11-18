from word_ladder import WordLadder
from word_ladder_app import load_words


def test_make_ladder():
    """Test the make_ladder method"""
    english_words = load_words()
    wl = WordLadder("cat", "hat", english_words)
    assert wl.make_ladder().__repr__() == "cat\that\t"
    wl = WordLadder("angel", "devil", english_words)
    assert wl.make_ladder().__repr__() == "angel\targel\tareel\treel\trevel\
\tdevel\tdevil\t"
    wl = WordLadder("love", "hate", english_words)
    assert wl.make_ladder().__repr__() == "love\thove\thave\thate\t"


def test_generate_word():
    english_words = load_words()
    wl = WordLadder("angel", "revel", english_words)
    wl.setup()
    assert wl.generate_word("reel", wl.q.peek()) is True
    assert wl.generate_word("areel", wl.q.peek()) is None
    wl.w2 = "areel"
    wl.checked = set()
    assert wl.generate_word("argel", wl.q.peek()) is True
    assert wl.generate_word("angel", wl.q.peek()) is None


def test_add_letter():
    english_words = load_words()
    wl = WordLadder("angel", "revel", english_words)
    wl.setup()
    assert wl.add_letter(2, ord('v')-ord('a'), "reel", wl.q.peek()) is True
    assert wl.add_letter(2, ord('c')-ord('a'), "reel", wl.q.peek()) is None
    wl = WordLadder("earth", "ecad", english_words)
    wl.setup()
    assert wl.add_letter(1, ord('c')-ord('a'), "ead", wl.q.peek()) is True
    assert wl.add_letter(2, ord('c')-ord('a'), "ead", wl.q.peek()) is None
    wl.w2 = "ectad"
    assert wl.add_letter(2, ord('t')-ord('a'), "ecad", wl.q.peek()) is True


def test_delete_letter():
    english_words = load_words()
    wl = WordLadder("angel", "reel", english_words)
    wl.setup()
    assert wl.delete_letter(0, "areel", wl.q.peek()) is True
    wl.checked.remove("reel")
    assert wl.delete_letter(2, "revel", wl.q.peek()) is True
    wl = WordLadder("earth", "ecad", english_words)
    wl.setup()
    assert wl.delete_letter(2, "ectad", wl.q.peek()) is True
    wl.checked.remove("ecad")
    assert wl.delete_letter(1, "ectad", wl.q.peek()) is None
    wl.w2 = "eat"
    assert wl.delete_letter(3, "eath", wl.q.peek()) is True


def test_replace_letter():
    english_words = load_words()
    wl = WordLadder("angel", "devel", english_words)
    wl.setup()
    assert wl.replace_letter(0, ord('d')-ord('a'), "revel", wl.q.peek())\
        is True
    assert wl.replace_letter(0, ord('f')-ord('a'), "revel", wl.q.peek())\
        is None
    wl = WordLadder("earth", "ocean", english_words)
    wl.setup()
    assert wl.replace_letter(2, ord('e')-ord('a'), "octan", wl.q.peek())\
        is True
    assert wl.replace_letter(2, ord('e')-ord('a'), "octad", wl.q.peek())\
        is None


def test_check_new_word():
    """Test the check_word method"""
    english_words = load_words()
    wl = WordLadder("angel", "areel", english_words)
    wl.setup()
    assert wl.check_new_word("anger", wl.q.peek()) is None
    assert wl.check_new_word("lingel", wl.q.peek()) is None
    assert wl.check_new_word("areel", wl.q.peek()) is True

    wl = WordLadder("angel", "devil", english_words)
    wl.setup()
    assert wl.check_new_word("reel", wl.q.peek()) is None
    assert wl.check_new_word("devel", wl.q.peek()) is None
    assert wl.check_new_word("devil", wl.q.peek()) is True
