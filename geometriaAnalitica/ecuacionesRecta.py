# Ecuaciones Recta, Calcula la ec. punto pendiente, ordenada al origen y general
# a partir de dos puntos de un segmento de recta A( x1, y1 ) B( x2, y2 )
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

from Recta import Recta



print("ECUACIONES DE LA RECTA")
print("Obtener la ecuación punto pendiente, ordendad al origen y general de una recta que pasa por los puntos A y B\n")
print("A( x1, y1 )  B( x2, y2 )\n")

print("Coordenada (x1):")
x1 = float(input())
print("Coordenada (y1):")
y1 = float(input())

print("Coordenada (x2):")
x2 = float(input())
print("Coordenada (y2):")
y2 = float(input())

recta = Recta(x1, y1, x2, y2)
recta.calcularPendiente()
recta.calcularValoresEcuaciones()
ecPuntoPendiente = recta.ecPuntoPendiente()
ecOrdenadaOrigen = recta.ecOrdenadaOrigen()
ecGeneral = recta.ecGeneral()

print("Ecuación Punto Pendiente: \n")
print(str(ecPuntoPendiente))

print("Ecuación Ordenada al Origen: \n")
print(str(ecOrdenadaOrigen))

print("Ecuación General: \n")
print(str(ecGeneral))