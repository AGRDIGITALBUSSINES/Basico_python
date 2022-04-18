def main():
    file = open("Prueba.txt","w") # "a" anexa ; "w" elimina ; "x" crea
    file.write("Hola Mundo\n")
    nombre = input("Introduce tu nombre: ") #VARIABLE (crear siempre una variable)
    file.write(nombre + '\n')
    numero = int(input("Introduce tu número: ")) # Tener claro el tipo de valor
    file.write('numero  = % s' %numero + '\n')
    n = int(input("¿Cuantos deportes?: "))
    deportes = []  # VARIABLE donde se va almacenar la lista
    for i in range(n):
        deporte = input("Deportes: ")
        deportes.append(deporte)
    file.write('deportes = %s' %deportes)

    file.close()

if __name__ == '__main__':
    main()
