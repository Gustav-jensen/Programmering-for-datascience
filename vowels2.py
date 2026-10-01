
'''
Write a program vowels.py that reads in a string from the user. If the string contains
at least one of every vowel (a, e, i, o, u), print “You have all the vowels!”. Also, print
the number of vowels contained in the string and print the first appearance of each
vowel in the string.
'''

text = input("Enter your string: ")

vowels = "aeiou"
count = 0
found = ""
found_vowels = set() 
i = 0
'''
while i < len(text):
    if text[i].lower() in vowels:
        count += 1

        if found != "":
            found += ", "

        found += text[i]

        i += 1
        '''
for vowel in text.lower():
    if vowel in vowels:
        found_vowels.add(vowel)
        count += 1

if len(found_vowels) == 5:
    print("You have all the vowels!")
    print(f'There are {count} vowels in "{text}": {found}')
else:
    print("You are missing some vowels.")
    print(f'There are {count} vowels in "{text}": {found}')
