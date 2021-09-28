import numpy as np
import random
import neural
from roulette import Roullete
from jugador import Jugador

class DNA():
    def __init__(self, target, mutation_rate, n_individuals, n_selection, n_generation, variation_rate, verbose = True):
        self.target = target
        self.mutation_rate = mutation_rate
        self.n_individuals = n_individuals
        self.n_selection = n_selection
        self.n_generation = n_generation
        self.variation_rate = variation_rate
        self.verbose = verbose

    def createIndividual(self, numero):
        nombre = "Jugador " + str(numero)
        tam_layers = [20, 50,50]
        return Jugador(nombre, 50000, tam_layers, 5)

    def createPopulation(self):
        population = [self.createIndividual(i) for i in range(self.n_individuals)]
        return population

    def fitness(self, individual, ruleta):
        return individual.Jugar(ruleta)


    def takeFirst(self, elem):
        return elem[0]

    def medirDiferencia(self, primero, segundo):
        puntaje_igualdad = 0
        layers_primero = [i.tolist() for i in primero.layers]
        layers_segundo = [i.tolist() for i in segundo.layers]
        layer_1 = []
        layer_2 = []
        for i in range(len(layers_primero)):
            for b in range(len(layers_primero[i])):
                layer_1.append(layers_primero[i][b])
        for i in range(len(layers_segundo)):
            for b in range(len(layers_segundo[i])):
                layer_2.append(layers_segundo[i][b])
        layer_1 = layer_1[0]
        layer_2 = layer_2[0]
        layer_1_normalized = [i / 100  for i in layer_1]
        layer_2_normalized = [i / 100  for i in layer_2]
        difference=[]
        for i in range(len(layer_2_normalized)):
            difference.append(layer_2_normalized[i] - layer_1_normalized[i])
        variation_rate = sum(difference)/len(difference)
        return abs(variation_rate)


    def selection(self, population, ruleta):
        # Metodo para seleccionar los mejores
        scores = [(self.fitness(i , ruleta), i) for i in population]
        scores = sorted(scores, reverse=True, key=self.takeFirst)
        selection = []
        for i in range(0, len(scores)):
            if i == 0:
                selection.append(scores[0][1])
            if self.n_selection - len(selection) == len(scores) - i :
                selection.append(scores[i][1])
            else:
                if self.medirDiferencia(selection[-1], scores[i][1]) >= self.variation_rate:
                    selection.append(scores[i][1])
        return selection

    def reproduction(self, population, selected):
        point = 0
        father = []
        for i in range(len(population)):
            points = [np.random.randint(0,9) for i in range(len(population[0].layers))]
            father = random.sample(selected, 2)
            for x in range(len(population[0].layers)):
                population[x].layers[x][:points[x]] = father[0].layers[x][:points[x]]
                population[x].layers[x][points[x]:] = father[1].layers[x][points[x]:]
        return population

    def mutation(self, population):
        for i in range(len(population)):
            for x in range(len(population[i].layers)):
                for y in range(len(population[i].layers[x])):
                    if random.random() <= self.mutation_rate:
                        point = np.random.randint(len(population[i].layers[x][y]))
                        new_value = np.random.randint(-5,5)
                        while new_value == population[i].layers[x][y][point]:
                            new_value =  np.random.randint(-5,5)
                        population[i].layers[x][y][point] = new_value
        return population
    # def mutation(self, population):
    #     for i in range(len(population)):
    #         if random.random() <= self.mutation_rate:
    #             point = np.random.randint(len(self.target))
    #             new_value = np.random.randint(0,9)
    #             while new_value == population[i][point]:
    #                 new_value = np.random.randint(0, 9)
    #             population[i][point] = new_value
    #     return population

    def runGeneticAlgorithm(self):
        ruleta = Roullete(20)
        population = self.createPopulation()
        selected = self.selection(population, ruleta)
        population = self.reproduction(population, selected)
        population = self.mutation(population)
        print(len(population[0].layers[0]), len(population[0].layers[1]), len(population[0].layers[2]))

        # resultado = population[0].thinkNew(ruleta1.obtenerResultados())
        # print("RESULTADO", resultado)

        #
        # population = self.createPopulation()
        # for i in range(self.n_generation):
        #     if self.verbose:
        #         print ('____________\n')
        #         print('Generacion : ', i)
        #         print('Poblacion', population)
        #         print('\n')
        #     selected = self.selection(population)
        #     population = self.reproduction(population, selected)
        #     population = self.mutation(population)
