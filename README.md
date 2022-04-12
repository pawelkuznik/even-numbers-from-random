# even-numbers-from-random
a computer program that returns even numbers from random and unit tests

Task:
1. Prepare a class that will contain a method returning even numbers from the randomly selected numbers.

2. Prepare a test class to test the above method.
The test class is designed to check the following situations:
- the returned file will be empty
- only even numbers will be returned
- only odd numbers will be returned
- both even and odd numbers are returned 
all assertion check if method return only even numbers list

All test were run with range(0-1000) and returned 10 element list (to easy debug etc.)
#### To run:
##### the use of a virtual environment is recommended (virtualvenv etc.)
1. install latest pip package
2. invoke in cmd: pip install -r requierements.txt
3. run pytest by `python -m pytest` inside project directory
4. If You want You have html report, you should invoke pytest --html=report.html --self-contained-html
