#armstrong number 
def armstrong_number(x,y):
    for i in range(x,y+1):
        j=str(i)
        count=len(j)
        sum=0
        a=i
        # print(count)
        while(a>0):
            ld=a%10
            a=a//10
            sum=sum+pow(ld,count)
        if(sum==int(j)):
            print(i)
x=int(input("start: "))
y=int(input("stop: "))
armstrong_number(x,y)            

    