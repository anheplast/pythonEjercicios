#Los cajeros automáticos permiten códigos PIN de 4 ó 6 dígitos 
#y los códigos PIN no pueden contener más que exactamente 4 dígitos o exactamente 6 dígitos.

#Si a la función se le pasa una cadena PIN válida, devuelve true, en caso contrario devuelve false.

def validate_pin(pin):
    if (pin.isdigit()):
        if (len(pin) == 6 or len(pin) == 4):
            return True
        else:
            return False
    else:
        return False



print(validate_pin("a123"))
print(validate_pin("123"))
print(validate_pin("123456"))
print(validate_pin("1234"))

