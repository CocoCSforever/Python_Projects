from prime_generator import PrimeGenerator


def test_primes_to_max():
    """Test the primes_to_max method"""
    pg = PrimeGenerator()
    assert pg.primes_to_max(120) == [2, 3, 5, 7, 11, 13, 17,
                                     19, 23, 29, 31, 37, 41,
                                     43, 47, 53, 59, 61, 67,
                                     71, 73, 79, 83, 89, 97,
                                     101, 103, 107, 109, 113]
    assert 7919 in pg.primes_to_max(10000)
    assert 115249 in pg.primes_to_max(1000000)
    assert 2011 in pg.primes_to_max(2200)
    assert 181081 in pg.primes_to_max(1000000)
    assert 524287 in pg.primes_to_max(1000000)
