# 1. cada jugador es un individuo dentro del algoritmo genetico
# 2. cada individuo dentro del algoritmo genetico es una red neuronal.
# 3. cada accion de la red neuronal es una estrategia en la ruleta

import jugador
import roulette
import neural
import genetic
import numpy as np

def main():
    print("iniciado")
    # hola = ["manzana", "pera", "naranja"]
    # for i in range(1, len(hola)+1):
    #     print(hola[-i])
    # ruleta = roulette.Roullete(10)
    # usuario = jugador.Jugador("Sebastian", 385000)
    # print(usuario.getNombre())
    # print(usuario.getStack())
    #
    # datosDeEntrada = ruleta.resultados
    # datosDeEntrada.append(usuario.getStack())
    # print(datosDeEntrada)

    # print("Estrategia 1 docena")
    # usuario.evaluarDocenaStrategy(ruleta, 385000, 10000)
    # print("\n")
    # print("Estrategia 2 docenas")
    # usuario.evaluar2DocenasStrategy( ruleta, 385000, 10000)
    # ----------------------------
    # GENERACIONES
    # target = [1,0,0,1,1,0,0,1]
    # model = genetic.DNA(target = target, mutation_rate = 0.5, n_individuals = 50, n_selection = 10, n_generation = 50, verbose = True)
    # model.runGeneticAlgorithm()
    # ----------------------------
    # NEURAL
    # red = neural.NeuralNetwork([3,5], 1)
    #
    # print(len(red.layers))
    # training_inputs = np.array([[0,0,1],
    #                             [1,1,1],
    #                             [1,0,1]])
    # training_outputs = np.array([[0,1,1]]).T
    #
    # red.train(training_inputs, training_outputs, 1000)
    # print("nuevas sinaptics")
    # print("\n")
    # a = str(input("input 1: "))
    # b = str(input("input 2: "))
    # c = str(input("input 3: "))
    #
    # print("new situation: ", a, b, c)
    # print(red.thinkNew(np.array([a,b,c])))
    # ----------------------------

if __name__ == '__main__':
    main()
