import random
myList = []
go = True
kg = True

while go == True:
    usrInput = input('Tell me something to add to the list fam\nsay \'done\' when u done ite?\n')
    if usrInput == 'done':
        go = False
    else:
        myList.append(usrInput)

while kg == True:
    usrInput = input('press enter to get a random from list\nsay \'done\' when u done ite?\n')
    if usrInput == 'done':
        kg = False
    else:
        print('\n%s\n' %(random.choice(myList)))
