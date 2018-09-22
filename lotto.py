#lotto number predictor

import random

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
print ('this weeks numbers wil be:\n' + FirstNumber + '\n' + SecondNumber + '\n' + ThirdNumber + '\n' + FourthNumber + '\n' + FifthNumber + '\n' + SixthNumber + '\n')

a=input('press Return to close')










