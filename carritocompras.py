data_leches = 0
data_galletas = 0
data_gaseosas = 0
data_huevos = 0
data_aceites = 0
data_pan = 0
precio_leches = 0
precio_galletas = 0
precio_gaseosas = 0
precio_huevos = 0
precio_aceite = 0
precio_pan = 0
total = 0
data=0

while True:
    
    menu = """
    MENU
    1. Agregar producto
    2. Eliminar producto
    3. Ver lista de compras
    4. Finalizar compra
    5. Salir
    """
    print(menu)
    data = input("Ingrese una opción del menú: ")

    if data == "5":
        break

    if data == "1":
        menu_productos = """
        Agregar producto
        1. Leche $50 
        2. Galletas $35  
        3. Gaseosa $87 
        4. Huevos $66 
        5. Aceite $110 
        6. Pan $20
        7. Regresar al MENU
        """
        print(menu_productos)

        data_producto = input("Ingrese el número del producto que desea agregar: ")

        if data_producto == "1":
            data_leches += int(input("Ingrese la cantidad de Leches: "))
        elif data_producto == "2":
            data_galletas += int(input("Ingrese la cantidad de Galletas: "))
        elif data_producto == "3":
            data_gaseosas += int(input("Ingrese la cantidad de Gaseosas: "))
        elif data_producto == "4":
            data_huevos += int(input("Ingrese la cantidad de Huevos: "))
        elif data_producto == "5":
            data_aceites += int(input("Ingrese la cantidad de Aceite: "))
        elif data_producto == "6":
            data_pan += int(input("Ingrese la cantidad de Pan: "))

    if data == "3":
        print("Lista de compras:")
        if data_leches > 0:
            print("Leches:", data_leches)
        if data_galletas > 0:
            print("Galletas:", data_galletas)
        if data_gaseosas > 0:
            print("Gaseosas:", data_gaseosas)
        if data_huevos > 0:
            print("Huevos:", data_huevos)
        if data_aceites > 0:
            print("Aceites:", data_aceites)
        if data_pan > 0:
            print("Pan:", data_pan)
        print("*********************************")

    if data == "2":
        menu_prod = """
        Eliminar producto
        1. Leche $50 
        2. Galletas $35  
        3. Gaseosa $87 
        4. Huevos $66 
        5. Aceite $110 
        6. Pan $20
        7. Regresar al MENU
        """
        print(menu_prod)
        eliminar_producto = input("Ingrese el número del producto que desea eliminar: ")

        if eliminar_producto == "1":
            data_leches = 0
        elif eliminar_producto == "2":
            data_galletas = 0
        elif eliminar_producto == "3":
            data_gaseosas = 0
        elif eliminar_producto == "4":
            data_huevos = 0
        elif eliminar_producto == "5":
            data_aceites = 0
        elif eliminar_producto == "6":
            data_pan = 0

    if data == "4":
        precio_leches = data_leches * 50
        precio_galletas = data_galletas * 35
        precio_gaseosas = data_gaseosas * 87
        precio_huevos = data_huevos * 66
        precio_aceite = data_aceites * 110
        precio_pan = data_pan * 20

        total = precio_leches + precio_galletas + precio_gaseosas + precio_huevos + precio_aceite + precio_pan

        print("Total a pagar:", total)

   
        break

