#pythonlab

 
Group_13 
Group Report on Quadratic Equation Solver 
 
Group Members:   
Lohedami MOGBOLU [ENG2403540],  
ORITSEGBUGBEMI Oritsesholaja Ephraim [ENG2403565],  
GODFREY-ARIAVE Jason [ENG2403523],  
UMOH Mmekobong Ime [ENG2403576],  
AGINDOTAN Boyowa Solomon [ENG2410267],  
OKPISA Ilamosi Theresa [ENG2403557],  
OHAHMEN Superior Afudah [ENG2403553] 
 
Date: Sept. 2025 
 
Course: CPE112 
 
Lecturer: Dr. E. Olaye 
 
INTRODUCTION 
This report documents the team work in writing, implementing, debugging and testing of a 
Python program to find the roots of the quadratic equation 𝑎𝑥2 + 𝑏𝑥 + 𝑐 = 0 using x=-bb2-4ac2a
The program, developed by Group_13 handles two cases: two normal roots and complex roots. The work was completed using Visual Studio Code, tested with Pytest and using draw.io, the flowchart was designed. After which it was documented using MS Word. 

 ORITSEGBUGBEMI Oritsesholaja Ephraim implemented the Python code and also tested the program using the Pytest framework alongside UMOH Mmekobong Ime. 

 Lohedami MOGBOLU documented the process. 

 GODFREY-ARIAVE Jason designed the flowchart.
 
FLOWCHART DEVELOPMENT 
The flowchart was designed to outline the procedure used in solving the quadratic equation. 
GODFREY-ARIAVE Jason led this task, using the online flowchart tool draw.io: 
● Step 1- Start: The program begins here. 
Step 2 - Input: The user is asked to input their values for each unknown. 

Step 3 - The discriminant 𝑑 =b² − 4𝑎𝑐 is calculated. And, based on d the roots are calculated: 
 If d >= 0: compute x1, x2 and output otherwise output complex roots. 
Step 4 - End: The program ends here. 


IMPLEMENTATION 

The program was implemented by ORITSEGBUGBEMI Oritsesholaja Ephraim  using VS Code ● Code structure: 
A quadratic_solver() function computers and displays roots based on the
discriminant. 
A get_positive_float_input() function ensures the user does not input any number less than 1. 
A get_float_input() function validates numeric input with an while loop and try-except. 

 The file was saved as quadratic_solver.py and tested. 

TESTING
The program was tested by ORITSEGBUGBEMI Oritsesholaja Ephraim and UMOH Mmekobong Ime using the Pytest framework. This was done in two stages: 

Stage 1: The Manual Testing Stage 
Test case 1: a = 1; b = 3; c = 1. Two real roots were found: -0.3819 and -2.6180. 
Tested by Lohedami MOGBOLU. 
Test Case 2: a =2; b =4; c = 4. Two complex roots were found: -1 + 4i and -1 – 4i. 
Tested by Lohedami MOGBOLU  

Stage 2: The Automated Testing Stage.
ORITSEGBUGBEMI Oritsesholaja Ephraim created test_quadratic_solver.py All tests passed as reviewed by the group. 
 
CONCLUSION 
The quadratic equation solver was successfully created. Lohedami MOGBOLU after executing the code observed there was no if statement should a user decide to input zero as the coefficient of x^2. She suggested that to ORITSEGBUGBEMI Oritsesholaja Ephraim. UMOH Mmekobong Ime tested the initial file program but when Lohedami MOGBOLU suggested an edit, ORITSEGBUBEMI Oritsesholaja Ephraim stepped up to write the final test file.
 
