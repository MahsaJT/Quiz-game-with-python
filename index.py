print("Do you wanna play? ")
answer = input("")
if answer.lower()=="yes":
    print("lets Go!")
else :
    print("another time")
    quit()
    
score = 0

print("where is the Iran capacity? ")
answer1 = input("").lower()
if answer1 == "tehran":
    print ("YEAH! CORRECT :) ")
    score += 1
else :
    print("AWCH, WRONG ANSWER!!")


print("how many continents are in the world ? ")
answer1 = input("").lower()
if answer1 == "six":
    print ("YEAH! CORRECT :) ")
    score += 1
else :
    print("AWCH, WRONG ANSWER!!")


print("what is the most important thing to live? ")
answer1 = input("").lower()
if answer1 == "air":
    print ("YEAH! CORRECT :) ")
    score += 1
else :
    print("AWCH, WRONG ANSWER!!")


print("how many fingers are in one hand? ")
answer1 = input("").lower()
if answer1 == "five":
    print ("YEAH! CORRECT :) ")
    score += 1
else :
    print("AWCH, WRONG ANSWER!!")

    
print("your score is : " + str(score) )
