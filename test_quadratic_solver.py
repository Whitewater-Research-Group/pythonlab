import pytest
from quadratic_solver import quadratic_solver

def test_real_distinct_roots():
    result = quadratic_solver(1, -5, 6)  # roots 2 and 3
    assert pytest.approx(result[0]) in (2, 3)
    assert pytest.approx(result[1]) in (2, 3)

def test_real_equal_roots():
    result = quadratic_solver(1, -4, 4)  # root 2 (double)
    assert result == (2, 2)

def test_complex_roots():
    result = quadratic_solver(1, 1, 1)  # complex roots
    assert result == "complex roots found"

def test_large_coefficients():
    result = quadratic_solver(2, -8, 8)  # root 2 (double)
    assert result == (2, 2)

def test_negative_a():
    result = quadratic_solver(-1, 3, -2)  # roots 1 and 2
    assert pytest.approx(result[0]) in (1, 2)
    assert pytest.approx(result[1]) in (1, 2)
