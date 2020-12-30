# PITAGORAS, Calcula la Hipotenusa y el Cateto Opuesto a partir del Cateto Adyacente y el Ángulo Agudo
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
def calculoCoseno(angulo):
    anguloRadianes = math.radians(angulo)
    valorCoseno = math.cos(anguloRadianes)
    return valorCoseno

def calculoTangente(angulo):
    anguloRadianes = math.radians(angulo)
    valorTangente  = math.tan(anguloRadianes)
    return valorTangente


def calculoHipotenusa(anguloAgudo, catetoAdyacente):
    print('\n CÁLCULO DE LA HIPOTENUSA')
    print('cos(A) = CA /  h')
    print('cos(' + str(anguloAgudo) + '°) = ' + str(catetoAdyacente) + ' /  h')
    print('h cos(' + str(anguloAgudo) + '°) = ' + str(catetoAdyacente))
    print('h = ' + str(catetoAdyacente)+'/ cos(' + str(anguloAgudo) + '°)')
    valorCoseno = calculoCoseno(anguloAgudo)
    print('h = ' + str(catetoAdyacente) + ' / ' + str(round(valorCoseno,3)) )
    hipotenusa = catetoAdyacente / valorCoseno
    print('h = ' + str(round(hipotenusa, 3)))
    return hipotenusa

def calculoCO(anguloAgudo, catetoAdyacente):
    print('\n CÁLCULO DEL CATETO OPUESTO')
    print('tan(A) = CO /  CA')
    print('CO = CA tan(A) ')
    print('CO = ('+str(catetoAdyacente)+') tan(' + str(anguloAgudo) + '°) ')
    valorTangente = calculoTangente(anguloAgudo)
    print('CO =  ('+str(catetoAdyacente)+')' + str(round(valorTangente,3)))
    catetoOpuesto = catetoAdyacente * valorTangente
    print('CO = ' + str(round(catetoOpuesto, 3)))
    return catetoOpuesto

print("TEOREMA DE PITÁGORAS")
print("Calcula la Hipotenusa y el Cateto Opuesto a partir del Cateto Adyacente y el Ángulo Agudo en un triángulo rectángulo\n")

print("Magnitud del Ángulo Agudo (DEG):")
anguloAgudo = float(input())

print("Magnitud del Cateto Adyacente:")
catetoAdyacente = float(input())

hipotenusa = calculoHipotenusa(anguloAgudo, catetoAdyacente)
catetoOpuesto = calculoCO(anguloAgudo, catetoAdyacente)

print("\nCateto Adyacente : "+str(round(catetoAdyacente, 3)))
print("Cateto Opuesto : "+str(round(catetoOpuesto, 3)))
print("Hipotenusa : "+str(round(hipotenusa, 3)))


