#the main funtion to work with files is open()
#open()->two parameters 1.file name 2.mode
# there are 4 modes:
# 1.read-"r"->opens the file for read only returns error if file not exist
# 2.append-"a"->opens the file and append .file creates if not exist
# 3.write-"W"->writes in the file .if not exist create the new file
# 4.create-"x"->creates file if it is not exist
# in addition you can handeled it in two modes test and binary mode
#"t" - Text - Default value. Text mode
#"b" - Binary - Binary mode (e.g. images)
# we can directly access the file if python file and accessing file in same directory other wise we have to specify the file location 
f=open("demo.txt","rt")
print(f.read())
