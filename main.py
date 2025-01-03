import os
from random import randint

temas = {
    "Comidas": ["pizza", "tacos", "arroz", "frango", "picles","sopa", "lasanha", "sushi", "batata", "manga"], 
    "Filmes": ["Avatar", "Shrek", "Frozen", "Rocky", "Mulan","Titanic", "Jumanji", "Aladdin", "Cinderela", "Fargo"], 
    "Cidades": ["Paris", "Recife", "Londres", "Tóquio", "Moscou", "Berlim", "Sidney", "Lisboa", "Quito", "Miami"]
}
tema_escolhido = ""

while True:
    for ind, tem in enumerate(temas.keys()):
        print(f"{ind + 1} - {tem}")

    tema_escolhido = int(input("Escolha um tema dentre os disponiveis: "))

    if tema_escolhido in list(range(len(temas.keys()))):
        break
    else:
        print("Tema invalido")

categoria = list(temas.keys())[tema_escolhido - 1]
palavra_secreta = temas[categoria][randint(0, 9)]
chances = 5
letras_jogadas = []
palavra_visivel = "X"*len(palavra_secreta)

while chances > 0:
    os.system('cls||clear')
    print(f"Tema: {categoria}")
    print(f"Chances: {chances}")
    print(f"Letras jogadas: {', '.join(letras_jogadas)}")
    print(palavra_visivel)

    tentativa = input("Tente uma letra: ")

    if len(tentativa) > 1:
        input("SOMENTE LETRAS\nPressione enter para continuar")
        continue

    if tentativa in letras_jogadas:
        input("Letra ja jogada.\nPressione enter para continuar")
        continue
    
    letras_jogadas.append(tentativa)

    if tentativa in palavra_secreta:
        for index, letra in enumerate(palavra_secreta):
            if letra == tentativa:
                aux = list(palavra_visivel)
                aux[index] = letra
                palavra_visivel = ''.join(aux)
    else:
        chances -= 1

    if palavra_secreta == palavra_visivel:
        print("Vitoria")
        print(palavra_visivel)
        break

    if chances == 0:
        print("Derrota");
        print(palavra_secreta)
        break
