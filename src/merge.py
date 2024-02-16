from typing import TextIO

MAX = 999999


# Unificado "ES" el archivo
def guardar(padron: int, nombre: str, apellido: str, unificado: TextIO) -> None:
    unificado.write(f"{padron},{nombre},{apellido}\n")


def leer(archivo: TextIO) -> tuple:
    if linea := archivo.readline():
        # PADRON,NOMBRE,APELLIDO\n
        padron, nombre, apellido = linea.rstrip().split(",")
        return int(padron), nombre, apellido
    else:
        return MAX, "", ""


def merge(nombre_archivo1: str, nombre_archivo2: str, nombre_unificado: str) -> None:
    with open(nombre_archivo1, "r") as archivo1, \
            open(nombre_archivo2, "r") as archivo2, \
            open(nombre_unificado, "w") as unificado:
        padron1, nombre1, apellido1 = leer(archivo1)
        padron2, nombre2, apellido2 = leer(archivo2)
        while padron1 < MAX or padron2 < MAX:
            minimo = min(padron1, padron2)
            while padron1 == minimo:
                guardar(padron1, nombre1, apellido1, unificado)
                padron1, nombre1, apellido1 = leer(archivo1)
            while padron2 == minimo:
                guardar(padron2, nombre2, apellido2, unificado)
                padron2, nombre2, apellido2 = leer(archivo2)
