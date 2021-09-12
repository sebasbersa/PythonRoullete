import random

class Roullete():
    resultados = []
    numero = 0

    def __init__(self):
        print("ruleta inicializada")

    def girarRuleta(self):
        self.numero = random.randint(0,36)
        self.resultados.append(self.numero)
        return self.numero

    def obtenerResultados(self):
        return self.resultados

    def betDocena(self, docena):
        resultado = self.girarRuleta()
        betting = []
        if(docena == 1):
            betting = [3,5,7,12,14,16,21,23,25,30,32,34]
            if(resultado in betting):
                return True
            else:
                return False
        if(docena == 2):
            betting = [2,4,8,11,13,17,20,22,26,29,31,35]
            if(resultado in betting):
                True
            else:
                return False
    def bet2Docenas(self, docenas):
        resultado = self.girarRuleta()
        if(docenas == 1):
            # 2da y 3ra
            if(resultado > 12):
                return True
            else:
                return False
        if(docenas == 2):
            # 1ra y 2da
            if(resultado > 0 and resultado < 25):
                return True
            else:
                return False
        if(docenas == 3):
            # 1ra y 3ra
            if(resultado > 0 and resultado < 13 or resultado > 24 ):
                return True
            else:
                return False

class Jugador():
    nombre = ""
    stack = 0
    def __init__(self, nombre, stack):
        self.nombre = nombre
        self.stack = stack

    def getNombre(self):
        return self.nombre
    def getStack(self):
        return self.stack
    def setStack(self, stack):
        self.stack = stack
    def betDocena(self, ruleta, docena, bet):
        if(ruleta.betDocena(docena) == True):
            self.stack += bet*2
            return True
        else:
            self.stack -= bet
            return False
    def bet2Docenas(self, ruleta, docenas, bet):
        if(ruleta.bet2Docenas(docenas) == True):
            self.stack += bet
            return True
        else:
            self.stack -= bet*2
            return False
    def bet2DocenasStrategy(self, ruleta):
        initBet = 100
        bet = initBet
        iter = 0
        while(self.getStack() < 770000 and self.getStack() > 0 ):
            if(bet > self.getStack()):
                bet = self.getStack()
            if(self.bet2Docenas(ruleta, 1, bet)):
                bet = 3*bet
            else:
                bet = initBet
            iter += 1
        if(self.getStack() > 770000):
            return True
        else:
            return False
    def evaluar2DocenasStrategy(self, ruleta, stackInit, iteraciones):
        gan = 0
        per = 0
        for i in range(0, iteraciones):
            random.seed(i)
            self.setStack(stackInit)
            if(self.bet2DocenasStrategy(ruleta)==True):
                gan += 1
            else:
                per += 1
        print("gano: ", gan)
        print("perdio: ", per)
        print("porcentaje de ganados: ", gan * 100 / (gan + per), "%")


    def docenaStrategy(self, ruleta):
        betting = [1200, 2400, 3600, 4800, 7200, 10800, 16800, 25200, 38400, 57600, 86400, 129600]
        i = 0
        iter = 0
        while(self.getStack() < 770000 and self.getStack() > 0):
            if(i > 11):
                i = 11
            bet = betting[i]
            if(self.betDocena(ruleta, 1, bet)==True):
                i = 0
            else:
                i += 1
            iter += 1
        if(self.getStack() > 770000):
            return True
        else:
            return False

    def evaluarDocenaStrategy(self, ruleta, stackInit, iteraciones):
        gan = 0
        per = 0
        for i in range(0, iteraciones):
            random.seed(i)
            self.setStack(stackInit)
            if(self.docenaStrategy(ruleta)== True):
                gan += 1
            else:
                per += 1
        print("gano: ", gan)
        print("perdio: ", per)
        print("porcentaje de ganados: ", gan * 100 / (gan + per), "%")





def main():
    ruleta = Roullete();
    usuario = Jugador("Sebastian", 385000)
    print(usuario.getNombre())
    print(usuario.getStack())
    print("Estrategia 1 docena")
    usuario.evaluarDocenaStrategy(ruleta, 385000, 10000)
    print("\n")
    print("Estrategia 2 docenas")
    usuario.evaluar2DocenasStrategy( ruleta, 385000, 10000)

if __name__ == '__main__':
    main()
