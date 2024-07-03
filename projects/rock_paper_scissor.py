#rock breaks scissor
#paper cover rock
#scissor cuts the paper
import random
options=["rock","paper","scissor"]
computer_score=0
user_score=0
while True:
    user_input=input("please choose rock/paper/scissor/'q'for break:").lower()
    if user_input=='q':
       break
    if user_input not in options:
        continue
    random_number=random.randint(0,2)
    computer_input=options[random_number]
    if(user_input=="rock" and computer_input=="scissor"):
        print("hurry! you are the winner!")
        user_score+=1
    elif(user_input=="scissor" and computer_input=="paper"):
        print("hurry! you are the winner!")
        user_score+=1
    elif(user_input=="paper"and computer_input=="rock"):
        print("hurry! you are the winner!")
        user_score+=1
    elif(user_input==computer_input):
        print("tie")
    else:
        print("sorry! you loose the match")
        computer_score+=1
print("you got the score",user_score,"and computer score is",computer_score)
print("good bye")


