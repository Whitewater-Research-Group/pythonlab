import pytest
from quadratic import solve_quadratic

def test_real_roots():
    roots = solve_quadratic(1, -3, 2)  # x^2 - 3x + 2 = 0
    assert roots == (2, 1) or roots == (1, 2)

def test_complex_roots():
    roots = solve_quadratic(1, 2, 5)  # x^2 + 2x + 5 = 0
    expected = (-1+2j, -1-2j)
    assert roots == expected or roots == (expected[1], expected[0])

def test_invalid_quadratic():
    with pytest.raises(ValueError):
        solve_quadratic(0, 2, 3)
