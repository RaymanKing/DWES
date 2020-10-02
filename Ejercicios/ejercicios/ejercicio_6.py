def palindromo():
    frase = input("Inserta una frase")
    frase2 = frase[::-1]

    if frase[::-1] == frase2:
        print("Es palindromo")
    else:
        print("No es palindromo")
