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
	git merge dev
	git commit -m "step-c committing for version-1 release"
	git tag -a V1.0 -m "release of version-1 step-c"
	git push origin main
	git push origin V1.0	
d) Add any of your classmates as collaborators.

Added Lokesh and Swwapnnashree as a collaborator

e) Implement a feature by creating a new branch called ‘feature/sqrt’.

	git checkout -b feature/sqrt
 	ls
  	nano Calculator.py
   
f) Add the ‘sqrt’ code into it.

** Note: uncomment the square root part of code**

g) While you are working on this feature, imagine that one critical bug is reported in the main branch, and you need to switch back to the ‘dev’ branch, create fixes, and apply them while keeping your ‘feature/sqrt’ branch up-to-date. For this, you need to create
The bug fixation is in the divide function and the new function :

	git checkout dev
Note: replace the division function with the below function to make it handle the division with zero.
def divide(self, a, b): if b == 0: raise ValueError("Cannot divide by zero.") return a / b

h) After completing the feature implementation and ensuring that the application works correctly, create a pull request targeting the main branch.

	git checkout feature/sqrt
	nano Calculator.py
	git add Calculator.py
	git commit -m "step g & H bug is fixed in dev branch"
	git push origin feature/sqrt

i) Request a code review from a team member and make any necessary improvements based on the review feedback.
j) Once the code reviewer approves your pull request, merge the "feature/sqrt" branch into the ‘dev’ branch.

	git checkout dev
	git merge feature/sqrt

k) Finally, do the testing in the ‘dev’ branch itself and merge it into the ‘main’ branch and create a ‘version 2’ release.

![image](https://github.com/AdarshIITDH/git_assignment_HeroVired/assets/60352729/c41aa5c0-9e5d-4e77-8b7e-488a7dc893f8)

	git tag -a V2.0 -m "step-k version2 release"


Q.2: For a project that deals with large binary files, integrate Git LFS (Large File Storage) to handle these files efficiently. Demonstrate how to add, commit, and push binary files to the repository, ensuring they are tracked by Git LFS correctly. Clone the repository on another machine to verify that the binary files are downloaded correctly. In the repository ‘git_assignment_HeroVired’, create a branch ‘lfs’. Upload any large file whose size is over ‘200mb’ and try to push this file into the repository.

	git branch -a lfs
Note: Place the file in the same directory

	git lfs install
	git lfs track filename
	git add filename
	git commit -m "question2- large file"
	git push origin lfs
Note: Replace the file name in above command with your file name
Clone the repository in some other machine or directory and check the file is visible or not?
![image](https://github.com/AdarshIITDH/git_assignment_HeroVired/assets/60352729/23cec2fe-48dc-4d33-95cc-fd5a0fb45026)

Q.3: In this same GitHub repository, create a new branch ‘geometry-calculator’, we'll work on a simple Python program that calculates the area of a circle and the area of a rectangle. We'll use Git stash to switch between working on multiple features (calculating circle area and calculating rectangle area) without committing incomplete changes.

a.Create a New Branch:
	- Create a new branch named "feature/circle-area" to work on the circle-area feature
 
	git checkout -b geometry-calculator
	nano geometry.py
 Note: Paste the below code in the file and save it
```
# import math
# class GeometryCalculator:
    #def calculate_circle_area(self, radius): return math.pi * radius ** 2
    #def calculate_rectangle_area(self, length, width): return length * width
# if  __name__=="main": calculator = GeometryCalculator()

# TODO: Implement the feature to calculate the area of a circle 
# radius = 5
# print(f"The area of the circle with radius {radius} ={calculator.calculate_circle_area(radius)}")

# TODO: Implement the feature to calculate the area of a rectangle 
# length = 10
# width = 6
# print(f"The area of the rectangle with length {length} and width {width} ={calculator.calculate_rectangle_area(length, width)}")
```
b.Stash Changes for Circle Area Feature:
	-  Before committing the changes, stash them using git stash to save the incomplete feature implementation.
	-  Verify that the working directory is clean

	git checkout -b feature/circle-area
 	nano geometry.py
  Note: Uncomment 

















