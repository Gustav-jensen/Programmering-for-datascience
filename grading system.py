##Write a Python program that takes a numerical grade as input(0 to 100), and prints
#the corresponding letter grade based on the following scale:

#write grade:
x1 = input("Write Grade: ")

#-A for grades 90 to 100

if 100 > int(x1) and int(x1) > 90:
    print("A")

#-B for grades 80 to 89

elif 89 > int(x1) and int(x1) > 80:
    print("B")

#--C for grades 70 to 79

elif 79 > int(x1) and int(x1) > 70:
    print("C")

#--M for grades 60 to 69

elif 69 > int(x1) and int(x1) > 60:
    print("M")

#--F for the other grades

elif int(x1) > 60:
    print("F")
    