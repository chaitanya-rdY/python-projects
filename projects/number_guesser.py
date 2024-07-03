#in the randrange(10) it will give 0<=n<10 [start,stop)
#in the randint it is not possible it must include [start,stop]
#in the randrange we can include step also [start,stop,step]
import random
answer=input("do you want to play ?")
if(answer.lower()!="yes"):
    quit()
print("lets play!")
stop=int(input("enter the number range: "))
i=random.randrange(stop)
g=0
while True:
    g+=1
    x=input("please enter your guess:")
    if(x.isdigit()!=True):
        print("please enter number")
        continue
    else :
        x=int(x)

    if(x==i):
        print("it's correct")
        
        break

    elif(x>i):
        print("incorrect your input is greater than correct number")
        
    else:
        print("incorrct your input is less than correct number")
        g+=1
print("you guessed the correct number in",g,"guesses")