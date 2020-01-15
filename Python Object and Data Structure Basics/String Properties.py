##Strings are immutable i.e a String cannot be changed after it has been assigned a Value

name = 'abhishek'
##### name[0] = 'f' : This will throw an exception. So the solution is String concatination
new_name = 'f' + name[1:]
print(new_name)

##Multiplication of letters
myLetter = 'a'
print(myLetter *10) ##Will give a 10 times

##Converting string into Upper Case
print(name.upper()) ##Will give ABHISHEK
print(name.lower())

##Spliting String
string_to_be_splitted = 'Hello There'
print(string_to_be_splitted.split()) ## ['Hello', 'There'] By Default it splits the white spaces
print(string_to_be_splitted.split('e'))  ##['H', 'llo Th', 'r', '']
