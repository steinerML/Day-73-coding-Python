class Shark: #Define a class
    def __init__(self):
        print("This is the constructor method")
    
    def swim(self): #Define swim method
        print("The shark is swimming towards you")
    def be_awesome(self): #Define be_awesome method
        print("The shark is awesome")


big_white = Shark() #Create shark object
big_white.swim() #Call swim method
big_white.be_awesome() #Call be_awesome method

class Shark:
    def __init__(self,name):
        self.name = name
    def swim(self):
        print(self.name, 'is swimming')
    def be_awesome(self):
        print(self.name, 'is awesome')

sammy = Shark('Sammy')
sammy.swim()
sammy.be_awesome()
