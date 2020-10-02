def ocurrencias():
    frase = input("Introduce una frase")
    caracter = input("Introduce un caracter")

    if len(caracter) != 1:
        print("Introduce solo un carácter")
    else:
        frase_final = frase.replace(caracter, "*")

    print(frase_final)