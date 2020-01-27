## List comprehension is a way to extract list from some other data structure

mylist = []

word = 'hello'
for alpha in word:
    mylist.append(alpha)
print(mylist) #['h', 'e', 'l', 'l', 'o']

#The above could be simply done by:-

mylist = [alpha for alpha in 'abhishek']
print(mylist) #['a', 'b', 'h', 'i', 's', 'h', 'e', 'k']

numList = [num**2 for num in range(0,8)]
print(numList) #[0, 1, 4, 9, 16, 25, 36, 49]

onlyodd = [ oddNumber for oddNumber in range(0,7) if oddNumber%2!=0 ]
print(onlyodd) #[1, 3, 5]

#Fareinheight to celcius conversion
celcius = [0,10,20,30]
fahrenheit = [ ( (9/5)*temp +32 ) for temp in celcius ]
print(fahrenheit) #[32.0, 50.0, 68.0, 86.0]