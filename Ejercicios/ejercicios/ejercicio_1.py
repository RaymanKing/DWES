def ej1_es_vocal():
    letra = input("Introduce una letra")

    if len(letra) != 1:
        print("Debe ser una letra")
    else:
        if letra in ("a", "e", "i", "o", "u"):
            print("ES VOCAL")
        else:
            print("NO ES VOCAL")