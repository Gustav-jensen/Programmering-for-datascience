# -Write a program that reads an integer x from the user. Then your program should
# display a message indicating whether the integer is even or odd.

x = input("Write variable: ")

if int(x) % 2 == 0:
    print("even")
else:
    print("odd")