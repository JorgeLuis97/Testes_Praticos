def verificar(strings):
    for i in range(1, len(strings)):
        if strings[i] < strings[i-1]:
            return False
    return True

strings = []
for i in range(4):
    entrada = input("Digite uma string: ")
    strings.append(entrada)

resultado = verificar(strings)
print(strings)
print(f"O resultado é {resultado}")