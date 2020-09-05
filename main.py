# Author: Saeed Alyami ssa5468@psu.edu
grade01 = input ("Enter your course 1 letter grade: ")
cr01 = input ("Enter your course 1 credit: ")
cr01 = float(cr01)
if grade01 == "A":
  grpo1 = 4.0 
  print(f"Grade point for course 1 is: 4.0")
elif grade01 == "A-":
  grpo1 = 3.67
  print(f"Grade point for course 1 is: 3.67")
elif  grade01 == "B+":
  grpo1 = 3.33 
  print(f"Grade point for course 1 is: 3.33")
elif grade01 == "B":
  grpo1 = 3
  print(f"Grade point for course 1 is: 3:0")
elif grade01 == "B-":
  grpo1 = 2.67
  print(f"Grade point for course 1 is: 2.67")
elif grade01 == "C+":
  grpo1 = 2.33
  print(f"Grade point for course 1 is: 2.33")
elif grade01 == "C": 
  grpo1 = 2.0 
  print(f"Grade point for course 1 is: 2.0")
elif grade01 == "D": 
  grpo1 = 1.0 
  print(f"Grade point for course 1 is: 1.0")
else:
  grpo1 = 0.0
  print(f"Grade point for course 1 is: 0.0")

grade02 = input ("Enter your course 2 letter grade: ")
cr02 = input ("Enter your course 2 credit: ")
cr02 = float(cr02)
if grade02 == "A":
  grpo2 = 4.0 
  print(f"Grade point for course 2 is: 4.0")
elif grade02 == "A-":
  grpo2 = 3.67
  print(f"Grade point for course 2 is: 3.67")
elif  grade02 == "B+":
  grpo2 = 3.33 
  print(f"Grade point for course 2 is: 3.33")
elif grade02 == "B":
  grpo2 = 3
  print(f"Grade point for course 2 is: 3:0")
elif grade02 == "B-":
  grpo2 = 2.67
  print(f"Grade point for course 2 is: 2.67")
elif grade02 == "C+":
  grpo2 = 2.33
  print(f"Grade point for course 2 is: 2.33")
elif grade02 == "C": 
  grpo2 = 2.0 
  print(f"Grade point for course 2 is: 2.0")
elif grade02 == "D": 
  grpo2 = 1.0 
  print(f"Grade point for course 2 is: 1.0")
else:
  grpo2 = 0.0
  print(f"Grade point for course 2 is: 0.0")

grade03 = input ("Enter your course 3 letter grade: ")
cr03 = input ("Enter your course 3 credit: ")
cr03 = float(cr03)
if grade03 == "A":
  grpo3 = 4.0 
  print(f"Grade point for course 3 is: 4.0")
elif grade03 == "A-":
  grpo3 = 3.67
  print(f"Grade point for course 3 is: 3.67")
elif  grade03 == "B+":
  grpo3 = 3.33 
  print(f"Grade point for course 3 is: 3.33")
elif grade03 == "B":
  grpo3 = 3
  print(f"Grade point for course 3 is: 3.0")
elif grade03 == "B-":
  grpo3 = 2.67
  print(f"Grade point for course 3 is: 2.67")
elif grade03 == "C+":
  grpo3 = 2.33
  print(f"Grade point for course 3 is: 2.33")
elif grade03 == "C": 
  grpo3 = 2.0 
  print(f"Grade point for course 3 is: 2.0")
elif grade03 == "D": 
  grpo3 = 1.0 
  print(f"Grade point for course 3 is: 1.0")
else:
  grpo3 = 0.0
  print(f"Grade point for course 3 is: 0.0")

GPA =float((grpo1 * cr01 + grpo2 * cr02 + grpo3 * cr03)/(cr01 + cr03 + cr02))

print(f"Your GPA is: {GPA}")