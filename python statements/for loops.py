mynumberlist = [12, 43, 3434, 132, 767, 7879]

for number in mynumberlist:
    if number % 2 == 0:
        print(f'Even number is {number}')
    else:
        print(f'Odd number is {number}');
# Even number is 12
# Odd number is 43
# Even number is 3434
# Even number is 132
# Odd number is 767
# Odd number is 7879
sumOfNumbers = 0;
for number in mynumberlist:
    sumOfNumbers = sumOfNumbers + number

print(f'Sum of all numbers in the list is {sumOfNumbers}')  # Sum of all numbers in the list is 12267

##Iterating through a Tuple

tuple = (12, 45, 76)
for item in tuple:
    print(item)
# 12
# 45
# 76

## Tuples inside list iteration example
tupleList = [(2,4),('Abhishek','Sumi'),('June',18)]
for tupLi in  tupleList:
    print(tupLi)

#Tuple unpacking

for key,value in tupleList:
    print(f'Key is {key} and value is {value}');

#3Iterating through dictionary
dictionary = {'apple':20,'pineapple':50,'oranges':67}

for items in dictionary:
    print(items);
#apple
#pineapple
#oranges
#By default for loop over dictionary will return only keys

dictionary = {'apple':20,'pineapple':50,'oranges':67}

for items in dictionary.items():
    print(items);

#('apple', 20)
#('pineapple', 50)
#('oranges', 67)
#Again we could use tuple unpacking to iterate over doctionaries

for key,value in dictionary.items():
    print(f'Key is {key} and value is {value}');
#Key is apple and value is 20
#Key is pineapple and value is 50
#Key is oranges and value is 67
