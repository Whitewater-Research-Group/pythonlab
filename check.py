import cmath

def solve_quadraticx(a: float, b: float, c: float):
    """
    Solve a quadratic equation ax^2 + bx + c = 0
    Returns a dictionary with:
      - "type": "two real", "one real", "complex", "not quadratic"
      - "roots": tuple of roots, or None
      - "discriminant": float
    """
    if a == 0:
        return {"type": "not quadratic", "roots": None, "discriminant": None}

    discriminant = b**2 - 4*a*c
    sqrt_disc = cmath.sqrt(discriminant)

    root1 = (-b + sqrt_disc) / (2*a)
    root2 = (-b - sqrt_disc) / (2*a)

    if discriminant > 0:
        roots = tuple(sorted((root1.real, root2.real)))
        return {"type": "two real", "roots": roots, "discriminant": discriminant}
    elif discriminant == 0:
        root = root1.real
        return {"type": "one real", "roots": (root, root), "discriminant": discriminant}
    else:
        roots = (root1, root2)
        return {"type": "complex", "roots": roots, "discriminant": discriminant}


if __name__ == "__main__":
    try:
        a, b, c = map(float, input("Enter coefficients a, b, c: ").split())
        result = solve_quadraticx(a, b, c)
        print(f"Discriminant: {result['discriminant']}")
        print(f"Type: {result['type']}")
        print(f"Roots: {result['roots']}")
    except Exception as e:
        print("Error:", e)
