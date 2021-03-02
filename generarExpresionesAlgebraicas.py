# GENERADOR DE EXPRESIONES, Genera expresiones algebraicas al azar para la sintaxis de LibreMath
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


import random

variables = [
    'a',
    'b',
    'c',
    'v',
    'w',
    'x',
    'x',
    'y',
    'y',
    'z',
]

potencias = [2,3,4]

print("Generador de expresiones algebraicas")
nExpresiones = 5

tamVariables = len(variables) - 1
tamPotencias = len(potencias) - 1

for i in range(0, nExpresiones):
    ranV1 = random.randint(0, tamVariables)
    ranV2 = random.randint(0, tamVariables)
    ranV3 = random.randint(0, tamVariables)
    ranP1= random.randint(0, tamPotencias)
    ranP2 = random.randint(0, tamPotencias)
    ranP3 = random.randint(0, tamPotencias)
    ranP4 = random.randint(0, tamPotencias)
    coef1 = random.randint(2, 10)
    coef2 = random.randint(2, 10)
    coef3 = random.randint(2, 10)
    coef4 = random.randint(2, 10)

    #Suma
    # print("\n " + str(i+1) +". ("+str(variables[ranV1])+"^{"+str(potencias[ranP1])+"} + "+str(coef2)+str(variables[ranV2])+"^{"+str(potencias[ranP2])+"})     -  ( "+str(coef3)+str(variables[ranV3])+"^{"+str(potencias[ranP3])+"} +"+str(coef4)+str(variables[ranV3])+"^{"+str(potencias[ranP1])+"})  newline")

    # Suma fracciones
    # print("\n " + str(i+1) +". ({"+str(coef2)+"}over{"+str(coef4)+"}"+ str(variables[ranV1])+"^{"+str(potencias[ranP1])+"} + "+str(coef2)+str(variables[ranV2])+"^{"+str(potencias[ranP3])+"})      -   ( {"+str(coef3)+"}over{"+str(coef1)+"}"+str(variables[ranV1])+"^{"+str(potencias[ranP1])+"} +"+str(coef4)+str(variables[ranV3])+"^{"+str(potencias[ranP1])+"})  newline")

    #multiplicacion 1
    # print("\n " + str(i+1) +". ("+str(variables[ranV1])+"^{"+str(potencias[ranP1])+"}  "+str(variables[ranV2])+"^{"+str(potencias[ranP2])+"})       ( "+str(coef3)+str(variables[ranV3])+"^{"+str(potencias[ranP3])+"} +"+str(coef4)+str(variables[ranV3])+"^{"+str(potencias[ranP1])+"})  newline")
    # print("\n " + str(i+1) +". ("+str(variables[ranV1])+"^{"+str(potencias[ranP1])+"} + "+str(coef2)+str(variables[ranV2])+"^{"+str(potencias[ranP2])+"})    ( "+str(coef3)+str(variables[ranV3])+"^{"+str(potencias[ranP3])+"} +"+str(coef4)+str(variables[ranV3])+"^{"+str(potencias[ranP1])+"})  newline")
    # print("\n " + str(i + 1) + ". (-" + str(variables[ranV3]) + "^{" + str(potencias[ranP1]) + "} )     ( " + str(coef3) + str(variables[ranV3]) + "^{" + str(        potencias[ranP3]) + "} -" + str(coef4) + str(variables[ranV3]) + "^{" + str(potencias[ranP1]) + "})  newline")
    # multiplicacion fracción
    # print("\n " + str(i+1) +". ({"+str(coef2)+"}over{"+str(coef4)+"}"+ str(variables[ranV1])+"^{"+str(potencias[ranP1])+"} + {"+str(coef3)+"}over{"+str(coef1)+"}"+str(variables[ranV2])+"^{"+str(potencias[ranP3])+"})         ( {"+str(coef2)+"}over{"+str(coef1)+"}"+str(variables[ranV1])+"^{"+str(potencias[ranP2])+"} +"+str(coef4)+str(variables[ranV3])+"^{"+str(potencias[ranP4])+"})  newline")

    #division
    # print("\n " + str(i+1) +". ("+str(variables[ranV3])+"^{"+str(potencias[ranP1])+"} + "+str(coef2)+str(variables[ranV3])+"^{"+str(potencias[ranP2])+"})  /  ( "+str(coef4)+str(variables[ranV3])+"^{"+str(potencias[ranP1])+"})  newline")
    # print("\n " + str(i+1) +". ("+str(variables[ranV3])+"^{"+str(potencias[ranP3])+"} + "+str(coef2)+str(variables[ranV3])+"^{"+str(potencias[ranP4])+"})  / [ ( "+str(coef4)+str(variables[ranV3])+"^{"+str(potencias[ranP1])+"}) ( "+str(coef1)+str(variables[ranV3])+"^{"+str(potencias[ranP2])+"})]  newline")

    # Binomio al cuadrado
    # print("\n " + str(i+1) +". ("+str(variables[ranV1])+"^{"+str(potencias[ranP1])+"} + "+str(coef2)+str(variables[ranV2])+"^{"+str(potencias[ranP2])+"}) ^{2}   newline")
    # print("\n " + str(i+1) +". ("+str(coef2)+str(variables[ranV1])+"^{"+str(potencias[ranP1])+"} - "+str(coef2)+str(variables[ranV2])+"^{"+str(potencias[ranP2])+"}) ^{2}   newline")

    # Binomio conjugado
    # print("\n " + str(i+1) +". ("+str(coef1)+str(variables[ranV1])+" + "+str(coef2)+str(variables[ranV2])+")    ( "+str(coef1)+str(variables[ranV1])+" -"+str(coef2)+str(variables[ranV2])+")  newline")
    # print("\n " + str(i+1) +". ({"+str(coef1)+"}over{"+str(coef2)+"}"+str(variables[ranV1])+" + "+str(coef2)+str(variables[ranV2])+")    ( {"+str(coef1)+"}over{"+str(coef2)+"}"+str(variables[ranV1])+" -"+str(coef2)+str(variables[ranV2])+")  newline")

    # Binomio con un término en común
    # print("\n " + str(i+1) +". ("+str(coef1)+str(variables[ranV1])+" + "+str(coef2)+str(variables[ranV2])+")    ( "+str(coef1)+str(variables[ranV1])+" +"+str(coef3)+str(variables[ranV3])+")  newline")

    # factoriza binomio al cuadrado
    print("\n " + str(i+1) +". "+str(variables[ranV1])+"^{2} + "+str(coef2)+str(variables[ranV2])+"^{"+str(potencias[ranP2])+"})     -  ( "+str(coef3)+str(variables[ranV3])+"^{"+str(potencias[ranP3])+"} +"+str(coef4)+str(variables[ranV3])+"^{"+str(potencias[ranP1])+"})  newline")