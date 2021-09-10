from random import randint
class Roullete():
    resultados = []
    numero = 0

    def __init__(self):
        print("ruleta inicializada")

    def girarRuleta(self):
        self.numero = randint(0,36)
        self.resultados.append(self.numero)
        return self.numero

    def obtenerResultados(self):
        return self.resultados

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
    def betDocenas():
        return True

primera = Roullete();
usuario = Jugador("Sebastian", 80000)
print(usuario.getNombre())
print(usuario.getStack())





# print("1 para seguir, 2 para ver resultados, 0 para terminar:\n")
# while (True):
#     x = input("Ingrese numero: ")
#     if(x == "1"):
#         print("el resultado es: ", primera.girarRuleta())
#     if(x == "2"):
#         print("los resultados fueron: ", primera.obtenerResultados())
#     if(x == "0"):
#         break
