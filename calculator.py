'''
1. Write a Python script calculator.py, for a basic calculator that performs arithmetic
operations on two numbers based on user input. The calculator should operate as
follows:
- ask the user to enter the first number
- ask the user to enter the operation (+, -, *,/)
- ask the user to enter the second number
- depending on the operation, print out the result “The answer = ”
- print a message in case the user decides on the division, and having
0 as the second number “You divided by zero!!!”
- print a message in case the user enters any other operation:
"Error... Invalid Operation!! :( "
'''


# Input numbers and operator
try:
    num1 = int(input("Input first number: "))
    op = input("Input operator: ")
    num2 = int(input("Input second number: "))

except ValueError:
    print("Error... Invalid Operation!! :( ")

else:
    # Check for invalid operators
    if op not in ("+", "-", "*", "/"):
        print("Wrong use of operator")

    # Check for division by zero
    elif op == "/" and num2 == 0:
        print("You divided by zero")

    # Print the result
    else:
        print("The answer to", num1, op, num2, "is:")

        if op == "+":
            print(num1 + num2)
        elif op == "/":
            print(num1 / num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "*":
            print(num1 * num2)