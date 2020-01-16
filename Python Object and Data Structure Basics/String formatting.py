# Injecting a varible into a String is called Interpolation. It is very different from String Concatination

#1. .format() method
#2. f-strings Formated String literals


#1. .format() method
#Syntax - 'My String goes {}'.format('HERE') -> So 'HERE' will be inserted in the placeholder {}. Multiple
#placeholders could also be used.

myName = 'Abhishek {}'
myFullName = myName.format('Roy')
print(myFullName) #Abhishek Roy

multiplePlaceholders = 'We want {} and {} to live a good life'
placeholderInsertedStr = multiplePlaceholders.format('Money','Honey')
print(placeholderInsertedStr) #We want Money and Honey to live a good life

# The placeholder holder could be give indexes and alias of the inserted String
myIndexPlaceholder = 'We could use {1}, to insert the {0}'
indexInserted = myIndexPlaceholder.format('STRING','INDEX')
print(indexInserted)

aliasPlaceholder = 'My little {dog} and {cat} are very naughty'
aliasInserted = aliasPlaceholder.format(dog = 'DOG',cat = 'CAT')
print(aliasInserted)

## Formatting a floating point
##Syntax -> {value:width.precisionf} -> Here width is the number of white spaces before the number gets inserted
## precision is the number of places after the decimal point

myFloatingNumber = 200.5689
print('My floating number {floating:1.2f}'.format(floating = myFloatingNumber)) #My floating number 200.57
print('My floating number {floating:1.1f}'.format(floating = myFloatingNumber)) #My floating number 200.6

#2. f-strings Formated String literals
#Syntax is name = 'ABHISHEK'  ->  f"Here is my String {name}" : Here is my String ABHISHEK
name = 'ABHISHEK'
fString = f"My name is {name}"
print(fString) #My name is ABHISHEK

#So instead of name.format(<text>) we could use place a 'f' before


