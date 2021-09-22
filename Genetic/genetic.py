import numpy as np
import random
import neural

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
