# -Write a program to ask the user to enter three numbers, and find the
# largest number among the three input numbers.

x1 = input("Write variable 1: ")
x2 = input("Write variable 2: ")
x3 = input("Write variable 3: ")

if x1 > x2 and x1 > x3:
    print(x1)
elif x2 > x1 and x2 > x3:
    print(x2)
elif x3 > x1 and x3 > x2:
    print(x3)