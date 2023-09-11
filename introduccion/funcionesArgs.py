def suma(a,b):
    c = a+b
    print("la suma es:",c)
    
#suma (10 , 25 ) 
 
def sumaArgs(*args):
    resultado = 0
    for x in args:
           resultado = x+resultado
    print("el resultado de los argumentos son: ",resultado)
    
sumaArgs(3,5,6)