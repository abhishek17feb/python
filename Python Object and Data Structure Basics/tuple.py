##Tuples are similar to list with a difference of immutability. That means once a tuple is made, the objects at
## any index position cannot be changed. Again tuples can hold mixure of data types

# E.g myTuple = ('abhishek',450)
tuple = ('abhishek',345,678)
print(tuple[0]) #abhishek
print(tuple[-1]) #678

##Tuples have 2 methods i.e count and index
countChars = ('a','f','a')
print(countChars.count('a'))#2

print(countChars.index('a')) #0 The first index location of occurance

## Showing how list are different from a tuple
myList = [1,2,3]
myList[2] = 8 #Item reassignment is possible with list
print(myList)

countChars[1] = 4 #    countChars[1] = 4
#TypeError: 'tuple' object does not support item assignment
print(countChars)

##So tuples are used when data integrity is required as you cannot re-assign something in tuple accidently

