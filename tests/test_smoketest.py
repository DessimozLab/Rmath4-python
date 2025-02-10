from Rmath4 import rnorm, runif, pbinom
from math import log


def test_rnorm():
    assert 15 < rnorm(20, 1) < 25


def test_runif():
    assert 0 <= runif(0, 2) < 2


def test_pbinom():
    res = pbinom(1.5, 3, 0.5, 0, 0)
    assert res == 0.5


def test_pbinom_log():
    res = pbinom(2, 3, 0.5, 0, 1)
    assert res == log(0.125)
