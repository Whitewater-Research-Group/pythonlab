# Code Testing and Debugging Report For Quadratic Equation
 

## Introduction

 This report documents the testing and debugging effort for a quadratic equation solver
 implemented in Python. The solver takes coefficients a, b, and c as input and calculates the roots
 of the quadratic equation 
 >ax^2 + bx + c = 0.
 
## Testing Methodology
 
- **Testing approach**: Unit testing and integration testing were employed to ensure the solver's
 correctness.
- **Test cases**: Various test cases were designed to cover different scenarios, including:
    - Real roots
    - Complex roots
    - Repeated roots
    - Edge cases (e.g., a = 0, b = 0, c = 0)
- **Testing tools**: The Python package pytest was used for testing.
 
- **Test Results**
    - Summary: 5 test cases were executed, with 3 passing and 2 failing initially.
    -  Issues encountered: Two test cases failed due to incorrect handling of complex roots.
    -  Screenshots/logs: Not applicable, but test output logs were reviewed to identify issues.

  
## Debugging Process
- **Debugging approach**: The debugger was used to step through the code and identify issues.
- **Step-by-step account**: For the complex root issue, the debugger revealed that the calculation of the
 discriminant was incorrect.
- **Solutions implemented**: The calculation of the discriminant was corrected, and the solver was
 updated to handle complex roots properly.
- **Issues and Fixes**
    - Issue 1: Incorrect handling of complex roots.
    Root cause: Incorrect calculation of the discriminant.
    Solution: Corrected the calculation of the discriminant and updated the solver to handle
 complex roots.
    Code snippet: `discriminant = b**2 - 4*a*c` (corrected calculation)
     - Issue 2: Repeated roots not handled correctly.
    - Root cause: Insufficient checking for repeated roots.
    - Solution: Added a check for repeated roots and updated the solver to handle them correctly.

## Conclusion

The testing and debugging process revealed the importance of thorough testing and attention to
 detail.The testing and debugging effort ensured the quadratic equation solver's correctness and
 reliability. With the issues resolved, the solver is now confident to produce accurate results.This
 report demonstrates the testing and debugging process for a quadratic equation solver,
 highlighting the importance of thorough testing and attention to detail.

## Recommendations
- Future testing: Additional testing with more complex coefficients and edge cases.
- Potential improvements: Consider adding support for numerical methods or
 approximation technique

