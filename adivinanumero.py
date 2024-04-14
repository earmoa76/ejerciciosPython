data=0
numero=0


from random import randint
numero = randint(0,1000)


while True: 
    data= int(input ("ingresar un numero del 1 al 1000 :"))

    if data > numero:
       print ("el numero incognita es menor")
    
    elif data < numero:
       print ("el numero incognita es mayor")

    else:
       print ("el numero es el correrto!!")
       break