import math
class Recta:
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    pendiente = 0

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calcularAnguloInclinacion(self):
        self.calcularPendiente()
        angulo = self.calculoArcoTangente(self.pendiente)
        if angulo < 0:
            angulo = 180 + angulo
        return angulo

    def calculoArcoTangente(self, valTangente):
        arcocotangente = math.atan(valTangente)
        valorAngulo = round(math.degrees(arcocotangente), 3)
        return valorAngulo

    def calcularPendiente(self):
        deltaX = self.x2 - self.x1
        deltaY = self.y2 - self.y1
        self.pendiente = deltaY / deltaX

    def ecuacionPuntoPendiente(self):
        y1 = -1 * self.y1
        b = self.x1 * self.pendiente

        signoY1 = ""
        if(y1>0): signoY1 = "+"
        signoB = ""
        if (b > 0): signoB = "+"

        ecuacion = "y "+signoY1+" "+str(y1)+" = "+str(self.pendiente)+" x "+signoB+" "+str(b)
        return ecuacion