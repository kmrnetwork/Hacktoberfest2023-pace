
# - **Task 3:** Factorial Script in Python
#   - Develop a Python script to calculate factorials.

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

number=int(input("enter a positive number "))
print("factorial of",number, "is",factorial(number))
