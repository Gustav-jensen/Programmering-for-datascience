'''99
1. Prompt the user to enter a telephone number.
2. Check if the number:
○ Starts with either "0045" or "+45"
○ Consists only of digits (after removing the initial country code).
○ Has a total length (excluding spaces) of no more than 8 digits after the
country code.
3. If the number is valid, print a success message; if not, print an error message. 
3. If the number is valid, print a success message; if not, print an error message. 
'''
# 1. Prompt the user to enter a telephone number.

num = input("Phone number")

# 1.1 remove blank spaces from telephone number.

num = num.replace(" ","")

#2. Check if the number:

#○ Starts with either "0045" or "+45"

if "+45" in num[0:5:] or "0045" in num[0:5:]:
    print("contains country code")
else:
    print("Doesn't contain country code")

#○ Consists only of digits (after removing the initial country code).

if "+45" in num[0:5:]:
    code = 3
elif "0045" in num[0:5:]:
    code = 4
else: code = 0


if num[code:].isdigit():
    print("Number is only digits")
else:
    print("invalid number")

# Has a total length (excluding spaces) of no more than 8 digits after the
# country code.

if len(num)-code == 8:
    print("8 digits")
else:
    print("invalid amount of digits")