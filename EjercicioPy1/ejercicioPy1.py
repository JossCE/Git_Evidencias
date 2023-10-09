#! /bin/bash
print('ES NUMERO PAR O IMPAR?')
numero = int(input ('Ingresar un numero cualquiera: '))
if numero % 2 == 0:
    print(numero, "es numero par")
else:
    print(numero, "es numero impar")
    