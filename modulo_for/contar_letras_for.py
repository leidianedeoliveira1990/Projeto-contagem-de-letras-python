def contar_letras(texto):
    frequencia = {}

    for letra in texto.lower():
        if letra.isalpha():
            frequencia[letra] = frequencia.get(letra, 0) + 1

    return frequencia


texto = input("Digite um texto: ")

resultado = contar_letras(texto)

print("Frequência das letras:")

for letra, quantidade in resultado.items():
    print(letra, ":", quantidade)
