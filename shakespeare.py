import re
text= '''William Shakespeare was a renowned English poet,playwright,and
actor born in 1564 in Stratford-upon-Avon. His birthday is most commonly
celebrated on 23 April,which is also believed to be the date he died in
1616. Shakespeare was a prolific writer during the Elizabethan and Jacobean
ages of British theater (sometimes called the English Renaissance or the
Early Modern Period).
Shakespeare’s plays are perhaps his most enduring legacy, but they are not
all he wrote.Shakespeare’s poems also remain popular to this day.'''


print(len(text))
Shakespeare = text.count("Shakespeare")

print("Number of mentions of Shakespeare: ",Shakespeare)

theater = text.count("theater")

print("Number of mentions of theater: " , theater)

# First occurance of the word Shakespeare

print(text.find("Shakespeare"))

print(text.rfind("Shakespeare"))