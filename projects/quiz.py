print("hey! welcome to the game ")
x=input("do you want to play? ").lower()
if(x!="yes"):
    quit()
print("lets play!")
score=0
answer=input("what is CPU ?")
if(answer.lower()=="central processing unit"):
    print("correct!")
    score+=1
else:
    print("incorrect!")
answer=input("what is GPU? ")
if(answer=="grapic processing unit"):
    print("correct!")
    score+=1
else:
    print("incorrect!")
answer=input("what is RAM?")
if(answer=="random access memory"):
    print("correct!")
    score+=1
else:
    print("incorrect!")
print("you got",str(score),"out of 3")