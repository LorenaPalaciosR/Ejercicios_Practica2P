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

# Programa


print("Bienvenido a Apuestas.com")
print("**********")
print("  _______________________________")
print(f" Fecha:  {formato_fecha(dia)}")
print(f" {pais1} vs {pais2}")
print(f" Hora: {hora_random}")
print("  _______________________________")
