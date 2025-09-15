from quadratic import findRoots

def test_two_real_roots():
    assert findRoots(1, -5, 6) == (3.0, 2.0)
    
def test_one_real_root():
    assert findRoots(1, -2, 1) == (1.0, 1.0)

def test_complex_roots():
    assert findRoots(1, 1, 1) == "complex roots"