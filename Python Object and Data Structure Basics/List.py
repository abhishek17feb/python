#List are ordered sequesnces that can hold a variety of objects
#They use [] brackets and commas to seperate object in the List [1,2,13,25]
#List supports indexing and slicing

#1. Indexing
myList = ['Hello','There','How']
print(myList[1]) #There

#2.Slicing
print(myList[1::]) # ['There', 'How']

#3. Concatination
anotherList = ['Are','You']
newList = myList + anotherList
print(newList) #['Hello', 'There', 'How', 'Are', 'You']

#4. Chaning a value from an index position
newList[3] = 'HOW ALL CAPS'
print(newList) #['Hello', 'There', 'How', 'HOW ALL CAPS', 'You']

##List and String are same in may way, but List are mutable as showed in the above example

#Adding value to a List
myList = [90,556,6]
myList.append(8)
print(myList) #[2, 5, 6, 8]

#Removing value from a list
myList.pop()
print(myList) #[2, 5, 6]

#RFemoving from a index position
print(myList.pop(0)) #2
print(myList) #[5, 6]

#Sorting a List
print(myList.sort()) #None as sort() doesn't return anything
print(myList) #[6, 556]

#Reversing a List
print(myList.reverse()) #None as reverse() doesn't return anything
print(myList) #[556, 6]
