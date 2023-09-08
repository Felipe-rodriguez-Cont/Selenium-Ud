#introduciendo valores

#print("Nombre?")
#nombre = input()

#print(f"Hola {nombre}")

while True:
    try:
        print("dime un numero; ")
        numero=int (input())
        if numero > 0:
            print(f"el numero es; {numero} ")
            break
        else:
            print("Solo numeros positivos ")
        
    except ValueError:
        print ("no es un número")
        continue
    



    
