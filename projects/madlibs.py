#enumerate is a built in function in python.it returns the both index,value at index from the iterable.it is often used in for loop to get the index and value at the index
#it is a gime in which we take some <words> like this with some hint from story.txt file and ask the user to give the input and after replacing all words we will replace all the words and print it
with open("story.txt","r") as file:
    story=file.read()
start_of_word="<"
end_of_word=">"
words=set()
for i,char in enumerate(story):
    if(char=="<"):
        start=i
    elif(char==">"):
        if(story[i-1].isalpha() or story[i-1]!="<"):
            word=story[start:i+1]
            words.add(word)
print(words)
answers={}
print("please enter the inputs according to given hints")
for word in words:
    answer=input(word+":")
    answers[word]=answer
for word in words:
    story=story.replace(word,answers[word])
print(story)