

import cmath  # For handling complex numbers


def solve_quadratic_eqn(a, b, c):
    if a == 0:
        print("Coefficient 'a' cannot be zero for a quadratic equation.")
        return None

    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    elif discriminant == 0:
        root1 = -b / (2*a)
        root2 = root1
    else:
        root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2*a)

    return root1, root2


def get_user_input():
    while True:
        try:
            a = float(input("input the coefficient of a:"))
            b = float(input("input the coefficient of b:"))
            c = float(input("input the coefficient of c:"))
            return a,b,c
        
        except ValueError:
            print("invalid input, please enter a valid input")
    
    
def main():
    a,b,c = get_user_input()
    result = solve_quadratic_eqn(a,b,c)
    print(f"The roots of the equation are {result}")

if __name__ == "__main__":
    main()





