#lista
lenguajes = ["Php","Java","Python"]

print("prueba "+ lenguajes[0])

#agregar algo al final de la lista
lenguajes.append("Swift")
print("los lenguajes son:",lenguajes)

#modificar item de la lista
lenguajes[0] = "pascal"
print("los lenguajes son:",lenguajes)

#eliminar item de la lista
lenguajes.remove("Swift")
print("los lenguajes son:",lenguajes)