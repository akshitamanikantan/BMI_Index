This Python project analyzes health risks for multiple individuals based on their Body Mass Index (BMI), blood pressure, and heart rate.
The program uses input data from users, calculates BMI, and classifies each health parameter as Low, Medium, or High. Based on the number of high-risk parameters, it determines the overall health risk level of each person.
At the end, it provides a summary report showing how many individuals fall under each health risk category ( Low, Medium, or High).

TECHNOLOGIES USED:
python, conditional statements,loops,string and arithmetic operations.

INPUT FORMAT:
1.Number of individuals (n)
2.For each person:
    i)Weight in kilograms (kg)
    ii)Height in meters (m)
    iii)Blood Pressure in mmHg (Systolic/Diastolic)
    iv)Heart Rate in beats per minute (bpm)
    
FEATURES:

Calculates BMI (Body Mass Index) using the formula:
       BMI = weight / (height²)

Classifies BMI levels as:
    1.Low (Underweight): BMI < 18.5
    2.Medium (Normal Weight): 18.5 ≤ BMI ≤ 24.9
    3.High (Overweight): BMI ≥ 25

Evaluates Blood Pressure (Systolic/Diastolic):
    1.Low: Below 90/60 mmHg
    2.Medium (Normal): Between 90/60 mmHg and 120/80 mmHg
    3.High: Above 120/80 mmHg

Evaluates Heart Rate:
    1.Low: Below 60 bpm
    2.Medium (Normal): Between 60–100 bpm
    3.High: Above 100 bpm

Determines Overall Health Risk Level:
    1.High Risk: Two or more health parameters are high
    2.Medium Risk: Any one parameter is high
    3.Low Risk: None of the parameters are high

Displays a Summary Report at the end:
Shows total individuals in Low, Medium, and High risk categories.

HOW IT WORKS:

Data Collection Phase:
The program asks the user to input the number of individuals and collects data such as weight, height, blood pressure, and heart rate for each person.

Computation Phase:
Calculates BMI for each individual.
Categorizes BMI, blood pressure, and heart rate using conditional checks.

Risk Evaluation Phase:
Evaluates each person’s overall health risk level.
Uses the count of high-risk parameters to determine if a person falls into Low, Medium, or High risk.

Summary Report Phase:
After processing all individuals, the program prints a summary showing how many people are at each risk level.

SAMPLE INPUT:

2  
60  
1.65  
110
70  
75  
85  
1.70  
130
90  
105  

SAMPLE OUTPUT:

Person 1  
BMI: 22.04 kg/m²  
BMI Category: Normal Weight  
Blood Pressure: 110/70 mmHg  
Blood Pressure Level: Medium  
Heart Rate: 75 bpm  
Heart Rate Level: Normal  
Overall Health Risk: Low  

Person 2  
BMI: 29.41 kg/m²  
BMI Category: Overweight  
Blood Pressure: 130/90 mmHg  
Blood Pressure Level: High  
Heart Rate: 105 bpm  
Heart Rate Level: High  
Overall Health Risk: High  

Summary:  
High Risk Level: 1  
Medium Risk Level: 0  
Low Risk Level: 1  
