# LPUNTOS RECTA, Calcula la distancia, pendiente y ángulo de inclinación de un segmento de recta
# conociento dos puntos de la recta A( x1, y1 ) B( x2, y2 )
# Copyright (C) 2021  Edgar Santiago
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import math

def calculoArcoTangente(valTan):
    arcocotangente = math.atan(valTan)
    valorAngulo = round(math.degrees(arcocotangente), 3)
    return valorAngulo

def calcularAnguloInclinacion( pendiente ):
    angulo = calculoArcoTangente(pendiente)
    if angulo < 0:
        angulo = 180 + angulo
    return angulo

def calcularPendiente(x1, y1, x2, y2):
    deltaX = x2 - x1
    deltaY = y2 - y1
    pendiente = deltaY / deltaX
    return pendiente

def calcularDistancia(x1, y1, x2, y2):
    deltaX = x2 - x1
    deltaY = y2 - y1
    cuadradoX = deltaX ** 2
    cuadradoY = deltaY ** 2
    distancia = math.sqrt( cuadradoX + cuadradoY)
    return distancia
def calcularPuntoMedio(x1, y1, x2, y2):
    x = (x1+x2)/2
    y = (y1+y2)/2
    print("Punto medio : ("+str(round(x, 3))+", "+str(round(y, 3))+")")

print("PUNTOS SOBRE LA RECTA")
print("Calcula el punto medio, pendiente y grados de unclinación de un segmento de recta que pasa por los puntos A y B\n")
print("A( x1, y1 )  B( x2, y2 )\n")

print("Coordenada (x1):")
x1 = float(input())
print("Coordenada (y1):")
y1 = float(input())

print("Coordenada (x2):")
x2 = float(input())
print("Coordenada (y2):")
y2 = float(input())


pendiente = calcularPendiente(x1, y1, x2, y2)
anguloInclinacion = calcularAnguloInclinacion( pendiente )
distancia = calcularDistancia(x1, y1, x2, y2)

print("\n Pendiente : "+str(round(pendiente, 3)))
print("Ángulo de inclinación : "+str(round(anguloInclinacion, 3))+"°")
print("Distancia entre los puntos : "+str(round(distancia, 3)))

calcularPuntoMedio(x1, y1, x2, y2)

