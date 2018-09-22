#Euro Lottery number generator

import random

print ('1)Euro or 2)Lotto?')
Select = input()
Select = int(Select)

if Select==1:
    print ('EuroLottery Number Predictor\n')
    FirstNumber = random.randint(1, 50)

    SecondNumber = random.randint(1, 50) 
    if SecondNumber == FirstNumber:
        SecondNumber = random.randint(1, 50)
    
    ThirdNumber = random.randint(1, 50)
    if ThirdNumber == FirstNumber:
        ThirdNumber = random.randint(1, 50)
    
    if ThirdNumber == SecondNumber:
        ThirdNumber = random.randint(1, 50)

    FourthNumber = random.randint(1, 50)
    if FourthNumber == FirstNumber:
        FourthNumber = random.randint(1, 50)

    if FourthNumber == SecondNumber:
        FourthNumber = random.randint(1, 50)

    if FourthNumber == ThirdNumber:
        FourthNumber = random.randint(1, 50)

    FifthNumber = random.randint(1, 50)
    if FifthNumber == FirstNumber:
        FifthNumber = random.randint(1, 50)

    if FifthNumber == SecondNumber:
        FifthNumber = random.randint(1, 50)

    if FifthNumber == ThirdNumber:
        FifthNumber = random.randint(1, 50)

    if FifthNumber == FourthNumber:
        FifthNumber = random.randint(1, 50)

    
    print ('This weeks numbers will be:\n' + str(FirstNumber) + '\n' + str(SecondNumber) + '\n' + str(ThirdNumber) + '\n' + str(FourthNumber) + '\n' + str(FifthNumber) + '\n')

    StarNumberA = random.randint(1, 11)
    StarNumberB = random.randint(1, 11)
    if StarNumberB == StarNumberA:
        StarNumberB = random.randint(1, 11)

    StarNumberA = str(StarNumberA)
    StarNumberB = str(StarNumberB)


    print ('and the two star numbers:\n' + StarNumberA + '\n' + StarNumberB + '\n')
		
    a=input('Press Return to close')

if Select==2:
    print ('lotto number predictor\n')

FirstNumber = random.randint(1, 49)

SecondNumber = random.randint(1, 49)
if SecondNumber == FirstNumber:
    SecondNumber = random.randint(1, 49)

ThirdNumber = random.randint(1, 49)
if ThirdNumber == FirstNumber:
    ThirdNumber = random.randint(1, 49)

if ThirdNumber == SecondNumber:
    ThirdNumber = random.randint(1, 49)

FourthNumber = random.randint(1, 49)
if FourthNumber == FirstNumber:
    FourthNumber = random.randint(1, 49)

if FourthNumber == SecondNumber:
    FourthNumber = random.randint(1, 49)

if FourthNumber == ThirdNumber:
    FourthNumber = random.randint(1, 49)

FifthNumber = random.randint(1, 49)
if FifthNumber == FirstNumber:
    FifthNumber = random.randint(1, 49)

if FifthNumber == SecondNumber:
    FifthNumber = random.randint(1, 49)

if FifthNumber == ThirdNumber:
    FifthNumber = random.randint(1, 49)

if FifthNumber == FourthNumber:
    FifthNumber = random.randint(1, 49)

SixthNumber = random.randint(1, 49)
if SixthNumber  == FirstNumber:
    SixthNumber = random.randint(1, 49)

if SixthNumber == SecondNumber:
    SixthNumber = random.randint(1, 49)

if SixthNumber == ThirdNumber:
    SixthNumber = random.randint(1, 49)

if SixthNumber == FourthNumber:
    SixthNumber = random.randint(1, 49)

if SixthNumber == FifthNumber:
    SixthNumber = random.randint(1, 49)

FirstNumber = str(FirstNumber)
SecondNumber = str(SecondNumber)
ThirdNumber = str(ThirdNumber)
FourthNumber = str(FourthNumber)
FifthNumber = str(FifthNumber)
SixthNumber = str(SixthNumber)
print ('this weeks numbers wil be:\n' + FirstNumber + '\n' + SecondNumber+ '\n' +
ThirdNumber + '\n' + FourthNumber + '\n' + FifthNumber + '\n' + SixthNumber + '\n')

a=input('press Return to close')
