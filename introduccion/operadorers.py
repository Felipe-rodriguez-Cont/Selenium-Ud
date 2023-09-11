while True:
    try:
        num = int(input("digita un numero: "))
        num2 = int(input("digita otro numero: "))
        if num > 0 or num2 < 0:
            if num > num2:
                print (f"el numero {num} es mayor que {num2} ")
            elif num2 == num:
                print ("los numeros son iguales")
            else:
                print (f"el numero {num2} es mayor que {num} ")
            break
        else:
            print ("Solo numeros positivos")
            continue
    except ValueError:
        print("SOLO NUMEROS, IMBECIL")  
        