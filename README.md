# Clase 16: Merge

[Enlace a la presentación de git](https://docs.google.com/presentation/d/1XZF4_X7avzln-3k-zgRcmRW8CXkbf4hKztfK7ubs1Go/edit?usp=sharing)

Ambos algoritmos se pueden resumir en el siguiente pseudocódigo:

```
def merge (archivo1, archivo2, unificado):
    informacion1 = leer(archivo1)
    informacion2 = leer(archivo2)
    while (parametro1 < MAX) or (parametro2 < MAX):
        minimo = min(parametro1, parametro2)
        while (parametro1 == minimo):
            guardar(informacion1, unificado)
            informacion1 = leer(archivo1)
        while (parametro2 == minimo):
            guardar(informacion2, unificado)
            informacion2 = leer(archivo2)
```

Donde:

1. archivo1 y archivo2 son los archivos de texto que serán leídos.
2. unificado es el archivo final.
3. informacion1 e informacion2 contienen la información de una linea de los respectivos archivos (procesada o no,
   dependiendo de la implementación).
4. parametro1 y parametro2 son los campos específicos a comparar de la información leida.

Complejidad del merge: **O(N)**

Lo crucial es que al finalizar un archivo, la función leer() devuelva un dato "hardcodeado" igualado a MAX.<br>
MAX es una constante de valor muy alto para asegurarnos de que mínimo nunca sea MAX. Por lo tanto, evitamos leer
el archivo que ya fue totalmente recorrido.<br>

En este repositorio se realiza un merge de dos archivos con el formato:

> PADRON,NOMBRE,APELLIDO

Considerando la siguiente precondición:

1. Los archivos están ordenados por el valor a comparar (y de la misma forma ascendente).
