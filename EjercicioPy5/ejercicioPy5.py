print ("OBTENER UN ACRONIMO")
print("---------------------")
frase = input ("Ingresa una frase: ")
palabras = frase.split()
acronimo = ""
for i in palabras:
    acronimo = acronimo + i[0]
print("Acronimo creado para " + frase + " es: " + acronimo)
