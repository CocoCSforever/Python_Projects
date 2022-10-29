import some_functions as sf


# should have "test" in the name of file and functions
def test_multiply_numbers():
    """Test the multiply_numbers function"""
    assert sf.multiply_numbers(5, 10) == 50
    assert sf.multiply_numbers(-5, 10) == -50
    assert sf.multiply_numbers(2.5, 2) == 5.0
    assert sf.multiply_numbers(2.5, 1) == 2.5
    assert sf.multiply_numbers(2.5, 0) == 0
    assert sf.multiply_numbers('x', 5) == 'xxxxx'


def test_flatten_list_of_strings():
    """Test the flatten_list_of_strings_function"""
    s1 = "hello "
    s2 = "world."
    s3 = "1234"
    list_argument = [s1, s2, s3]
    conc = "hello world.1234"
    assert sf.flatten_list_of_strings(list_argument) == conc
