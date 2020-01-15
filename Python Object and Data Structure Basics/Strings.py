## Slicing of a string helps to grab a sub section of the string
## Syntax - [start:stop:step]

name = 'abhishek'
print(len(name))

##Example of indexing in Strings
alphabetH = name[2]
print(alphabetH)

##Example of Slicing in Strings
myString = 'delhi'
# Slice starting from 'e' and take everything after that
print(myString[1:])

#Slice till 'h' and take everything before that
print(myString[:4])

#Exmaple of Step in slicing
#Take out characters at even places i.e 'eh'
print(myString[1::2])

#Reversing a String
print(myString[::-1])
