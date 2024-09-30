# -*- coding: utf-8 -*-
"""
Programa que ordena os dados de alunos lidos de um arquivo texto. 
A ordenação é realizada por variados atributos (nome, RA, idade, curso).
Cada tipo de ordenação é feita por um dos métodos estudados: bubbleSort,
inserctionSort, selectionSort e quickSort.
Created on Fri Sep  6 10:23:43 2024
@author1: Ivan Carlos Alcântara de Oliveira
"""
# importação dos métodos de ordenação utilizados
# e que se encontram no arquivo ordenacao.py
# os métodos devem ser modificados para realizar as ordenações
# solicitadas
from ordenacao import selectionSort
from ordenacao import bubbleSort
from ordenacao import quickSort
from ordenacao import insertionSort

# leArquivo: método encarregado de ler e retornar os dados dos alunos: nome, RA, 
#            idade e curso e armazená-los em um vetor, no qual cada
#            posição representa um aluno.
# Parâmetros: nome do arquivo: nome do arquivo do tipo texto a ser lido.
#             O arquivo deve conter os dados nome, RA, idade e curso de alunos,
#             sendo um por linha.
def leArquivo(nomeArquivo):
    nomeAluno, RA, idade, siglaCurso = list(), list(), list(), list()
    with open(nomeArquivo,'r') as manip:
       for linha in manip:
           dados = linha.split(',')
           nomeAluno.append(dados[0])
           RA.append(dados[1])
           idade.append(dados[2])
           siglaCurso.append(dados[3].rstrip('\n'))
    return nomeAluno, RA, idade, siglaCurso

# imprimeDadosAluno: método que os dados dos alunos: nome, RA, idade e curso. 
#                    Todos os dados são armazenados em um vetor, no qual cada
#                    posição representa um aluno.
# Parâmetros: mensagem: texto com o tipo de ordenação dos dados.
#             nomeAluno: vetor com nome de alunos
#             RA: vetor contendo o RA dos alunos
#             idade: vetor com as idades dos alunos
#             curso: vetor contendo as siglas dos cursos
def imprimeDadosAluno(mensagem, nomeAluno, RA, idade, curso):
    print(mensagem)
    print("Nome         RA          idade  siglaCurso")
    for i in range(len(nomeAluno)):
        print(f"{nomeAluno[i]:10s} {RA[i]:10s}      {idade[i]:3s}      {curso[i]:8s}")  
        
# principal: método responsável por chamar os métodos de 
#            leitura dos dados, ordenação e impressão na tela.
def principal():
    # Leitura de dados do arquivo
    nomeAluno, RA, idade, curso = leArquivo('dadosAlunos.csv')
    # Ordena pelo nome do aluno método da Seleção Direta
    selectionSort(nomeAluno, RA, idade, curso)
    imprimeDadosAluno("Alunos ordenados pelo Nome:", nomeAluno, RA, idade, curso)
    # Ordena pelo RA do aluno método mergeSort
    insertionSort(nomeAluno, RA, idade, curso)
    imprimeDadosAluno("Alunos ordenados pelo RA:", nomeAluno, RA, idade, curso)
    # Ordena pela idade do aluno método da bolha
    bubbleSort(nomeAluno, RA, idade, curso)
    imprimeDadosAluno("Alunos ordenados pela idade:", nomeAluno, RA, idade, curso)
    # Ordena pelo nome do aluno método quicksort
    quickSort(nomeAluno, RA, idade, curso)
    imprimeDadosAluno("Alunos ordenados pelo curso:",nomeAluno, RA, idade, curso)
    
# chamada do método responsável por executar todas as 
# funcionalidades do programa
principal()