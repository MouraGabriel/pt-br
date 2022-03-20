# Gabriel Moura
# 2022.03.19

# Implementação em tkinter do jogo term.ooo em pt-br


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

