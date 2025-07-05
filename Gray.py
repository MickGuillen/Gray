# Convierte un número decimal a binario de 5 bits
def binario(n, bits=5):
    return format(n, f'0{bits}b')

# Convierte un número decimal a código Gray
def gray(n):
    return n ^ (n >> 1)

# Devuelve el código Gray como cadena binaria de 5 bits
def gray_binario(n, bits=5):
    return format(gray(n), f'0{bits}b')

# Contador binario ascendente con cálculo de costo por cambio de bits
def incremento_binario():
    resultados = []
    actual = binario(0)
    resultados.append((0, actual, '-'))
    for i in range(1, 32):
        siguiente = binario(i)
        costo = sum(1 for a, b in zip(actual, siguiente) if a != b)
        resultados.append((i, siguiente, costo))
        actual = siguiente
    return resultados

# Contador Gray ascendente con cálculo de costo por cambio de bits
def incremento_gray():
    resultados = []
    actual = gray_binario(0)
    resultados.append((0, actual, '-'))
    for i in range(1, 32):
        siguiente = gray_binario(i)
        costo = sum(1 for a, b in zip(actual, siguiente) if a != b)
        resultados.append((i, siguiente, costo))
        actual = siguiente
    return resultados

# Imprime tabla con formato estilo A[4]...A[0] y Costo total
def mostrar_tabla_formato(resultados, titulo):
    print(f"\n{titulo}")
    print(f"{'Valor':<8}{'A[4]':<6}{'A[3]':<6}{'A[2]':<6}{'A[1]':<6}{'A[0]':<6}{'Costo total'}")
    print("-" * 55)
    for valor, bin_str, costo in resultados:
        bits = list(bin_str)
        print(f"{valor:<8}{bits[0]:<6}{bits[1]:<6}{bits[2]:<6}{bits[3]:<6}{bits[4]:<6}{costo}")

# Suma de todos los costos (cambios de bits)
def costo_total(resultados):
    return sum(c for _, _, c in resultados if isinstance(c, int))

# Programa principal
if __name__ == "__main__":

    resultados_binario = incremento_binario()
    resultados_gray = incremento_gray()

    # Mostrar tabla estilo A[4] A[3] A[2] A[1] A[0]
    mostrar_tabla_formato(resultados_binario, "---------- Contador Binario ----------".center(50))
    mostrar_tabla_formato(resultados_gray, "---------- Contador Gray ----------".center(50))

    # Costos totales
    total_bin = costo_total(resultados_binario)
    total_gray = costo_total(resultados_gray)

    print("---------- Costos Totales ----------".center(35))
    print(f"Total de cambios en contador binario: {total_bin}")
    print(f"Total de cambios en contador Gray: {total_gray}")
