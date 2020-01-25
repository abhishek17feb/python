condition = 1
if condition:
    print('Condition is true');
else:
    print('Condition is false');

##Condition is true
##Any statment which result in boolean will be accepted by if elif statement, 1 is also accepted as Boolean TRUE

location = 'Pune'

if location.__eq__('Pune'):
    print('I am in pune')
elif location.__eq__('Bangalore'):
    print('I am in bangalore');
else :
    print('I am no where');