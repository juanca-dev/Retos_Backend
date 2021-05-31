#Reto Opción 01

"""Reto 1: Desarrollar un programa de bienvenida
11 respuesta sin leer.11 respuesta.
Para este reto tendremos que hacer lo siguiente:

Ingresar un nombre y su edad.
Si es menor de edad que indique que dependiendo de la hora (si es mas de las 6pm) debe ir a dormir y si no hacer la tarea.
Si es mayor de edad que indique que no esta obligado a hacer nada."""


# solución

nombre = input("ingrese su nombre")

edad = int( input('ingrese su edad'))

import time
time.strftime("%H:%M:%S") 



if edad>=18:
  print ("No estas obligado a hacer nada")      
else:
  if edad<=0:  
    print ("si es mas de las 6pm")
  else:  
    if edad<18:
       print ('Debe ir a dormir y si no hacer la tarea')
    else:
       print ('Eres mayor de edad')
print ('Hasta la proxima')
