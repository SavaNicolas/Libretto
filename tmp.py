class Prova:
    _myClassVariable = 0

    def __init__(self, input):
        self.myInstanceVariable = input

    #per controller e modello
    def standardMethod(self):  #hanno accesso a self
        print(self.myInstanceVariable)

    @staticmethod #dao
    def staticMethod():#hanno accesso solo a quello che passi come parametro
        pass

    @classmethod #dbconnect
    def classMethod(cls): #hanno accesso agli attribiuti di classe(quelli senza self)
        print(cls._myClassVariable)

newInstance = Prova("txt")
newInstance.standardMethod()