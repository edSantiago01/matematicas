# LEY DE COSENOS, Calcula los ángulos internos (DEG) de un triángulo
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

def calcularArcocoseno(valorCoseno):
    arcocoseno = math.acos(valorCoseno)
    valorAngulo = round(math.degrees(arcocoseno), 3)
    return valorAngulo


def calcularAnguloC(ladoA, ladoB, ladoC):
    print('\nCALCULAR ÁNGULO "C"')
    print("c^2 = a^2 + b^2 - 2ab cosC")
    print("cosC = (c^2 - a^2 - b^2) /(- 2ab )")
    print('cosC = (' + str(ladoC) + '^2 - ' + str(ladoA) + '^2 - ' + str(ladoB) + '^2) /( -2(' + str(ladoA) + ')(' + str(ladoB) + '))')
    denominador = -2 * ladoA * ladoB
    cuadradoA = round(ladoA ** 2, 3)
    cuadradoB = round(ladoB ** 2, 3)
    cuadradoC = round(ladoC ** 2, 3)
    print('cosC = (' + str(cuadradoC) + ' - ' + str(cuadradoA) + ' - ' + str(cuadradoB) + ') /( ' + str(round(denominador, 3)) + ' )')
    numerador = cuadradoC - cuadradoA - cuadradoB
    print('cosC = (' + str(round(numerador, 3)) + ') /(' + str(round(denominador, 3)) + ' )')
    valorCoseno = numerador / denominador
    print('C = arco(' + str(round(valorCoseno, 3)) + ')')
    angulo = calcularArcocoseno(valorCoseno)
    print('C = ' + str(round(angulo, 3)) + "°")
    return angulo


def calcularAnguloB(ladoA, ladoB, ladoC):
    print('\nCALCULAR ÁNGULO "B"')
    print("b^2 = a^2 + c^2 - 2ac cosB")
    print("cosB = (b^2 - a^2 - c^2) /(- 2ac )")
    print('cosB = (' + str(ladoB) + '^2 - ' + str(ladoA) + '^2 - ' + str(ladoC) + '^2) /( -2(' + str(ladoA) + ')(' + str(ladoC) + '))')
    denominador = -2 * ladoA * ladoC
    cuadradoA = round(ladoA ** 2, 3)
    cuadradoB = round(ladoB ** 2, 3)
    cuadradoC = round(ladoC ** 2, 3)
    print('cosB = (' + str(cuadradoB) + ' - ' + str(cuadradoA) + ' - ' + str(cuadradoC) + ') /( ' + str(round(denominador, 3)) + ')')
    numerador = cuadradoB - cuadradoA - cuadradoC
    print('cosB = (' + str(round(numerador, 3)) + ') /(' + str(round(denominador, 3)) + ' )')
    valoCoseno = numerador / denominador
    print('B = arco(' + str(round(valoCoseno, 3)) + ')')
    angulo = calcularArcocoseno(valoCoseno)
    print('B = ' + str(round(angulo, 3)) + "°")
    return angulo


def calcularAnguloA(ladoA, ladoB, ladoC):
    print('\nCALCULAR ÁNGULO "A"')
    print("a^2 = b^2 + c^2 - 2bc cosA")
    print("cosA = (a^2 - b^2 - c^2) /(- 2bc )")
    print('cosA = (' + str(ladoA) + '^2 - ' + str(ladoB) + '^2 - ' + str(ladoC) + '^2) /( -2(' + str(ladoB) + ')(' + str(ladoC) + '))')
    denominador = -2 * ladoB * ladoC
    cuadradoA = round(ladoA ** 2, 3)
    cuadradoB = round(ladoB ** 2, 3)
    cuadradoC = round(ladoC ** 2, 3)
    print('cosA = (' + str(cuadradoA) + ' - ' + str(cuadradoB) + ' - ' + str(cuadradoC) + ') /( ' + str(round(denominador, 3)) + ')')
    numerador = cuadradoA - cuadradoB - cuadradoC
    print('cosA = (' + str(round(numerador, 3)) + ') /(' + str(round(denominador, 3)) + ' )')
    valorCoseno = numerador / denominador
    print('A = arco(' + str(round(valorCoseno, 3)) + ')')
    angulo = calcularArcocoseno(valorCoseno)
    print('A = ' + str(round(angulo, 3)) + "°")
    return angulo

print("\n LEY DE COSENOS\n Calcula todos los ángulos internos a partir de la magnitud de los lados.")
print("\n Magnitud del lado A:")
ladoA = float(input())
print("Magnitud del lado B:")
ladoB = float(input())
print("Magnitud del lado C:")
ladoC = float(input())

anguloA = calcularAnguloA(ladoA, ladoB, ladoC)
anguloB = calcularAnguloB(ladoA, ladoB, ladoC)
anguloC = calcularAnguloC(ladoA, ladoB, ladoC)

print('\nÁngulo A = ' + str(round(anguloA, 3)) + "°")
print('Ángulo B = ' + str(round(anguloB, 3)) + "°")
print('Ángulo C = ' + str(round(anguloC, 3)) + "°")