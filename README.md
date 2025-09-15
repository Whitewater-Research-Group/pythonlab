#pythonlab

def quadratic_solver(a: float, b: float, c: float):
    """
    Solves quadratic equation ax^2 + bx + c = 0
    Returns tuple (x1, x2) if real roots, or string if complex roots.
    Note: a must be > 0
    """
    if a <= 0:
        raise ValueError("Coefficient 'a' must be greater than 0 for a quadratic equation.")

    d = b**2 - 4*a*c  # discriminant

    if d >= 0:
        x1 = (-b + d**0.5) / (2*a)
        x2 = (-b - d**0.5) / (2*a)
        return (x1, x2)
    else:
        return "complex roots found"


def get_positive_float_input(prompt: str) -> float:
    """Keep asking until user enters a valid number greater than 0."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("❌ Coefficient 'a' must be greater than 0.")
        except ValueError:
            print("❌ Invalid input! Please enter a number.")


def get_float_input(prompt: str) -> float:
    """Keep asking until user enters a valid number (can be negative or positive)."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")


if __name__ == "__main__":
    print("Quadratic Equation Solver: ax² + bx + c = 0")
    a = get_positive_float_input("Enter coefficient a (must be > 0): ")
    b = get_float_input("Enter coefficient b: ")
    c = get_float_input("Enter coefficient c: ")

    result = quadratic_solver(a, b, c)

    if isinstance(result, tuple):
        print(f"The roots are: x1 = {result[0]}, x2 = {result[1]}")
    else:
        print(result)
        Python Lab
