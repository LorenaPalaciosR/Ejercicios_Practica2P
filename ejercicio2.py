# 2) Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales
# o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos 
# mensuales y muestre por pantalla si el usuario tiene que tributar o no. (10p) (Joel + Joseph)

#Joseph Soncco
def tributar():
    edad = int(input("Ingrese su edad: "))
    ingresos = float(input("Ingrese sus ingresos mensuales: "))

    if edad < 16:
        mensaje = f"Tienes {edad} años, lo cual no es suficiente para tributar."
    elif ingresos < 1000:
        mensaje = f"Tienes {edad} años, pero tus ingresos de {ingresos:.2f} € no son suficientes para tributar."
    else:
        mensaje = f"Tienes {edad} años y ganas {ingresos:.2f} €. Por lo tanto, debes tributar."

    print(mensaje)
    
tributar()