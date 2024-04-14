from random import randint

numero_aleatorio=randint(1,3)
data= input ("introducir piedra papel o tijera")

#piedra =1
#papel= 2
#tijera=3

if( data== "piedra"):
   if numero_aleatorio==1:
    print( "computadora= piedra")
    print("empate")
   if numero_aleatorio==2:
    print( "computadora= papel")
    print("perdiste")
    if numero_aleatorio==3:
     print( "computadora= tijera")
     print("ganaste")

if( data== "papel"):
   if numero_aleatorio==1:
    print( "computadora= piedra")
    print("ganaste")
   if numero_aleatorio==2:
    print( "computadora= papel")
    print("empate")
   if numero_aleatorio==3:
    print( "computadora= tijera")
    print("perdiste")

if( data== "tijera"):
   if numero_aleatorio==1:
    print( "computadora= piedra")
    print("perdiste")
   if numero_aleatorio==2:
    print( "computadora= papel")
    print("ganaste")
   if numero_aleatorio==3:
    print( "computadora= tijera")
    print("empate")