file = open("demo.txt","w")
file.write("text here")#writes at the beginning deleting the previous content
file.close()

file = open("demo.txt","r")
print(file.read())#reads from the begining - read(no of bytes to be read) or readline() to read one line till \n
file.close()

file = open("demo.txt","a")#append mode - writes at the end without deleting the content
file.write("new line")
file.close()