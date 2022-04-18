def main():

    print("Elige tu propio camino")
    inicio = input("Escribe empezar para iniciar: ")
    while(inicio == 'empezar'):
        print(""" ¿Que camino deseas elegir?
        escribe la opción con numero
        1 - Quiero ser saludado
        2 - Deseo multliplicar
        3 - Quiero salir del programa """)
        opcion = input()
        if opcion == '1':
            print("Hola, como estas!")
        elif opcion == '2':
            n1 = float(input('Introduce el valor a multlipicar primero: '))
            n2 = float(input('Introduce el valor a multlipicar segundo: '))
            print('El resultado es: ',n1*n2)
        elif opcion == '3':
            print('Gracias por tu tiempo')
            break
        else:
            print('No proceso tu eleccción, inserta alguna de las opciones')

if __name__ == '__main__':
    main()
