def main():

    final = float(input("colocar nota: "))
    if final >= 9:
        print("Sos un genio")
    elif final >= 7:
        print("Aprobaste")
    elif final == 6:
        print("Te falto poco")
    elif final <= 5:
        print("Estudia en el curso de Andrés")
    else:
        print("Esta nota no se puede evaluar")

if __name__ == '__main__':
    main()
