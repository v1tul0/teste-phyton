def realizar_operacoes(valor1, valor2):
    resultado_soma = valor1 + valor2
    resultado_subtracao = valor1 - valor2
    resultado_multiplicacao = valor1 * valor2

    if valor2 != 0:
        resultado_divisao = valor1 / valor2
    else:
        resultado_divisao = float('inf')  # Infinito positivo por padrão

        if valor1 < 0:
            resultado_divisao = float('-inf')  # Infinito negativo se valor1 for negativo
        elif valor1 == 0:
            resultado_divisao = 'indefinido'  # Indefinido se valor1 for zero

    return [resultado_soma, resultado_subtracao, resultado_multiplicacao, resultado_divisao]

# Exemplo de uso
#valor1 = float(input("Digite o primeiro valor: "))
#valor2 = float(input("Digite o segundo valor: "))

#resultados = realizar_operacoes(valor1, valor2)
#print("Resultados:", resultados)

def test_operacoes_matematicas():
    test_cases = [
        (5, 2),     # Valores positivos
        (8, -3),    # Valores mesclados
        (0, 7),     # Valor neutro (zero)
        (4, 0)      # Divisão por zero
    ]

    expected_results = [
        [7, 3, 10, 2.5],                     # Resultado esperado para valores positivos
        [5, 11, -24, -2.6666666666666665],   # Resultado esperado para valores mesclados
        [7, -7, 0, 0.0],                     # Resultado esperado para valor neutro (zero)
        [4, 4, 0, 'Divisão por zero não é permitida.']  # Resultado esperado para divisão por zero
    ]

    for i, (a, b) in enumerate(test_cases):
        expected_result = expected_results[i]
        result = operacoes_matematicas(a, b)

        if result == expected_result:
            print(f"Test case {i+1}: Passed")
        else:
            print(f"Test case {i+1}: Failed. Expected {expected_result}, but got {result}")

test_operacoes_matematicas()