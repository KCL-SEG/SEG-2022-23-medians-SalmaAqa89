"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
numbers.sort()
count = len(numbers)
if count % 2 != 0:
    median = numbers[count//2]
else:
    median = (numbers[count//2]+numbers[(count//2)-1])/2
print("Median:", median)
