#abstaction : 

#hinding impleamentation detail only main feature anr showing in user:


class Car():

    def __init__(self):
        self.brack = False
        self.cluchh = False
        self.acc = False

    def Start(self):
        self.breck = True
        self.cluchh = True
        self.acc = True
        print("Car stared.....")

car1 = Car()
car1.Start()            