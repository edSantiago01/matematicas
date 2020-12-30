# LEY DE SENOS, Resuelve un triángulo a partir de 2 lados y un ángulo
# Copyright (C) 2020  Edgar Santiago
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

def calcularSeno(angulo):
    anguloRadianes = math.radians(angulo)
    seno = math.sin(anguloRadianes)
    return seno

def calcularArcoseno(valorSeno):
    arcoseno  = math.asin(valorSeno)
    valorAngulo = round(math.degrees(arcoseno), 3)
    return valorAngulo


def calcularAnguloB(anguloA, ladoA, ladoB):
    print('\nCALCULAR ÁNGULO "B"')
    print('sen(B) / b = sen(A) / a')
    print('sen(B) = (b) ( sen(A) / a )')
    print('sen(B) = ('+str(ladoB)+') ( sen('+str(anguloA)+'°) / '+str(ladoA)+' )')

    valorSeno = calcularSeno(anguloA)
    print('sen(B) = (' + str(ladoB) + ') ( ' + str(round(valorSeno,3)) + ' / ' + str(ladoA) + ' )')

    cociente = valorSeno/ ladoA
    print('sen(B) = (' + str(ladoB) + ') ( ' + str(round(cociente, 3)) + ' )')

    valorSeno = ladoB * cociente
    print('sen(B) = '+str(round(valorSeno, 3)))
    print('B = arcoseno('+str(round(valorSeno, 3))+'))')

    valorAngulo = calcularArcoseno(valorSeno)
    print('B = ' + str(round(valorAngulo, 3)) + '°' )
    return valorAngulo


def calcularLadoC(ladoA, anguloA, anguloC):
    print('\nCALCULAR LADO "c"')
    print('c / sen(C) = a / sen(A)')
    print('c = ( sen(C) ) ( a / sen(A) ) ')
    print('c = ( sen('+str(anguloC)+'° ) ( '+str(ladoA)+' / sen('+str(anguloA)+'°) ) ')

    valorSenoA = calcularSeno(anguloA)
    valorSenoC = calcularSeno(anguloC)
    print('c = ( ' + str(round(valorSenoC)) + ' ) ( ' + str(ladoA) + ' / ' + str(round(valorSenoA, 3)) + ' )')

    cociente = ladoA / valorSenoA
    print('c = ( ' + str(round(valorSenoC)) + ' ) ( ' + str(round(cociente)) + ' )')

    ladoC = valorSenoC * cociente
    print('c = ' + str(round(ladoC)))
    return ladoC

print("Magnitud del lado 'a':")
ladoA = float(input())

print("Magnitud del Ángulo A, opuesto al lado 'a' (DEG):")
anguloA = float(input())

print("Magnitud del lado 'b':")
ladoB = float(input())

anguloB = calcularAnguloB(anguloA, ladoA, ladoB)
anguloC = 180 - anguloA - anguloB

ladoC = calcularLadoC(ladoA, anguloA, anguloC)

print('\nLado A: '+str(ladoA))
print('Lado B: '+str(ladoB))
print('Lado C: '+str(round(ladoC, 3)))

print('\nAngulo A: '+str(anguloA)+ '°')
print('Angulo B: '+str(round(anguloB, 3)) + '°')
print('Angulo C: '+str(round(anguloC, 3)) + '°')