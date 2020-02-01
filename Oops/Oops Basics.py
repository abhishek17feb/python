##Class

class my_sample_class():


    def __init__(self, name):
        print(f'Hello Mr.{name} how are you')
        self.name = name

mySampleClass = my_sample_class('Abhishek') #Hello Mr.Abhishek how are you
name = mySampleClass.name
print(name) #Abhishek

#Self is the instance of the object itself. All the variables attached to it are different for different instance
#Class object attributes are attributes which is shared among all the instance, they are same for all the instances

class Dog():
    color = 'Black'

    def __init__(self, name):
        self.name = name

    def what_is_your_name(self):
        print(f'Hi my name is {self.name}, how are you')

huskie = Dog('Huskie')
junior = Dog('junior')

huskie.what_is_your_name() #Hi my name is Huskie, how are you
junior.what_is_your_name() #Hi my name is junior, how are you

print(f'My color is {huskie.color}') #My color is Black
print(f'My color is {huskie.color}') #My color is Black



