def divide(a,b):
    result = a/b
    return result

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("The result of division is: ", divide(num1, num2))
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")