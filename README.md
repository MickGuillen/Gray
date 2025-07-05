# Contador Binario vs. Contador Gray en Python

Este proyecto en Python compara dos tipos de contadores digitales: un **contador binario** tradicional y un **contador en código Gray**, evaluando el costo en términos de cambios de bits entre cada incremento.

## Descripción

El objetivo es demostrar la diferencia en eficiencia entre el contador binario y el de código Gray al recorrer todos los valores de 0 a 31 (5 bits), analizando cuántos bits cambian en cada paso. Se generan tablas detalladas y se calcula el **costo total** de los cambios de bits en ambos casos.

### ¿Qué es el Código Gray?

El **código Gray** es una representación binaria donde solo un bit cambia entre un número y el siguiente, lo cual lo hace útil en sistemas digitales donde los cambios simultáneos de múltiples bits pueden generar errores.

## Estructura del Script

El archivo `Gray.py` contiene las siguientes funciones principales:

- `binario(n, bits=5)`: Convierte un número decimal a binario con un formato de 5 bits.
- `gray(n)`: Convierte un número decimal a su representación en código Gray.
- `gray_binario(n, bits=5)`: Representación en cadena binaria del número en código Gray.
- `incremento_binario()`: Genera una lista con los valores binarios del 0 al 31 y el costo por cambio de bits entre cada paso.
- `incremento_gray()`: Similar a la anterior, pero usando código Gray.
- `mostrar_tabla_formato(resultados, titulo)`: Muestra los resultados en una tabla con formato `A[4]` a `A[0]`.
- `costo_total(resultados)`: Calcula el número total de bits que cambiaron a lo largo de los incrementos.



Se imprimen dos tablas en consola:

- Tabla del contador binario con los valores en binario de 5 bits y su costo de transición.
- Tabla del contador Gray con los valores en código Gray y su respectivo costo.

Al final, se muestra un resumen comparando el **total de cambios de bits** en cada método.

## Ejemplo de salida

```
---------- Contador Binario ----------
Valor   A[4]  A[3]  A[2]  A[1]  A[0]  Costo total
0       00000 -
1       00001 1
2       00010 2
...

---------- Contador Gray ----------
Valor   A[4]  A[3]  A[2]  A[1]  A[0]  Costo total
0       00000 -
1       00001 1
2       00011 1
...

---------- Costos Totales ----------
Total de cambios en contador binario: 80
Total de cambios en contador Gray: 49
```

## Requisitos

- Python 3.x

## Aplicaciones

Este código es útil en contextos educativos de ingeniería o electrónica digital para entender:

- Diferencias entre representaciones binarias.
- Eficiencia del código Gray en comparación con el binario.
- Cálculo y análisis de costos por transición de estados en sistemas digitales.

## Autor

Desarrollado por [Alan Guillen](https://github.com/MickGuillen)
