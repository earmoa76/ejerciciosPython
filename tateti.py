def imprimir_tablero():
    for fila in jugar_1:
        print("|".join(fila))
        print("-" * 5)

def jugar(jugada, jugador, jugar_1):
    if jugador == 1:
        simbolo = "x"
    else:
        simbolo = "o"

    if jugada == "a1":
        jugar_1[0][0] = simbolo
    elif jugada == "a2":
        jugar_1[1][0] = simbolo
    elif jugada == "a3":
        jugar_1[2][0] = simbolo
    elif jugada == "b1":
        jugar_1[0][1] = simbolo
    elif jugada == "b2":
        jugar_1[1][1] = simbolo
    elif jugada == "b3":
        jugar_1[2][1] = simbolo
    elif jugada == "c1":
        jugar_1[0][2] = simbolo
    elif jugada == "c2":
        jugar_1[1][2] = simbolo
    elif jugada == "c3":
        jugar_1[2][2] = simbolo
    else:
        print("Movimiento no válido. Por favor, ingresa un movimiento válido.")

    return jugar_1

# Definir una matriz 3x3 llena de ceros
jugar_1 = [[" ", " ", " "],
           [" ", " ", " "],
           [" ", " ", " "]]

def check_ganar():
    if (#fila
        jugar_1[0][0] == jugar_1[0][1] == jugar_1[0][2] == "x" or 
        jugar_1[1][0] == jugar_1[1][1] == jugar_1[1][2] == "x" or 
        jugar_1[2][0] == jugar_1[2][1] == jugar_1[2][2] == "x" or 
        #columna
        jugar_1[0][0] == jugar_1[1][0] == jugar_1[2][0] == "x" or 
        jugar_1[0][1] == jugar_1[1][1] == jugar_1[2][1] == "x" or 
        jugar_1[0][2] == jugar_1[1][2] == jugar_1[2][2] == "x"or
        #diagonal
        jugar_1[0][0] == jugar_1[1][1] == jugar_1[2][2]=="x" or
        jugar_1[0][2] == jugar_1[1][1] == jugar_1[2][0]=="x"
        ):


        return "gano1"# gano el jugador 1
    
    elif (#filas
          jugar_1[0][0] == jugar_1[0][1] == jugar_1[0][2] == "o" or
          jugar_1[1][0] == jugar_1[1][1] == jugar_1[1][2] == "o" or
          jugar_1[2][0] == jugar_1[2][1] == jugar_1[2][2] == "o" or
          
          #columnas
          jugar_1[0][0] == jugar_1[1][0] == jugar_1[2][0] == "o" or
          jugar_1[0][1] == jugar_1[1][1] == jugar_1[2][1] == "o" or
          jugar_1[0][2] == jugar_1[1][2] == jugar_1[2][2] == "o" or
          #diagonal
          jugar_1[0][0] == jugar_1[1][1] == jugar_1[2][2] =="o"or
          jugar_1[0][2] == jugar_1[1][1] == jugar_1[2][0]== "o"):
        
        return "gano2" # gano el jugador 2
    
    
    # si esta lleno el tablero es empate
    elif all(cell != " " for row in jugar_1 for cell in row):
        return "empate"
    
    
    else:
        return None

ganador = None


print(" INSTRUCCIONES: INGRESAR a-b-c para filas y 1-2-3 para columnas ejemplo:a1")

jugar_1 = [["x", " ", " "],
           [" ", " ", " "],
           [" ", " ", " "]]
imprimir_tablero()


print("**********************************************")

print("********* EMPECEMOS A JUGAR ******************")


jugar_1 = [[" ", " ", " "],
           [" ", " ", " "],
           [" ", " ", " "]]

#print(jugar_1)


while not ganador:

    imprimir_tablero()
    jugador = 1
    jugada = input("Jugador 1, ¿dónde quieres jugar? (a1-a2-a3-b1-b2-b3-c1-c2-c3): ")
    
    jugar(jugada, jugador, jugar_1)
    ganador = check_ganar()
    if ganador == "gano1":
        imprimir_tablero()
        print("¡Jugador 1 ha ganado!")
        break

    elif ganador == "empate":
        imprimir_tablero()
        print("¡El juego ha terminado en empate!")
        break



    imprimir_tablero()
    jugador = 2
    jugada = input("Jugador 2, ¿dónde quieres jugar? (a1-a2-a3-b1-b2-b3-c1-c2-c3): ")
    
    jugar(jugada, jugador, jugar_1)
    ganador = check_ganar()
    if ganador == "gano2":
       imprimir_tablero()
       print("¡Jugador 2 ha ganado!")
       break
