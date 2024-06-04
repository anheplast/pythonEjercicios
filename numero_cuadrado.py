
#Dado un número entero, determina si es un número cuadrado 

# Si la raiz cuadrada de n es un numero entero entonces n es un numero cuadrado
# Multiplicar el numero para si mismo, para saber si el resultado es igual a n

import math

def is_square(n):
    if (n < 0):
        return False
    result = math.sqrt(n)
    if result.is_integer():
        int(result)
        if (result * result == n):
            return True
    else:
        return False



#Test
print(f"\nEs un numero cuadrado? {is_square(-1)}")
print(f"Es un numero cuadrado? {is_square(0)}")
print(f"Es un numero cuadrado? {is_square(3)}")
print(f"Es un numero cuadrado? {is_square(4)}")
print(f"Es un numero cuadrado? {is_square(25)}")
print(f"Es un numero cuadrado? {is_square(26)}")



