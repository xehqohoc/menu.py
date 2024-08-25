#MENU!

import random 


print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. crear contraseña")
print("5. cerrar")

options = int(input("selecione una opcion:"))

#BLQUE1

if options == 1:
  a = int(input("digite el primer numero:"))
  b = int(input("digite segundo numero:"))
  suma = a + b
  print (suma, "adios!")

#BLQUE2

if options == 2:
	a = int(input("digite el primer numero:"))
	b = int(input("digite el segundo numero:"))
	resta = a - b 
	print (resta,"adios!")

#BLQUE3

if options ==  3:
	a = int(input("digite el primer numero"))
	b  = int(input("digite el segundo numero"))
	mult = a*b
	print (mult,"adios!")

#BLQUE4

if options == 4:
	chars = "abcdefghijklmnñopqrstuvwxyz1234567890*_!/#&"
	password = ""
	for i in range(20):
		password += random.choice(chars)
		print(f"Tu contraseña es:", {password})


#BLQUE5

if options == 5:
	print ("ADIOS!").
	

