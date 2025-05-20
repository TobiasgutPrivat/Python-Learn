class Bottle:
    def open(self):
        pass

class Fridge:
    def putbottle(self, bottle):
        self.__bottle = bottle

    def getbottle(self):
        return self.__bottle

b = Bottle()
f = Fridge()
f.putbottle(b)
b = f.getbottle()
b.open()