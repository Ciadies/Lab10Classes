'''
Created on Dec. 21, 2023

@author: sebbe
'''
from copy import deepcopy

lista = [[0,0,0],[1,1,1],[2,2,2]]
listb= lista
listc = lista[:]
listd = deepcopy(lista)

lista[2] = [4,5,6]
listb[2][0] = 10
listc[0][0] = -1

print(lista,listb,listc,listd)