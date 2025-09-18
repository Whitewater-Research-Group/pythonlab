Report on Solving Quadratic Equations with Python

Introduction:

This project focuses on implementing a Python program to solve quadratic equations of the form:

𝑎𝑥^2+𝑏𝑥+𝑐=0

The task was to write a function that returns the type of roots (two real, one real, complex, or not quadratic) and the actual roots. In addition, the function was tested using pytest to ensure its correctness.

This report not only presents the final solution but also highlights the debugging journey, showing how errors were identified, corrected and validated.

The Problem:

Quadratic equations are a key topic in both mathematics and engineering. The discriminant:

𝐷=𝑏^2−4𝑎𝑐

is central to determining the nature of the roots:

D>0 → Two distinct real roots

D=0 → One real root (repeated)

D<0 → Two complex roots

a=0 → Not a quadratic equation

Implementation:

The Python function solve_quadraticx(a, b, c) was implemented using the cmath library to handle both real and complex roots.

Key features of the implementation:

Handles the case where 

a=0 (not quadratic).

Sorts real roots for consistency with test cases.

Returns results in a dictionary with "type" and "roots".

Designed to integrate smoothly with pytest.

Testing with Pytest

To ensure correctness, the function was tested with four scenarios:

Two Real Roots → 

x^2 −5x+6=0 → Roots: (2, 3)

One Real Root → 

x^2−4x+4=0 → Roots: (2, 2)

Complex Roots → 

2x^2+6x+7=0 → Roots: -1.5 ± 1.118i

Not Quadratic → 

x^2+2x+3=0 → No quadratic roots

Debugging Journey:

During testing, several issues appeared:

Mismatch in Root Order: The program returned (3, 2) instead of
 (2, 3). This was fixed by sorting the roots.

Complex Root Discrepancy: The expected test case initially assumed −3 ± 2i, but the actual correct roots were −1.5 ± 1.118i. Adjusting the test expectations solved this.

Discriminant Printing Error: The code tried to print "discriminant" from the result dictionary, but it wasn’t included. This was fixed by explicitly adding "discriminant" to the returned dictionary.

After corrections, all tests passed successfully.

Results:

The program now correctly handles all scenarios of quadratic equations:

Case Input (a, b, c) Output Type	Roots
Two Real Roots	(1, -5, 6)	two real	(2.0, 3.0)
One Real Root	(1, -4, 4)	one real	(2.0, 2.0)
Complex Roots	(2, 6, 7)	complex	(-1.5 ± 1.118i)
Not Quadratic	(0, 2, 3)	not quadratic	None

Conclusion:

This project demonstrated how Python can be used to implement and test mathematical solutions. Beyond just coding, the debugging process showed the importance of systematic testing and error correction.

The use of pytest ensured that the function was reliable under multiple scenarios. The final implementation is accurate, efficient, and educational, meeting both mathematical rigor and programming best practices.