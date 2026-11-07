def contar_letras(texto):
    frequencia = {}
    texto = texto.lower()
    i = 0

    while i < len(texto):
        letra = texto[i]

        if letra.isalpha():
            frequencia[letra] = frequencia.get(letra, 0) + 1

        i += 1

    return frequencia


texto = input("Digite um texto: ")

resultado = contar_letras(texto)

print("Frequência das letras:")

for letra, quantidade in resultado.items():
    print(letra, ":", quantidade)
