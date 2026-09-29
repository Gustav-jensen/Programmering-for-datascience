'''
Write a Python program converter.py that prompts the user to enter an integer number
and a unit to convert it to meters:
The program should operate as follows:
- ask the user to enter a number
- ask the user to enter the unit (‘inch’ or ‘in’ …)
- depending on the unit, print out the result in meters
- print a message in case the user enters any other unit
"Error... Invalid Unit!! :
'''
unit = (input("input your unit")).lower
num = input("input your integer for conversion")
if num.isdigit() == True:
    if unit in ("Inch","in"):
        print(int(num)*0.0254)
    elif unit in ("hand","h"):
        print(int(num)*0.1016)
    elif unit in ("foot","ft"):
        print(int(num)*0.3048)
    elif unit in ("yard","yd"):
        print(int(num)*0.9144)
    else: print("Error... Invalid Unit!! :( ")
else: print("Error... Invalid Unit!! :( ")
