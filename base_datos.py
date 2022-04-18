def main():

    print("""MENU REGISTROS
    1 - Nuevo Registro
    2 - Mostrar Registro
    3 - Eliminar Registro
    """)

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("Nuevo Registro")
        archivo = open("base_datos.csv","a")

        nombre = input("Ingrese el nombre: ")
        documento = input("Ingrese el documento: ")

        print("Se a almacenado: " + nombre + ", con el documento: " + documento)

        archivo.write(nombre)
        archivo.write(",")
        archivo.write(documento)
        archivo.write(",")
        archivo.write("\n")

        archivo.close()

    elif opcion == "2":
        print("Mostrar registros")
        archivo = open("base_datos.csv")

        print(archivo.read())

        archivo.close()

    elif opcion == "3":
        archivo = open("base_datos.csv","a")
        archivo.truncate()

        print("Registros eliminados")

        archivo.close()

    else:
        print("Debes elegir una opción valida")

if __name__ == '__main__':
    main()
