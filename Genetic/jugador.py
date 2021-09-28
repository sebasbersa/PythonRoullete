from neural import NeuralNetwork
from roulette import Roullete

class Jugador(NeuralNetwork):
    nombre = ""
    stack = 0
    def __init__(self, nombre, stack, tam_layers, n_outputs):
        self.nombre = nombre
        self.stack = stack
        self.initStack = stack
        NeuralNetwork.__init__(self,tam_layers, n_outputs)

    def getNombre(self):
        return self.nombre
    def getStack(self):
        return self.stack
    def setStack(self, stack):
        self.stack = stack
    def desicion(self, outputs):
        return int(outputs.index(1))

    def Jugar(self, ruleta):
        self.stack = self.initStack
        iter = 0
        puntaje = 0
        while self.getStack() < 770000 and self.getStack() >= 0:
            desicion = self.desicion(self.thinkNew(ruleta.obtenerResultados()))
            if desicion == 0:
                if self.docenaStrategyOnce(ruleta, 0) == True:
                    puntaje += 1
            elif desicion == 1:
                if self.docenaStrategyOnce(ruleta, 1) == True:
                    puntaje += 1
            elif desicion > 1:
                if self.bet2DocenasStrategyOnce(ruleta, desicion - 2) == True:
                    puntaje += 1
            # if(iter % 1000 == 0):
            #     print(iter)
            iter += 1
        if self.getStack() <= 0:
            return 0
        else:
            fitness = puntaje / iter
            return fitness

    def bet2DocenasStrategyOnce(self, ruleta, desicion):
        initBet = 100
        bet = initBet
        win = 0
        while win == 0 and self.getStack() > 0:
            if(bet > self.getStack()):
                bet = self.getStack()
            if self.bet2Docenas(ruleta, desicion, bet) == True:
                win +=1
            else:
                bet = 3 * bet
        if win > 0:
            return True
        else:
            return False

    def docenaStrategyOnce(self, ruleta, desicion):
        betting = [1200, 2400, 3600, 4800, 7200, 10800, 16800, 25200, 38400, 57600, 86400, 129600]
        i = 0
        win = 0
        while win == 0 and self.getStack() > 0:
            if(i > 11):
                i = 11
            bet = betting[i]
            if self.betDocena(ruleta, desicion, bet) == True:
                i = 0
            else:
                i += 1
        if win > 0:
            return True
        else:
            return False
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
            random.seed(i + 5000)
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
            random.seed( i + 5000)
            self.setStack(stackInit)
            if(self.docenaStrategy(ruleta)== True):
                gan += 1
            else:
                per += 1
        print("gano: ", gan)
        print("perdio: ", per)
        print("porcentaje de ganados: ", gan * 100 / (gan + per), "%")
