
def sayHello(name):
    print(f'Hello Mr.{name}')

sayHello('Abhishek') #Hello Mr.Abhishek

#Adding information of the function

def showFunctionInfo(name):
    """
    The function will print any name provided as a parameter
    :rtype: object
    :param name: String value
    :return: nono
    """
    print('Here showed the information of the function')

showFunctionInfo('abhishek')

#*args used when we don't know the number of arguments which will be passed to a funcion, *args is like a tuple

def my_func(*args):
    print(args) #(12, 67, 34)
    print('The sum is', sum(args)) #The sum is 113

my_func(12,67,34)

#**kwargs return dictionary

def my_another_function(**kwargs):
    print(kwargs) #{'name': 'abhishek'}
    if 'name' in kwargs:
        print('My name is {name}'.format(name = kwargs['name']))
    else:
        print('There is no name associated')

my_another_function(name='abhishek') #My name is abhishek

my_another_function(fruit='apple')
#{'fruit': 'apple'}
#There is no name associated

#The difference between *args and **kwargs is that *args return tuples and **kwargs returns dictionary
