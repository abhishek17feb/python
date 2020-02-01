class calculator():

    def divide(self, numnber1, number2):
        try:
            self.result = numnber1 / number2
        except:
            print('The number cannot be divided')
            self.result = 0
        finally:
            print('Yee you are done with the division')


myCal = calculator()
myCal.divide(10,5)
print('The division is ', myCal.result)