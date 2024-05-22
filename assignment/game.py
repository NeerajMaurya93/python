#guess the number
import random
target=random.randint(1,100)
while True:
    userNumber=input(" Guess the target or exit for tape(Q) :")
    if(userNumber=="q"):
        break
    userNumber=int(userNumber)
    if(userNumber==target):
        print("Success : Correct Guess  :")
        break
    elif(userNumber<target):
        print("your number was to small.take a begger guess  :")
    else:
        print("your number was to beg . take a smaller guess..:")
print("_____GAME OVER_______")