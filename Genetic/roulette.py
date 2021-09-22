import random

class Roullete():
    resultados = []
    numero = 0

    def __init__(self, n_resultados):
        print("ruleta inicializada")
        for i in range(0,n_resultados):
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