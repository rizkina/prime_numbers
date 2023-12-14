from project import prime_selector, is_prime, sum_primes


def test_prime_selector():
    assert prime_selector(1, 10) == [2, 3, 5, 7]
    assert prime_selector(1, 25) == [2, 3, 5, 7, 11, 13, 17, 19, 23]
    assert prime_selector(10, 25) == [11, 13, 17, 19, 23]
    assert prime_selector(0, 0) == []
    assert prime_selector(-10, 0) == []


def test_is_prime():
    assert is_prime(-1) == False
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(7) == True
    assert is_prime(9) == False
    assert is_prime(101) == True
    assert is_prime(903) == False


def test_sum_primes():
    assert sum_primes(1, 2) == 2
    assert sum_primes(1, 10) == 17
    assert sum_primes(1, 100) == 1060
    assert sum_primes(1, 777) == 48494
    assert sum_primes(10, 25) == 83
