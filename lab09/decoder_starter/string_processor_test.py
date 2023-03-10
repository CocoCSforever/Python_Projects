from string_processor import StringProcessor


def test_process_string():
    """Test for process_string function"""
    # Include the following cases
    # "ab" should yield "" as ouptut
    # "ab*" should yield "b" as output
    # "ab^" should yield "ba" as output
    # "^" should yield "" as output
    sp = StringProcessor()
    assert sp.process_string("ab") == ""
    sp = StringProcessor()
    assert sp.process_string("ab*") == "b"
    sp = StringProcessor()
    assert sp.process_string("ab^") == "ba"
    sp = StringProcessor()
    assert sp.process_string("^") == ""
