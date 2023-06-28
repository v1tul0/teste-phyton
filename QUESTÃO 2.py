val1 = float(input("Digite a primeira nota: "))
val2 = float(input("Digite a segunda nota: "))

def operacoes(val1, val2):
    # Soma
    soma = val1 + val2

    # Subtração
    subtracao = val1 - val2

    # Multiplicação
    multiplicacao = val1 * val2

    # Divisão
    if val2 != 0:
        divisao = val1 / val2
    else:
        divisao = None
        if val1 == 0:
            divisao = "indefinido"
        elif val1 > 0:
            divisao = "infinito positivo"
        else:
            divisao = "infinito negativo"

    # Retornar resultados em uma lista
    resultados = [soma, subtracao, multiplicacao, divisao]
    return resultados
valores = operacoes(val1,val2)
print(valores)