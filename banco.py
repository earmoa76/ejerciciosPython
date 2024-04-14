# Definición de funciones

def solicitar_clave():
    clave = input("Por favor, ingrese su clave de 6 dígitos: ")
    return clave

def verificar_clave(clave_almacenada):
    clave = solicitar_clave()
    if clave == clave_almacenada:
        print("Clave válida. ¡Bienvenido!")
        return True
    else:
        print("Clave incorrecta. Por favor, inténtelo de nuevo.")
        return False

def cambio_clave(clave_almacenada):
    nueva_clave = input("Ingrese su nueva clave de 6 dígitos: ")
    if len(nueva_clave) == 6 and nueva_clave.isdigit():
        print("Clave cambiada con éxito.")
        return nueva_clave
    else:
        print("La nueva clave debe tener 6 dígitos.")
        return clave_almacenada

def menu_inicio():
    print("BANCO XXX")
    print("\n1. INGRESAR\n2. CAMBIAR CLAVE\n3. SALIR\n")
    opcion = input("Ingrese una opción del menú: ")
    return opcion

def menu_ingreso(n_cuenta):
    if n_cuenta=="1":
     print("cuenta n°xxx-xxxx-001")
    else :
      print  ("cuenta n°xxx-xxxx-002")
    print("\nMENU\n1. INGRESAR DINERO\n2. RETIRAR DINERO\n3. CONSULTAR SALDO\n4. TRANSFERIR\n5. ATRAS\n")
    opcion = input("Ingrese una opción del menú: ")
    return opcion

# Función principal
def main():
    clave_almacenada = "123456"  # Clave inicial, puedes cambiarla si lo deseas
    dinero_cuenta1 = 0
    dinero_cuenta1_retirar = 0
    dinero_cuenta2 = 0
    dinero_cuenta2_retirar = 0
    cbu = 0
    transferencia = 0
    n_cuenta = "1"

    while True:
        opcion_menu_inicio = menu_inicio()

        if opcion_menu_inicio == '1':
            if verificar_clave(clave_almacenada):
                while True:
                    print("Selecciona una cuenta:")
                    print("1. xxx-xxxx-001\n2. xxx-xxxx-002")
                    n_cuenta = input("Ingrese el número de la cuenta: ")
                    if n_cuenta in ['1', '2']:
                        break
                    else:
                        print("Cuenta inválida. Inténtelo de nuevo.")
                
                while True:
                    opcion_menu_ingreso = menu_ingreso(n_cuenta)
                    if opcion_menu_ingreso == '1':
                        if n_cuenta == "1":
                            dinero_cuenta1 += int(input("¿Qué cantidad quieres ingresar?: "))
                        elif n_cuenta == "2":
                            dinero_cuenta2 += int(input("¿Qué cantidad quieres ingresar?: "))
                    elif opcion_menu_ingreso == '2':
                        if n_cuenta == "1":
                            print("Dinero en la cuenta 1:", dinero_cuenta1)                
                            dinero_cuenta1_retirar = int(input("¿Qué cantidad quieres retirar?: "))
                            dinero_cuenta1 -= dinero_cuenta1_retirar
                            print("Dinero en la cuenta 1:", dinero_cuenta1)
                        elif n_cuenta == "2":
                            print("Dinero en la cuenta 2:", dinero_cuenta2)                
                            dinero_cuenta2_retirar = int(input("¿Qué cantidad quieres retirar?: "))
                            dinero_cuenta2 -= dinero_cuenta2_retirar
                            print("Dinero en la cuenta 2:", dinero_cuenta2)
                    elif opcion_menu_ingreso == '3':
                        if n_cuenta == "1":
                            print("Dinero en la cuenta xxx-xxxx-001:", dinero_cuenta1)
                        elif n_cuenta == "2":
                            print("Dinero en la cuenta xxx-xxxx-002:", dinero_cuenta2)
                    elif opcion_menu_ingreso == '4':
                        if n_cuenta == "1":
                            print("Dinero en la cuenta 1:", dinero_cuenta1)
                            print("Dinero en la cuenta 2:", dinero_cuenta2)
                            cbu = input("Ingrese el cbu de la cuenta destino: ")
                            transferencia = int(input("¿Cuánto quieres transferir?: "))
                            dinero_cuenta1 -= transferencia
                            print("Transferencia realizada con éxito. Dinero en la cuenta 1:", dinero_cuenta1)
                        elif n_cuenta == "2":
                            print("Dinero en la cuenta 1:", dinero_cuenta1)
                            print("Dinero en la cuenta 2:", dinero_cuenta2)
                            cbu = input("Ingrese el cbu de la cuenta destino: ")
                            transferencia = int(input("¿Cuánto quieres transferir?: "))
                            dinero_cuenta2 -= transferencia
                            print("Transferencia realizada con éxito. Dinero en la cuenta 2:", dinero_cuenta2)


                         # salir
                    elif opcion_menu_ingreso=="5":
                        break
                    elif opcion_menu_ingreso == '6':
                        print("Cerrando sesión...")
                        break
        elif opcion_menu_inicio == '2':
            clave_almacenada = cambio_clave(clave_almacenada)
        elif opcion_menu_inicio == '3':
            print("Saliendo del programa.")
            break

# Llamada a la función principal
if __name__ == "__main__":
    main()
