import random
import numpy as np

class NeuralNetwork():
    def __init__(self):
        self.layer1 = self.createSynapticWeights(3,5)
        self.layer2 = self.createSynapticWeights(5,1)

    def createSynapticWeights(self, entrada, salida):
        return 2 * np.random.random((entrada, salida)) - 1

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):

        for iteration in range(training_iterations):
            # Pass the training set through our neural network (a single neuron).
            l1 = self.think(training_inputs, self.layer1)
            l2 = self.think(l1, self.layer2)

            # Calculate the error (The difference between the desired output
            # and the predicted output).

            l2_error = training_outputs - l2
            l2_delta = l2_error * self.sigmoid_derivative(l2)
            l1_error = l2_delta.dot(self.layer2.T)
            l1_delta = l1_error * self.sigmoid_derivative(l1)

            # Multiply the error by the input and again by the gradient of the Sigmoid curve.
            # This means less confident weights are adjusted more.
            # This means inputs, which are zero, do not cause changes to the weights.
            ajustes = np.dot(training_inputs.T, l1_error * self.sigmoid_derivative(l1))
            ajustes2 = np.dot(l1.T, l2_error * self.sigmoid_derivative(l2))

            self.layer1 += ajustes
            self.layer2 += ajustes2

    def think(self, inputs, layer):
        output = self.sigmoid(np.dot(inputs, layer))
        return output
    def thinkNew(self, inputs):
        inputs = inputs.astype(float)
        l1 = self.think(inputs, self.layer1)
        return self.think(l1, self.layer2)


class DNA():
    def __init__(self, target, mutation_rate, n_individuals, n_selection, n_generation, verbose = True):
        self.target = target
        self.mutation_rate = mutation_rate
        self.n_individuals = n_individuals
        self.n_selection = n_selection
        self.n_generation = n_generation
        self.verbose = verbose
    def createIndividual(self, min = 0, max = 9):
        individual = [np.random.randint(min, max) for i in range(len(self.target))]
        return individual
    def createPopulation(self):
        population = [self.createIndividual() for i in range(self.n_individuals)]
        return population
    def fitness(self, individual):
        fitness = 0
        for i in range(len(individual)):
            if(individual[i] == self.target[i]):
                fitness += 1
        return fitness
    def selection(self, population):
        # Metodo para seleccionar los mejores
        scores = [(self.fitness(i), i) for i in population]
        scores = [i[1] for i in sorted(scores)]
        return scores[len(scores)-self.n_selection:]
    def reproduction(self, population, selected):
        point = 0
        father = []

        for i in range(len(population)):
            point = np.random.randint(1, len(self.target) - 1)
            father = random.sample(selected, 2)

            population[i][:point] = father[0][:point]
            population[i][point:] = father[1][point:]

        return population
    def mutation(self, population):
        for i in range(len(population)):
            if random.random() <= self.mutation_rate:
                point = np.random.randint(len(self.target))
                new_value = np.random.randint(0,9)

                while new_value == population[i][point]:
                    new_value = np.random.randint(0, 9)
                population[i][point] = new_value
        return population
    def runGeneticAlgorithm(self):
        population = self.createPopulation()
        for i in range(self.n_generation):
            if self.verbose:
                print ('____________\n')
                print('Generacion : ', i)
                print('Poblacion', population)
                print('\n')
            selected = self.selection(population)
            population = self.reproduction(population, selected)
            population = self.mutation(population)

class Roullete():
    resultados = []
    numero = 0

    def __init__(self):
        print("ruleta inicializada")
        for i in range(0,10):
            numero = self.girarRuleta()
            self.resultados.append(numero)

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





def main():
    ruleta = Roullete();
    print(ruleta.resultados)
    usuario = Jugador("Sebastian", 385000)
    print(usuario.getNombre())
    print(usuario.getStack())

    datosDeEntrada = ruleta.resultados
    datosDeEntrada.append(usuario.getStack())
    print(datosDeEntrada)

    # print("Estrategia 1 docena")
    # usuario.evaluarDocenaStrategy(ruleta, 385000, 10000)
    # print("\n")
    # print("Estrategia 2 docenas")
    # usuario.evaluar2DocenasStrategy( ruleta, 385000, 10000)
    # ----------------------------
    # GENERACIONES
    # target = [1,0,0,1,1,0,0,1]
    # model = DNA(target = target, mutation_rate = 0.5, n_individuals = 50, n_selection = 10, n_generation = 50, verbose = True)
    # model.runGeneticAlgorithm()
    # ----------------------------
    # NEURAL
    # neural = NeuralNetwork()
    # print(neural.layer1, neural.layer2)
    # training_inputs = np.array([[0,0,1],
    #                             [1,1,1],
    #                             [1,0,1],
    #                             [0,0,1]])
    # training_outputs = np.array([[0,1,1,0]]).T
    #
    # neural.train(training_inputs, training_outputs, 1000)
    # print("nuevas sinaptics")
    # print(neural.layer1, neural.layer2)
    # print("\n")
    # a = str(input("input 1: "))
    # b = str(input("input 2: "))
    # c = str(input("input 3: "))
    #
    # print("new situation: ", a, b, c)
    # print(neural.thinkNew(np.array([a,b,c])))

if __name__ == '__main__':
    main()
