done = False
while not done:
    number = int(input("What numbers times table would you like? > "))
    upto = int(input('what number would you like it to go up to? > '))
    upto += 1
    for i in range(1,upto):
        answer = i*number
        print(i,"x",number,"=",answer)
    again = input('would you like to enter another number? (Y/N) > ')
    if again == 'N' or again == 'n':
        done = True
