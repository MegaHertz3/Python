#Euro Lottery number generator

import random

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

FirstNumber = str(FirstNumber)
SecondNumber = str(SecondNumber)
ThirdNumber = str(ThirdNumber)
FourthNumber = str(FourthNumber)
FifthNumber = str(FifthNumber)
print ('This weeks numbers will be:\n' + FirstNumber + '\n' + SecondNumber + '\n' + ThirdNumber + '\n' + FourthNumber + '\n' + FifthNumber + '\n')

StarNumberA = random.randint(1, 11)
StarNumberB = random.randint(1, 11)
if StarNumberB == StarNumberA:
    StarNumberB = random.randint(1, 11)

StarNumberA = str(StarNumberA)
StarNumberB = str(StarNumberB)


print ('and the two star numbers:\n' + StarNumberA + '\n' + StarNumberB + '\n')
		
a=input('Press Return to close')

