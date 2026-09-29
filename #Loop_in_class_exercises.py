#Loop
# In-class exercises 1
'''
x = 30
while x > 0:
    print(x)
    x -= 3 
 # = 3 6 9 12 15 18 21 24 27 30
    '''

# In-class exercises 1: Write a program that calculates the factorial of a number entered by the
# user using a while loop.
# Note: The factorial of a number n is the product of all positive integers from 1
# to n. Factorial(5) = 5*4*3*2*1
'''
x = 1
n = 5
resultat = 1
while x <= n:
    resultat*= x
    x +=1
    print(resultat)
'''

'''1- Write a program that uses a while loop to reverse a string entered by the user.
Enter your string: abcde
The reverse string: edcba '''
'''
txt = input("write text to reverse")

reversed_text = ""
i = len(txt) -1

while i >= 0:
    reversed_text += txt[i]
    i -= 1
    print("The reverse string:", reversed_text)
'''
'''
text = input("Enter your string: ")

vowels = "aeiou"
count = 0
found = ""
i = 0

while i < len(text):
    if text[i].lower() in vowels:
        count += 1

        if found != "":
            found += ", "

        found += text[i]

    i += 1

print(f'There are {count} vowels in "{text}": {found}')
'''

num = input("Enter a number (or non-digit to exit): ")
liste = []
while num.isdigit():
    num= int(num)
    liste.append(num)
    num = input("Enter a number (or non-digit to exit): ")
else:
    if len(liste) > 0:
        print(max(liste))
        print(min(liste))
        print((sum(liste))/(len(liste)))
    else:
        print("list is empty")
    
    

