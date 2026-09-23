word = "The University of Southern Denmark"

test = word[0:3]
test2 = word[4:14]
test3 = word[14:17]
test4 = word[18:26]
test5 = word[27:34]
##- ['The', 'University', 'of', 'Southern', 'Denmark']
print("'"+test+"',"+test2+"',"+test3+"',"+test4+"','"+test5+"'")

##- The_University_of_Southern_Denmark

print(test+"_"+test2+"_"+test3+"_"+test4+"_"+test5)

#- University (using negative indexing)

Test6 = word[-30:-19]

print(Test6)

#- TeUiest fSuhr emr

test7 = word[0:35:2]

print(test7)

#- kanDneto oyirvn h

test8 = word[-1:-35:-2]

print(test8)

# - The University of Southern Denmark_Kolding

print(test+" "+test2+" "+test3+" "+test4+" "+test5+"_Kolding")