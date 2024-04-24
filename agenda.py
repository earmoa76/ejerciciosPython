
 

class Contacto:
    def __init__(self, nombre, telefono, correo, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def eliminar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                self.contactos.remove(contacto)
                return True
        return False

    def buscar_contacto(self, criterio, valor):
        contactos_encontrados = []
        for contacto in self.contactos:
            if getattr(contacto, criterio) == valor:
                contactos_encontrados.append(contacto)
        return contactos_encontrados

    def actualizar_contacto(self, nombre, nueva_info):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                contacto.__dict__.update(nueva_info)
                return True
        return False

    def mostrar_agenda(self):
        for contacto in self.contactos:
            print(f"Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Correo: {contacto.correo}, Dirección: {contacto.direccion}")

# Ejemplo de uso
if __name__ == "__main__":
    agenda = Agenda()

    while True:
        print("\nMenú:")
        print("1. Agregar contacto")
        print("2. Mostrar agenda")
        print("3. Buscar contacto")
        print("4. Actualizar contacto")
        print("5. Eliminar contacto")
        print("6. Salir")

        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el teléfono del contacto: ")
            correo = input("Ingrese el correo electrónico del contacto: ")
            direccion = input("Ingrese la dirección del contacto: ")
            contacto = Contacto(nombre, telefono, correo, direccion)
            agenda.agregar_contacto(contacto)
            print("¡Contacto agregado a la agenda!")
        elif opcion == "2":
            print("\nAgenda de contactos:")
            agenda.mostrar_agenda()
        elif opcion == "3":
            criterio = input("Ingrese el criterio de búsqueda (nombre, telefono, correo, direccion): ")
            valor = input("Ingrese el valor a buscar: ")
            contactos_encontrados = agenda.buscar_contacto(criterio, valor)
            if contactos_encontrados:
                print("\nContactos encontrados:")
                for contacto in contactos_encontrados:
                    print(f"Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Correo: {contacto.correo}, Dirección: {contacto.direccion}")
            else:
                print("No se encontraron contactos.")
        elif opcion == "4":
            nombre = input("Ingrese el nombre del contacto que desea actualizar: ")
            nueva_info = {}
            nueva_info["nombre"] = input("Nuevo nombre (dejar en blanco si no desea cambiar): ")
            nueva_info["telefono"] = input("Nuevo teléfono (dejar en blanco si no desea cambiar): ")
            nueva_info["correo"] = input("Nuevo correo electrónico (dejar en blanco si no desea cambiar): ")
            nueva_info["direccion"] = input("Nueva dirección (dejar en blanco si no desea cambiar): ")
            if agenda.actualizar_contacto(nombre, nueva_info):
                print("¡Contacto actualizado!")
            else:
                print("El contacto no se encontró en la agenda.")
        elif opcion == "5":
            nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
            if agenda.eliminar_contacto(nombre):
                print("¡Contacto eliminado de la agenda!")
            else:
                print("El contacto no se encontró en la agenda.")
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

 
