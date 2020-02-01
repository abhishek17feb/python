class Dog():

    def __init__(self):
        print('Dog created')

    def speak(self):
        print('I am a dog')

class Cat():

    def __init__(self):
        print('Cat created')
    def speak(self):
        print('I am a cat')

class TestSpeak():

    def testMySpeach(self, pet):
        pet.speak()

dog = Dog()
cat = Cat()
mySpeach =TestSpeak()
mySpeach.testMySpeach(cat) #I am a cat