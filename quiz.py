# -*- coding: utf-8 -*-
import os
import json
import random

path = "C:\\Users\\Documents\\python" #caminho arquivo json
files = os.listdir(path)

perguntas = None
pontos = 0

arquivo = open('ranking.txt','r')
maiores_pontuacoes = arquivo.readlines()

for file in files:
    if file == "quiz.json":
        with open(path + "/" +file, encoding='utf8') as data_file:
            perguntas = json.load(data_file)
            
p_lidas = [i for i in range(1,len(perguntas)+1)]

print('='*60)
print('Quiz muito criativo'.center(60))
print('='*60)
while True:
    print('O que você deseja fazer com esse quiz totalmente aleatório?')
    op = input('1 - Jogar\n2 - Ver ranking\n0 - Fechar\n')
    if op == '1':
        print('=' * 60)
        while len(p_lidas) > 0:
            n_p = random.choice(p_lidas)
            p_lidas.remove(n_p)
            print((perguntas[str(n_p)]['pergunta']))
            resposta = input(perguntas[str(n_p)]['itens'] + '\n')

            if resposta == perguntas[str(n_p)]['correto']:
                print('acertou\n')
                pontos += 1
            else:
                print('errou\n')
                break
        if int(min(maiores_pontuacoes).split(' ')[0]) < pontos:
            print("Você entrou para o ranking!!")
            nome = input("Digite seu nome: ")
            maiores_pontuacoes.pop()
            maiores_pontuacoes.append(str(pontos) + ' ' + nome + '\n')
            maiores_pontuacoes.sort(reverse=True)
        print('\n== ranking ==\n')

        for i in maiores_pontuacoes:
            print(i)
        print('=' * 60)

        arquivo = open('ranking.txt', 'w')
        arquivo.writelines(maiores_pontuacoes)

        arquivo.close()

    elif op == '2':
        print('\n== ranking ==\n')
        for i in maiores_pontuacoes:
            print(i)
        print('=' * 60)
        continue

    elif op == '0':
        print('=' * 60)
        break

    else:
        print("Opção invalida!")
        print('=' * 60)
        continue




