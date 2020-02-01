class Animal():

    def __init__(self):
        print('Animal Created')
    def what_you_eat(self):
        print('I eat anything')
    def say_something(self):
        print('I can\'t')

class Dog(Animal):

    def __init__(self):
        print('Dog created')
    def what_you_eat(self):
        print('I eat non veg')
    def say_something(self):
        print('Bhow Bhow')

myAnimal = Animal() #Animal Created
myAnimal.say_something() #I can't

myDog = Dog() #Dog created
myDog.say_something() #Bhow Bhow
