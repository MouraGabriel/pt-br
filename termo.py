# Gabriel Moura
# 2022.03.19

# Implementação em tkinter do jogo term.ooo em pt-br


from copy import deepcopy
from tkinter import *
from random import randint


tamanho = 5
file = "filetest"
files = [
	"conjugações", 
	"dicio", 
	"palavras", 
	"verbos"
]


def filterWordlist(file: str) -> list:
	"Filtra as palavras de dado tamanho e as organiza."
	f = open(file, "r")
	fileList = f.read()
	f.close()
	fileList = fileList.split("\n")
	lista = []
	for w in fileList:
		if len(w) == tamanho: 
			lista += [w]
	return lista

def listWordlist(files) -> list:
	"Ordena e lista as palavras de uma lista de arquivos."
	lista = []
	for file in files:
		lista += filterWordlist(file)
	lista.sort()
	lista = list(dict.fromkeys(lista))
	return lista

def sortWordlist(files: list) -> None:
	"Sorteia uma palavra de uma lista de arquivos."
	lista = listWordlist(files)
	palavra = lista[randint(0, len(lista) - 1)]
	print(palavra)
	return(palavra)

def freqWordlist(files) -> list:
	"Retorna a frequência de letras em casa posição."
	lista = listWordlist(files)
	freqList = []
	for posicao in range(tamanho):
		freq = dict()
		for letra in "abcdefghijklmnopqrstuvwxyz":
			freq[letra] = 0
		for palavra in lista:
			for letra in "abcdefghijklmnopqrstuvwxyz":
				if palavra[posicao] == letra:
					freq[letra] += 1
					if letra == "y": print(palavra)
		freqList.append(deepcopy(freq))
	return freqList

class gui:
	def __init__(self) -> None:
		self.interface()

	def interface(self) -> None:
		"Interface gráfica."
		self.jogo = Tk()
		
		self.jogo.frame = Frame(self.jogo)
		
		self.jogo.mainloop()
