import random

def roll():
    min_value=1
    max_value=6
    roll=random.randrange(min_value,max_value)
    return roll

while True:
    players=input("enter the number of players btw(2-4): ")
    if(players.isdigit()==True):
        players=int(players)
        if(2<=players<=4):
            break
        else:
            print("please enter valid number btw(2 to 4)")
            continue

    else:
        print("invaild , try again")
        continue
max_score=50
#List comprehension offers a shorter syntax when you want to create a new list based on the values of the existing list
#newlist=[expression for item in iterable if condition]
#expression:it is the value or tranformation applied to each item iterable that meets a specifies condition
#item:it is each individual element from the iterable
#condition:transformation or expression appplicable if this condition is satisfied

player_scores=[0 for i in range(players)]
while(max(player_scores)<max_score):
    for i in range(players):
        print("player",i+1,"turn begins")
        print("player",i+1,"score is",player_scores[i])
        current_score=0
        while True:
            j=input("do u want to roll dice?")
            if(j.lower()!="y"):
                break
            value=roll()
            if(value==1):
                print("score is 1,ur turn is over")
                current_score=0
                break
            else:
                current_score+=value
                print("you got",value)
        player_scores[i]+=current_score
        print("total score of player",i+1,"is",player_scores[i])   
print("player",player_scores.index(max(player_scores))+1,"wins the match","with",max(player_scores))


