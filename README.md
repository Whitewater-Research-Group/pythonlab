**##### Debbuging Process



1. Zero division error

* Problem: When a=o, the program crashed
* Fix: Added a check to raise a "ValueError" if a=o



2\. Negative Discriminant:

* Problem: Using math.sqrt() failed for negative values.
* Fix: Replaced with cmath.sqrt() to handle both real and complex roots.



3\. Input Errors:

* Problem: String inputs caused crashes.
* Fix: Converted inputs to float before processing.



##### Testing Process



* Manual Tests:



Verified results with known quadratic equations.



Example: x² - 3x + 2 = 0 → Roots: 2 and 1.



Example: x² + 2x + 5 = 0 → Roots: -1+2j and -1-2j.



* Automated Tests (pytest):



Created test cases for real roots, complex roots, and invalid input.



All tests passed successfully using pytest.



##### Conclusion



The program is stable, handles both real and complex solutions, rejects invalid inputs, and passes all manual and automated test cases.

