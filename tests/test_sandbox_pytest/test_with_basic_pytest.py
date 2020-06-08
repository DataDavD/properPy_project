# tests that always pass/fail, testing pytest
def test_always_passes():
    assert True


# def test_always_fails():
#     assert False


def test_lowercase():
    assert "loud noises".lower() == "loud noises"


def test_reversed():
    assert list(reversed([1, 2, 3, 4, 5, 6, 7, 8])) == [8, 7, 6, 5, 4, 3, 2, 1]


def test_some_primes():
    assert 37 in {
        num
        for num in range(1, 50)
        if num != 1 and not any([num % div == 0 for div in range(2, num)])
    }
