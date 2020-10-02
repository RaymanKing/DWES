def year_bisiesto():
    year = input("Introduce el año")

    if len(year) != 4:
        print("Introduce un año con sus 4 dígitos")
    else:
        year = int(year)
        if ((year % 4) == 0 and (year % 100) != 0) or ((year % 100) == 0 and (year % 400) == 0):
            print("Es un año bisiesto")
        else:
            print("No es un año bisiesto")