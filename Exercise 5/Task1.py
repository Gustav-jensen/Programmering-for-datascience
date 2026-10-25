n = int(input("wrtie an integer"))
print("the integer number is: ",n)
if int(n) > 0:
    i = 0
    while int(n) >= 0:
        print(n)
        n -= 1
elif int(n) <= 0:
    i = 0
    while int(n) < 0:
        n += 1
        print(n)
    print("the integer is negetative")
else:
    print("you entered 0")