#number guess game


import random

number = random.randrange(1, 101)
guess = 1


print("Hello, Im thinking of a number between 1 and 100, can you guess that number?")
print()
done = False
while not done:
    answer = int(input("Guess what number I am thinking of: "))
    if answer == number:
                 print("Well done!")
                 if guess < 2:
                     print("you guessed first time!")
                     done = True
                 elif guess >1:
                     print("you made it in", guess, "guesses")
                     done = True                     
                 
                 
    elif answer < number:
        print("Too low")
        guess += 1
        print()
        print("--- Guess #", guess)     
                 
    elif answer > number:
        print ("Too high")
        guess += 1
        print()
        print("--- Guess #", guess)    
        
print()
a = input("hit any key to close")


