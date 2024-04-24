
class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                self.productos.remove(producto)
                return True
        return False

    def buscar_producto(self, criterio, valor):
        productos_encontrados = []
        for producto in self.productos:
            if getattr(producto, criterio) == valor:
                productos_encontrados.append(producto)
        return productos_encontrados

    def actualizar_producto(self, nombre, nueva_info):
        for producto in self.productos:
            if producto.nombre == nombre:
                producto.__dict__.update(nueva_info)
                return True
        return False

    def mostrar_inventario(self):
        for producto in self.productos:
            print(f"Nombre: {producto.nombre}, Categoría: {producto.categoria}, Precio: {producto.precio}, Cantidad: {producto.cantidad}")


def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Salir")


# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()
    
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            categoria = input("Ingrese la categoría del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            producto = Producto(nombre, categoria, precio, cantidad)
            inventario.agregar_producto(producto)
            print("¡Producto agregado al inventario!")
        elif opcion == "2":
            print("\nInventario:")
            inventario.mostrar_inventario()
        elif opcion == "3":
            criterio = input("Ingrese el criterio de búsqueda (nombre, categoría, precio, cantidad): ")
            valor = input("Ingrese el valor a buscar: ")
            productos_encontrados = inventario.buscar_producto(criterio, valor)
            if productos_encontrados:
                print("\nProductos encontrados:")
                for producto in productos_encontrados:
                    print(f"Nombre: {producto.nombre}, Categoría: {producto.categoria}, Precio: {producto.precio}, Cantidad: {producto.cantidad}")
            else:
                print("No se encontraron productos.")
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto que desea actualizar: ")
            nueva_info = {}
            nueva_info["nombre"] = input("Nuevo nombre (dejar en blanco si no desea cambiar): ")
            nueva_info["categoria"] = input("Nueva categoría (dejar en blanco si no desea cambiar): ")
            nueva_info["precio"] = float(input("Nuevo precio (dejar en blanco si no desea cambiar): ") or "0")
            nueva_info["cantidad"] = int(input("Nueva cantidad (dejar en blanco si no desea cambiar): ") or "0")
            if inventario.actualizar_producto(nombre, nueva_info):
                print("¡Producto actualizado!")
            else:
                print("El producto no se encontró en el inventario.")
        elif opcion == "5":
            nombre = input("Ingrese el nombre del producto que desea eliminar: ")
            if inventario.eliminar_producto(nombre):
                print("¡Producto eliminado del inventario!")
            else:
                print("El producto no se encontró en el inventario.")
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
 


 
