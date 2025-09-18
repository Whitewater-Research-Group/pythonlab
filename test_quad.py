import pytest
from check import solve_quadraticx as solve_quadratic

def test_two_real_roots():
    result = solve_quadratic(1, -5, 6)  # x² - 5x + 6 = 0 → roots 2, 3
    assert result["type"] == "two real"
    assert result["roots"] == (2, 3)

def test_one_real_root():
    result = solve_quadratic(1, -4, 4)  # x² - 4x + 4 = 0 → root 2
    assert result["type"] == "one real"
    assert result["roots"] == (2, 2)

def test_complex_roots():
    result = solve_quadratic(2, 6, 7)  # 2x² + 6x + 7 = 0 → -1.5 ± 1.118i
    assert result["type"] == "complex"
    roots = result["roots"]
    assert roots[0] == pytest.approx(-1.5 + 1.1180339887j)
    assert roots[1] == pytest.approx(-1.5 - 1.1180339887j)


def test_not_quadratic():
    result = solve_quadratic(0, 2, 3)  # Not quadratic
    assert result["type"] == "not quadratic"
    assert result["roots"] is None
