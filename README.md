# git_assignment_HeroVired
**Question 1**

You are part of a development team working on a Python application called "CalculatorPlus." The application provides basic arithmetic operations, such as addition, subtraction, multiplication, and division. Your task is to implement a new feature that adds support for calculating the square root of a number.

a) Create a repository name: git_assignment_HeroVired
![image](https://github.com/AdarshIITDH/git_assignment_HeroVired/assets/60352729/54d0043b-be8a-4a28-a499-74e6cc2262c8)

b) Create a ‘dev’ branch and add this code.
```
git clone git@github.com:AdarshIITDH/git_assignment_HeroVired.git
cd git_assignment_HeroVired
git checkout -b dev
nano CalculatorPlus.py
```
```
import math 
class Calculator:
	def add(self, a, b): return a + b
	def subtract(self, a, b): return a - b
	def multiply(self, a, b):return a * b
	def divide(self, a, b): 
		if b == 0:raise ValueError("Cannot divide by zero.") 
		return a / b
	def square_root(self, x): return math.sqrt(x)

#TODO: Implement the following function to calculate the square root of a number.
# You need to uncomment the above function and complete its implementation to add the square root feature.
if __name__=="main": calculator = Calculator()
num1 = 16
num2 = 4
# print(f"{num1} + {num2} = {calculator.add(num1, num2)}") 
# print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}") 
# print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}") 
# print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")
# TODO: Uncomment and test the square root feature. 
num3 = 25
# print(f"The square root of {num3} = {calculator.square_root(num3)}")
```
	git add Calculator.py
 	git commit -m "step-b"
  	git push origin dev

c) Merge this branch with the main branch and make a release of version 1 of the ‘calculator plus app’.
git checkout main
git merge
