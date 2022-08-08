import math
import json
import os
import sys

def carregarJson():
    with open('alunos.json', 'r') as file:
        alunos = json.load(file)
        return alunos

class App:
    def __init__(self):
        self.alunos = carregarJson()
        self.app = True
    
    def menu(self):
        print("-----MENU-----")
        print("1 - ver notas")
        print("2 - adicionar nota")
        print("3 - editar nota")
        print("4 - deletar aluno")
        print("5 - sair")
        
    def limpar(self):
        myos = sys.platform
        if myos == "win32":
            os.system('cls')
        elif myos == "linux":
            os.system('clear')

    def verNotas(self):
        print("--------------")
        for i in self.alunos:
            print(f"nome: {i['nome']}\nnotas:")
            media = 0
            for e in i['notas']:
                print(i['notas'][i['notas'].index(e)])
                media += e
            media = math.floor(media/3)
            print(f"media: {media}\n--------------")
        input("ok? ")

    def adicionarNota(self):
        nome = input("nome do aluno: ")
        notas = []
        dicionario = {}
        if(len(self.alunos) != 0):
            for e in self.alunos:
                if e['nome'] == nome:
                    print("já existe alguém com esse nome")
                    input("ok? ")
                    return
                else:
                    if(len(notas) == 0):
                        print("notas: ")
                        for i in range(3):
                            nota = float(input())
                            if nota>=0 and nota<=10:
                                notas.append(nota)
                                dicionario = {
                                    "nome": nome,
                                    "notas": notas
                                }
                            else:
                                print('burro')
                                input("ok? ")
                                return
        else:
            print("notas: ")
            for i in range(3):
                nota = float(input())
                if nota>=0 and nota<=10:
                    notas.append(nota)
                    dicionario = {
                        "nome": nome,
                        "notas": notas
                    }
                else:
                    print('burro')
                    input("ok? ")
                    return  
        self.alunos.append(dicionario)
        with open('alunos.json', 'w') as file:
            json.dump(self.alunos, file)
        input("ok? ")
    
    def editarNota(self):
        aluno = input("nome do aluno: ")
        for i in self.alunos:
            if aluno == i['nome']:
                nNota = input("editar qual nota?(1,2,3) ")
                if nNota == "1" or nNota == "2" or nNota == "3":
                    nNota = int(nNota)-1
                    nota = int(input('por qual? '))
                    self.alunos[self.alunos.index(i)]['notas'][nNota] = nota
                    with open('alunos.json', 'w') as file:
                        json.dump(self.alunos, file)
                else:
                    return
            else:
                return
        input("ok? ")
        
    def deletarAluno(self):
        aluno = input("nome do aluno: ")
        for i in self.alunos:
            if aluno == i['nome']:
                self.alunos.pop(self.alunos.index(i))
        with open('alunos.json', 'w') as file:
            json.dump(self.alunos, file)
        input("ok? ")