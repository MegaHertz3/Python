go = input("Do you want to play the guessing game? y or n > ")
while go == "y":

    TargetNumber = int(input("Tell me a number between 1 and 10 > "))
    
    guess = int(input("Guess a number between 1 and 10. > "))

    while guess < TargetNumber and guess < 10:
        print("Higher")
        guess = int(input("Guess between 1 and 10. > "))

    while guess > TargetNumber and guess < 10:
        print("Lower")
        guess = int(input("Guess between 1 and 10. > "))

    if guess > 10:
        print("A number between 1 and 10!")
        guess = int(input("Guess between 1 and 10. > "))
    
    elif guess == TargetNumber:
        print("Congratulations - thats right!")

    else:
        guess = int(input("Guess between 1 and 10. > "))

    go = input("Do you want to go again? y or n > ")
