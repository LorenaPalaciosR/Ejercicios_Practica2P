# 3) Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
# Renta	                     | Tipo impositivo
# Menos de 10000€            | 5%
# Entre 10000€ y 20000€	     | 15%
# Entre 20000€ y 35000€      | 20%
# Entre 35000€ y 60000€      | 30%
# Más de 60000€              | 45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
# (10p) (Nicolás +Lorena)

rent=float(input('Escribir su renta anual: '))

if rent < 10000:
    tipo_impositivo = '5%'
elif 10000 <= rent <= 20000:
    tipo_impositivo = '15%'
elif 20000 <= rent <= 35000:
    tipo_impositivo = '20%'
elif 35000 <= rent <= 60000:
    tipo_impositivo = '30%'
else:
    tipo_impositivo = '45%'
    
print(f'Para su renta anual de {rent} debera pagar el {tipo_impositivo} de impositivo')