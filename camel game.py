import random
print('Welcome to Camel!')
print('You have stolen a camel to make your way across the great Mobi desert.')
print('The natives want their camel back and are chasing you down! Survive your')
print('desert trek and out run the natives.')
done = False
traveled = 0
thirst = 0
tiredness = 0
Ndistance = 30
drinks = 3
while not done:
    print('A. Drink from your canteen.\nB. Ahead moderate speed.\nC. Ahead full speed.\nD. Stop for the night.\nE. Status check.\nQ. Quit.')
    choice = input('Your choice? > ')
    oasis = random.randrange(1,21)
    if choice == 'Q' or choice == 'q':
        done = True
    elif choice == 'E' or choice == 'e':
        print('Miles traveled:', traveled)
        print('Drinks in canteen:', drinks)
        print('The natives are', Ndistance,'miles behind you')
    elif choice == 'd' or choice == 'D':
        tiredness = 0
        print('The camel is happy!')
        Ndistance -= random.randrange(3,11)
    elif choice == 'C' or choice == 'c':
        traveled += random.randrange(10,21)
        print('You have traveled',traveled,'miles')
        thirst += 1
        tiredness += random.randrange(1,4)
        Ndistance -= random.randrange(3,11)
    elif choice == 'B' or choice == 'b':
        traveled += random.randrange(5,13)
        print('You have traveled',traveled,'miles')
        thirst += 1
        tiredness += 1
        Ndistance -= random.randrange(3,11)
    elif choice == 'A' or choice == 'a':
        if drinks > 0:
            drinks -= 1
            thirst = 0
        else:
            print('You are out of drinks!')
    if thirst > 4 and thirst < 7:
        print('You are thirsty')
    elif thirst > 6:
        print('You died of thirst!')
        done = True
    if tiredness > 5 and tiredness < 9:
        print('Your camel is getting tired')
    elif tiredness > 8:
        print('Your camel is dead!')
        done = True
    if Ndistance < 1:
        print('The natives caught up!')
        done = True
    elif Ndistance > 0 and Ndistance < 15:
        print('The natives are getting close!')
    if traveled > 199:
        print('You crossed the dessert. You win!')
        done = True
    elif oasis == 1:
        print('You found an oasis!\nYou fill up your bottle and have a drink!')
        drink = 3
        thirst = 0
