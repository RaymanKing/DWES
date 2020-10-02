mi_coche = {"color": "blanco",
            "marca": "seat",
            "modelo": "ateca",
            "colores_disponibles": ["rojo", "negro"]}

mi_coche["marca"]
mi_coche["color"] = "azul"
mi_coche.get("color")

"marca" in mi_coche
# Devolvera true

"motor" in mi_coche
# Devolvera false

# Hacemos que nos deuelva una tupla
mi_coche.items()

# Devolvera los valores
mi_coche.values()

# Devolvera las llaves ej: marca
mi_coche.keys()

# Saca la ultima key con su value
mi_coche.popitem()

# Sacar todas las keys con sus valores
for key, value in versiones.items():
    print(clave,valor)

