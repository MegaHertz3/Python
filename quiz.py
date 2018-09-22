#Quiz time
print ("Quiz time !")
print ()
user = input("What is your name? ")
print ("Oh dear, really!")
print ()
print ("Are you ready for the first question", user, "?")
ready = input()
if ready.lower() == "yes":
    print("Excellent, lets begin!")
elif ready.lower() == "y":
    print("Excellent, lets begin!") 
else:
    print("Bugger off then!")

score = 0

#first question
print (user, ", question 1")
a1 =  input("What is the capital of England?\n")
if a1.lower() == "london":
    print ("Correct") 
    score = score + 1
    print ("Nice one son!")
else:
    print ("Jesus! dont you know that one!\n")

print()
print ("let's move on\n")
a=input("hit a key to continue")
print ()
#second question
print ("OK, second question", user)
print()
a2 = input("Who shot Roger Rabbit?\nA:Baby Herman\nB:Jessica Rabbit\nC:Toon Patrol\n")
if a2.lower() == "b":
    print ("correct", user)
    score = score + 1
else:
    print ("Incorrect buddy")
print ()
print (score)
 
