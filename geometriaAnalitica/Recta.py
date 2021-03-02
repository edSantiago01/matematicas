import math
from fractions import Fraction
class Recta:
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    pendiente = 0
    b = 0

    y1PuntoP = 0
    bPuntoP  = 0
    signoY1PuntoP = ""
    signoBPuntoP = ""
    signoB = ""

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

    def calcularValoresEcuaciones(self):
        self.y1PuntoP = -1 * self.y1
        self.bPuntoP = self.x1 * self.pendiente * -1
        if self.y1PuntoP > 0:
            self.signoY1PuntoP = "+" #para concatenar en cadena
        if self.bPuntoP > 0:
            self.signoBPuntoP = "+"

            #para ec. ordenada al origen:
        y1 = self.y1PuntoP * -1  # cambio de signo al pasar del otro lado de la ecuación
        self.b = self.bPuntoP + y1
        if self.b > 0:
            self.signoB = "+"


    def ecPuntoPendiente(self): # y - y1 = m(x - x1)
        ecuacion = "y "+self.signoY1PuntoP+" "+str(Fraction(self.y1PuntoP).limit_denominator())+" = "+str(Fraction(self.pendiente).limit_denominator())+" x "+self.signoBPuntoP+" "+str(Fraction(self.bPuntoP).limit_denominator())
        return ecuacion

    def ecOrdenadaOrigen(self): # y = mx +
        valPendiente = self.validarCoeficienteUno(self.pendiente)
        ecuacion = "y = "+str(valPendiente)+" x "+self.signoB+" "+str(Fraction(self.b).limit_denominator())
        return  ecuacion

    def validarCoeficienteUno(self, valor):
        if valor == 1:
            formatoValor = ""
        elif valor == -1 :
            formatoValor = "-"
        else:
            formatoValor = Fraction(valor).limit_denominator()
        return  formatoValor

    def ecGeneral(self): # Ax + By + C = 0
        pendiente = self.pendiente
        b = self.b
        y = "- y"
        if self.pendiente < 0:
            pendiente = self.pendiente * -1
            b = self.b * -1
            y = "+ y"
        signoB = ""
        if b > 0:
            signoB = "+"

        valPendiente = self.validarCoeficienteUno(pendiente)
        ecuacion = " "+str(valPendiente)+" x "+y+" "+signoB+" "+str(Fraction(b).limit_denominator())+" = 0"
        return ecuacion