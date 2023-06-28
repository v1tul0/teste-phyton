def calcular_conceito(nota1, nota2, nota3):
    if 0 <= nota1 <= 100 and 0 <= nota2 <= 100 and 0 <= nota3 <= 100:
        media = (nota1 + nota2 + nota3) / 3
        if media < 50:
            return "D"
        elif media < 70:
            return "C"
        elif media < 90:
            return "B"
        else:
            return "A"
    else:
        return "NULO"

# Exemplo de uso
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

conceito = calcular_conceito(nota1, nota2, nota3)
print("Conceito: ", conceito)