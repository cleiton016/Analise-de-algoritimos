import time
import timeit

def ler_arquivo(nome):
    arq = open(nome, 'r')
    conteudo = arq.read()
    r = conteudo.split('\n')
    arq.close()
    return r

def acha_numero(lista):
    n = lista[0]
    conjunto = lista[2:-1]
    for i in conjunto:
        if i == n:
            return (True,conjunto.index(i))

    return (False, -1)

#########################################
arquivos = ['dataset-1-a.csv','dataset-1-b.csv','dataset-1-c.csv']

for i in arquivos:

    inicio = timeit.default_timer()
    saida = acha_numero(ler_arquivo(i))
    fim = timeit.default_timer()

    novo_arq = open('resposta-'+i, 'w')
    novo_arq.write(
    str(saida[0])+'\n'+
    str(saida[1])+'\n'+
    str(fim-inicio))
    novo_arq.close()