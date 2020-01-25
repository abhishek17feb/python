##File I/O
myfile = open('io.txt')
print(myfile.read()) ##This will print out everything in the file

print(myfile.read()) #This won't print anything as the cursor is at the last point, So use seek(0) method

myfile.seek(0)
print(myfile.read()) ##This will print out everything in the file

##In practice we should close the file like:-
myfile.close()

#The following will spare you with not worrying about closing the file
with open('io.txt') as myio:
    contents = myio.read()
print(contents) #Will print everything

# Modes in file operation
# 1. r - only for read
# 2. w - only for writing
# 3. a - for appending to the existing file
# 4. r+ - used to read and write
# 5. w+ - used to write and read, this will override or create new file

with open('ty.txt',mode='w+') as writeFile:
    writeFile.write('something different')
    contents = writeFile.read()
print(writeFile)
