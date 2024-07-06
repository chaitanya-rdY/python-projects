#list comprehension offers a shorter syntax when you want to create a new list based on the values of the existing list
with open("story.txt","r") as f:
    story=f.read()
for i,char enumerate(story):
    print(i,char)