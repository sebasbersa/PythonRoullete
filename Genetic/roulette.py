import random

class Roullete():
    resultados = []
    numero = 0

    def __init__(self, n_resultados):
        print("ruleta inicializada")
        for i in range(0,n_resultados):
            self.girarRuleta()

    def girarRuleta(self):
        self.numero = random.randint(0,36)
        self.resultados.append(self.numero)
        return self.numero

    def obtenerResultados(self):
        results = self.resultados
        if len(results) > 20:
            results = results[-21:-1]
        return results

    def betDocena(self, docena):
        resultado = self.girarRuleta()
        betting = []
        if(docena == 0):
            if(resultado in betting):
                return True
            else:
                return False
        if(docena == 1):
            betting = [2,4,8,11,13,17,20,22,26,29,31,35]
            if(resultado in betting):
                True
            else:
                return False
    def bet2Docenas(self, docenas):
        resultado = self.girarRuleta()
        if(docenas == 0):
            # 2da y 3ra
            if(resultado > 12):
                return True
            else:
                return False
        if(docenas == 1):
            # 1ra y 2da
            if(resultado > 0 and resultado < 25):
                return True
            else:
                return False
        if(docenas == 2):
            # 1ra y 3ra
            if(resultado > 0 and resultado < 13 or resultado > 24 ):
                return True
            else:
                return False
