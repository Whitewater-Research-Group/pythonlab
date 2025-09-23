import pytest
from quadraticEqn import solve_quadratic_eqn  # Replace 'your_module' with your actual filename (without .py)

def test_two_real_roots():
    r1, r2 = solve_quadratic_eqn(1, -5, 6)
    roots = sorted([r1.real, r2.real])
    expected = sorted([2, 3])
    assert pytest.approx(roots[0]) == expected[0]
    assert pytest.approx(roots[1]) == expected[1]


def test_one_real_root():
    r1, r2 = solve_quadratic_eqn(1, -2, 1)
    assert r1 == pytest.approx(1)
    assert r2 == pytest.approx(1)
def test_complex_roots():
    r1, r2 = solve_quadratic_eqn(1, 2, 5)

    # Sort roots by imaginary part to ensure consistent order
    roots = sorted([r1, r2], key=lambda x: x.imag)

    assert roots[0].real == pytest.approx(-1)
    assert roots[1].real == pytest.approx(-1)
    assert roots[0].imag == pytest.approx(-2)
    assert roots[1].imag == pytest.approx(2)

def test_zero_a_coefficient():
    result = solve_quadratic_eqn(0, 2, 3)
    assert result is None

def test_zero_division_handling():
    result = solve_quadratic_eqn(0, 0, 0)
    assert result is None