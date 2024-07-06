#list comprehension offers a shorter syntax when you want to create a new list based on the values of the existing list
fruits=["apple","mango","banana"]
y=[x if x!="banana" else "orange" for x in fruits]
for i in y:
    print(i)