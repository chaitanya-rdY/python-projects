#armstrong number 
def armstrong_number(x,y):
    for i in range(x,y):
        j=str(i)
        count=len(j)
        sum=0
        while(i>0):
            ld=i%10
            i=i/10
            sum+=pow(ld,count)
        if(sum==i):
            print(i)
x=int(input("start: "))
y=int(input("stop: "))
armstrong_number(x,y)            

    