from Rmath4 import rnorm, runif


def test_rnorm():
    assert 15 < rnorm(20, 1) < 25


def test_runif():
    assert 0 <= runif(0, 2) < 2