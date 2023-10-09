nombre = input("Ingresa tu nombre: ")
if nombre.isalpha():
    edad = input("Ingresa tu edad: ")
    if edad.isdigit():
       cumple = input("Mes de cumpleaños: ")
       if cumple.isalpha():
        escuela =input("Escuela a la que asistes: ")
        direccion = input("Ingresa tu direccion: ")
        if direccion.isalnum():
            pelicula = input("Pelicula favorita: ") 

            print("******DATOS PERSONALES******")
            print("Nombre:" + nombre)
            print("Edad:" + edad)
            print("Cumpleaños:" + cumple)
            print("Escuela:" + escuela)
            print("Direccion:" + direccion)
            print("Pelicula Favorita:" + pelicula)
        else:
            print("Tipo de dato no valido")
       else:
         print("Tipo de dato no valido")
    else:
        print("Favor de solo introducir numeros") 
else:
    print("No se permite introducir numero o simbolos")



