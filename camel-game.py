#Camel game

import random

print("Welcome to Horse!")
print("You have stolen a horse to make your way across the great Thamesmead desert.")
print("The pikies want their horse back and are chasing you down! Survive your")
print("desert trek and out run the pikies")
print()


miles = 0
thirst = 0
horse_tiredness = 0
pikies_miles = -20
pikies_distance = 0

beers = 3

done = False
while not done:
    print("A. Drink some beer")
    print("B. Ahead moderate speed")
    print("C. Ahead full speed")
    print("D. Stop for the night")
    print("E. Status check")
    print("Q. Quit")
    print()
    print("Please select an option")
    user_select = input()

    
    if user_select.upper() == "Q":
        print("Goodbye")
        done = True;
        
    if not done and thirst > 4 and thirst < 6:
        print("You are thirsty")
        print()
    
    if not done and thirst > 5:
        print("You died of thirst!")
        print()
        done = True;  
        
    if not done and pikies_distance < 15:
        print("The pikies are getting close!")
        print()        
        
    if not done and horse_tiredness > 4 and horse_tiredness < 9:
        print("Your horse is getting tired!")
        print()        
        
    if not done and horse_tiredness > 8:
        print("Your horse is dead!!")
        print()
        done = True; 
        
    if not done and pikies_distance < 0:
        print("The pikies got ya! You are dead!")
        print()
        done = True;
        
    if not done and miles > 199:
        print("Well done, you got across the Thamesmead desert\nbefore the pikies got to you")
        print()
        done = True    
        
    elif user_select.upper() == "E":
        print("Miles traveled: ", miles, "\nBeers left: ", beers)
        print("The pikies are ", pikies_distance, " miles behind you")
        print("thirst", thirst)
        print("horse", horse_tiredness)
        print()
        print("You have travelled ", miles, " miles")
        print(pikies_miles)
        print("Pikies are", pikies_distance, "miles behind")
        print("thirst", thirst)
        print("horse", horse_tiredness)
        print()        
        
    elif user_select.upper() == "D":
        print("The horse is happy")
        horse_tiredness = 0
        pikies_miles += random.randrange(7, 15) 
        pikies_distance = miles - (pikies_miles)
        print(pikies_miles)
        print("You have travelled ", miles, " miles")
        print(pikies_miles)
        print(pikies_distance)
        print("thirst", thirst)
        print("horse", horse_tiredness)
        print()
        
    elif user_select.upper() == "C":
        miles = miles + random.randrange(10, 21)
        thirst += 1
        horse_tiredness = horse_tiredness + random.randrange(1, 4)
        pikies_miles = pikies_miles + random.randrange(7, 15)
        pikies_distance =  miles - (pikies_miles)
        print("You have travelled ", miles, " miles")
        print(pikies_miles)
        print(pikies_distance)
        print("thirst", thirst)
        print("horse", horse_tiredness)
        print()
        
    elif user_select.upper() == "B":
        miles = miles + random.randrange(5, 13)
        thirst += 1
        horse_tiredness += 1
        pikies_miles += random.randrange(7, 15) 
        pikies_distance = miles - (pikies_miles)
        print("You have travelled ", miles)
        print(pikies_miles)
        print()
        print("You have travelled ", miles, " miles")
        print(pikies_miles)
        print(pikies_distance)
        print("thirst", thirst)
        print("horse", horse_tiredness)
        print()        
               
    elif user_select.upper() == "A":
        if beers > 0:
            beers -= 1
            thirst = 0
            print("You have", beers, "beers left")
            print()
        else:
            print("You have no beer!")
            print()
            

    