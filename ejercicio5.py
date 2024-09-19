from datetime import date
import datetime
import random


# 5) En este ejercicio, tendrán total libertad para elegir la problemática y la mejor solución.
# Cada grupo podrá decidir su propio enfoque y desarrollar el software según sus criterios.
# El grupo que presente la mejor solución será el único en recibir los 60 puntos asignados a esta pregunta.
# ¡Buena suerte! -

# Funciones


def hora_aleatoria():
    hora = random.randint(8, 23)
    minuto = random.randint(0, 59)
    return datetime.time(hora, minuto, 0)


def formato_fecha(date):
    months = (
        "Enero",
        "Febrero",
        "Marzo",
        "Abri",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre",
    )
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} de {} del {}".format(day, month, year)

    return messsage


def pais_aleatorio(paises):
    pais1 = random.choice(paises)
    pais2 = random.choice(paises)
    while pais2 == pais1:
        pais2 = random.choice(paises)
    return pais1, pais2


def apuesta_dolares(apuesta):

    while apuesta < 10 or apuesta == " ":
        print("La apuesta mínima es de 10 dólares.")
        apuesta = float(input("Ingresa una nueva cantidad: "))
    return apuesta


def equipo_ganador(pais1, pais2, gol_equipo1, gol_equipo2):

    if gol_equipo1 > gol_equipo2:
        return pais1
    elif gol_equipo2 > gol_equipo1:
        return pais2
    else:
        return "Empate"


def cuota_aleatoria():
    cuota_pais1 = random.uniform(1.5, 3.0)
    cuota_pais2 = random.uniform(1.5, 3.0)
    cuota_empate = random.uniform(2.0,4.0)
    return cuota_pais1, cuota_pais2, cuota_empate


def goles_aleatorio():
    gol_equipo1 = random.randint(0, 10)
    gol_equipo2 = random.randint(0, 10)
    return gol_equipo1, gol_equipo2


# Variables

dia = date.today()
hora_random = hora_aleatoria()
paises = [
    "Brasil",
    "México",
    "Argentina",
    "Colombia",
    "Chile",
    "Perú",
    "Venezuela",
    "Cuba",
    "Ecuador",
    "Uruguay",
]

pais1, pais2 = pais_aleatorio(paises)

cuota_pais1, cuota_pais2, cuota_empate = cuota_aleatoria()

# Programa


print("Bienvenido a Apuestas.com")
print("**********")
print("  _______________________________")
print(f" Fecha:  {formato_fecha(dia)}")
print(f" {pais1} vs {pais2}")
print(f" Hora: {hora_random}")
print("  _______________________________")


print("  _______________________________")

print(" Cuotas por equipo")
print(f" Para {pais1}: {cuota_pais1:.2f}  vs {pais2}: {cuota_pais2:.2f}")
print(f"Empate: {cuota_empate:.2f}")
print("  _______________________________")

eleccion = input(f"¿Por cuál equipo quieres apostar ({pais1} - {pais2}) o Empate : ")

apuesta = float(input("El mínimo de apuesta es 10 USD, ¿Cuánto deseas apostar?: "))
apuesta_valida = apuesta_dolares(apuesta)
gol_equipo1, gol_equipo2 = goles_aleatorio()
ganador = equipo_ganador(pais1, pais2, gol_equipo1, gol_equipo2)


print(f"Confirmamos de recibido su apuesta {apuesta_valida}")
print(f"Confirmamos que seleccionó apostar por {eleccion}")

if ganador == eleccion:
    if ganador == pais1:
        ganancia = apuesta_valida * cuota_pais1
    elif ganador == pais2:
        ganancia = apuesta_valida * cuota_pais2
    elif ganador == "Empate":
        ganancia = apuesta_valida * cuota_empate
    print(f"Resultado: {pais1} - {gol_equipo1} - {pais2} - {gol_equipo2}")
    print(f"¡Felicidades! Ganaste {ganancia:.2f} dólares apostando por {ganador}.")
else:
    print(f"Resultado: {pais1} - {gol_equipo1} - {pais2} - {gol_equipo2}")
    print(f"Lo siento, perdiste. {ganador} fue el ganador.")
