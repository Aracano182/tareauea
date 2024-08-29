def buscar_valor_en_matriz(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"Valor {valor} encontrado en la posición ({i}, {j})"
    return f"Valor {valor} no encontrado en la matriz"

# Definir la matriz de 3x3
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Valor a buscar en la matriz
valor_a_buscar = 100

# Llamar a la función de búsqueda y mostrar el resultado
resultado = buscar_valor_en_matriz(matriz, valor_a_buscar)
print(resultado)
