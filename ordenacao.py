# -*- coding: utf-8 -*-
"""
Biblioteca contendo os métodos de ordenação:
    inserctionSort, SelectionSort, BubbleSort, MergeSort e QuickSort.
Todos devem realizar a ordenação de dados de alunos por algum critério, 
por exemplo, nome, RA, idade ou curso.
Cada um dos métodos deve ser modificado, a partir do estudado na teoria da 
aula.
Created on Fri Sep  6 12:21:41 2024
@author1: Ivan Carlos Alcântara de Oliveira
@author2 : Thais Jorge Azevedo
Data da atualização: 30/09/2024
"""
# selectionSort: realiza a ordenação pelo nome do aluno 
#                considerando como método a seleção direta
# Parâmetros: nomeAluno: vetor de nome de alunos
#             RA: vetor com os registros acadêmicos dos alunos
#             idade: vetor com as idades dos alunos
#             curso: vetor com o curso dos alunos 
def selectionSort(nomeAluno, RA, idade, curso):
    n = len(nomeAluno)
    # Percorre cada elemento do vetor nomeAluno
    for i in range(n):
        # Assume que o menor elemento é o atual
        min_idx = i
        # Encontra o menor nome no restante do vetor
        for j in range(i+1, n):
            if nomeAluno[j] < nomeAluno[min_idx]:
                min_idx = j
        # Troca o menor nome com o nome atual
        nomeAluno[i], nomeAluno[min_idx] = nomeAluno[min_idx], nomeAluno[i]
        # Faz a troca correspondente nos outros vetores
        RA[i], RA[min_idx] = RA[min_idx], RA[i]
        idade[i], idade[min_idx] = idade[min_idx], idade[i]
        curso[i], curso[min_idx] = curso[min_idx], curso[i]
    return nomeAluno, RA, idade, curso

# bubleSort: realiza a ordenação pela idade do aluno 
#            considerando como método bublleSort
# Parâmetros: nomeAluno: vetor de nome de alunos
#             RA: vetor com os registros acadêmicos dos alunos
#             idade: vetor com as idades dos alunos
#             curso: vetor com o curso dos alunos 
def bubbleSort(nomeAluno, RA, idade, curso):
    n = len(idade)
    # Percorre o vetor várias vezes
    for i in range(n):
        # Últimos i elementos já estão na posição correta
        for j in range(0, n-i-1):
            # Se a idade atual é maior que a próxima, faz a troca
            if idade[j] > idade[j+1]:
                # Troca as idades
                idade[j], idade[j+1] = idade[j+1], idade[j]
                # Troca os dados correspondentes
                nomeAluno[j], nomeAluno[j+1] = nomeAluno[j+1], nomeAluno[j]
                RA[j], RA[j+1] = RA[j+1], RA[j]
                curso[j], curso[j+1] = curso[j+1], curso[j]
    return nomeAluno, RA, idade, curso

# insertionSort: realiza a ordenação pelo RA do aluno 
#            considerando como método inserção direta
# Parâmetros: nomeAluno: vetor de nome de alunos
#             RA: vetor com os registros acadêmicos dos alunos
#             idade: vetor com as idades dos alunos
#             curso: vetor com o curso dos alunos 
def insertionSort(nomeAluno, RA, idade, curso):
    n = len(RA)
    # Percorre cada elemento do vetor a partir do segundo
    for i in range(1, n):
        key_RA = RA[i]
        key_nome = nomeAluno[i]
        key_idade = idade[i]
        key_curso = curso[i]

        # Move elementos de RA[0..i-1], que são maiores que o RA atual, para uma posição à frente
        j = i - 1
        while j >= 0 and RA[j] > key_RA:
            RA[j + 1] = RA[j]
            nomeAluno[j + 1] = nomeAluno[j]
            idade[j + 1] = idade[j]
            curso[j + 1] = curso[j]
            j -= 1
        
        # Coloca o RA atual na posição correta
        RA[j + 1] = key_RA
        nomeAluno[j + 1] = key_nome
        idade[j + 1] = key_idade
        curso[j + 1] = key_curso
    
    return nomeAluno, RA, idade, curso


# quickSort: realiza a ordenação pelo curso do aluno 
#            considerando como método quickSort
# Parâmetros: nomeAluno: vetor de nome de alunos
#             RA: vetor com os registros acadêmicos dos alunos
#             idade: vetor com as idades dos alunos
#             curso: vetor com o curso dos alunos 
def quickSort(nomeAluno, RA, idade, curso, low=0, high=None):
    if high is None:
        high = len(curso) - 1
    
    if low < high:
        # Encontra o índice do pivô
        pi = partition(nomeAluno, RA, idade, curso, low, high)
        # Ordena recursivamente os elementos antes e depois do pivô
        quickSort(nomeAluno, RA, idade, curso, low, pi - 1)
        quickSort(nomeAluno, RA, idade, curso, pi + 1, high)
    
    return nomeAluno, RA, idade, curso

def partition(nomeAluno, RA, idade, curso, low, high):
    # Escolhe o último elemento como pivô
    pivot = curso[high]
    i = low - 1  # Índice do menor elemento
    
    for j in range(low, high):
        # Se o elemento atual é menor ou igual ao pivô
        if curso[j] <= pivot:
            i += 1
            # Faz a troca dos elementos no vetor curso
            curso[i], curso[j] = curso[j], curso[i]
            # Troca correspondente nos outros vetores
            nomeAluno[i], nomeAluno[j] = nomeAluno[j], nomeAluno[i]
            RA[i], RA[j] = RA[j], RA[i]
            idade[i], idade[j] = idade[j], idade[i]
    
    # Coloca o pivô na posição correta
    curso[i + 1], curso[high] = curso[high], curso[i + 1]
    # Faz a troca correspondente nos outros vetores
    nomeAluno[i + 1], nomeAluno[high] = nomeAluno[high], nomeAluno[i + 1]
    RA[i + 1], RA[high] = RA[high], RA[i + 1]
    idade[i + 1], idade[high] = idade[high], idade[i + 1]
    
    return i + 1
