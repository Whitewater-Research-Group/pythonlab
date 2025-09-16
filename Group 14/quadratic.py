import cmath  # handles both real and complex roots

def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation.")

    discriminant = (b ** 2) - (4 * a * c)
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

    return root1, root2


if __name__ == "__main__":
    print("Quadratic Equation Solver: ax^2 + bx + c = 0")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    try:
        roots = solve_quadratic(a, b, c)
        print(f"The roots are: {roots[0]} and {roots[1]}")
    except ValueError as e:
        print(f"Error: {e}")
