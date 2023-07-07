valor = 0
lista = []
for i in range(1, 3):
    listateste = []
    nome = input(f"Nome do {i}º Jogador: ")
    listateste.append(nome)
    jogada = input("Impar ou Par: ").upper()
    listateste.append(jogada)
    valor = int(input("Número: "))
    listateste.append(valor)
    lista.append(listateste)

print(lista)