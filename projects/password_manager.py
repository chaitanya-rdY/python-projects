#the main funtion to work with files is open()
#open()->two parameters 1.file name 2.mode
# there are 4 modes:
# 1.read-"r"->opens the file for read only returns error if file not exist
# 2.append-"a"->opens the file and append .file creates if not exist
# 3.write-"W"->overwrites the entire file and added the new imformation .if not exist create the new file
# 4.create-"x"->creates file if it is not exist
# in addition you can handeled it in two modes test and binary mode
#"t" - Text - Default value. Text mode
#"b" - Binary - Binary mode (e.g. images)
# we can directly access the file if python file and accessing file in same directory other wise we have to specify the file location 
#by default it can have read() can get the total imformation instead we can use read(5).it can print first five characters in the file
# by using the readline() we can get the first line only
#after the work with file is completed close the file as file.close()
#by importing os we can track the file path as
#1.os.path.join("director_path","file_name")
#2.if the file existing in the sa, epython working folder we use os.path.abspath("file_name")
#3.from pathlib import path file_path=Path("directory path")/file_name
#by using strip we can delete the spaces 
#by using split(!)it will split the string in to parts at (!) into array[]
#  ex:x="chaitanya | reddy"
#then y=x.split("|")
#y=["chaitanya","reddy"]



