def add():
    account=input("enter username/gmail:")
    password=input("enter password:")
    with open("passwords.txt","a") as file:
        file.write(account+" | "+password+"\n")
def view():
    with open("passwords.txt","r") as file:
        for line in file.readlines():
            line=line.strip()
            user,passw=line.split("|")
            print("account:",user+"\n""password:",passw)
           

while True:
    user_input=input("Do you want to add new passwords,to view the current passwords ,quit(add/view/q)? ").lower()
    if(user_input=="q"):
        break
    elif(user_input=="add"):
        add()
    elif(user_input=="view"):
        view()
    else:
        print("choose correct option")
        continue

print("ok!bye")