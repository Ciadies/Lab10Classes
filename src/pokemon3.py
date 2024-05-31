'''
Created on Dec. 7, 2023
Simple pokemon battle script
@author: Sebastian
'''
from Pokemon import Pokemon
import random

def read_pokemon_from_file(filename):
    '''
    read a list of pokemon from a file
    '''
    file = open(filename,"r",encoding="utf-8")
    list = file.readlines()
    pokelist = []
    for i in range(1,len(list)): #exclude the first line
        split = list[i].split("|")
        pokemon = Pokemon(split[0], int(split[1]), int(split[2]), int(split[3]), int(split[3]))
        pokelist.append(pokemon)
    return pokelist
    
def main():
    """
    Battle of two Pokemon
    """
    pokelist = read_pokemon_from_file("all_pokemon.txt")
    pokemon1 = pokelist[random.randint(0,800)]
    pokemon2 = pokelist[random.randint(0,800)]
    while True:
        if pokemon1 != pokemon2 :
            print(f"Welcome, {pokemon1} and {pokemon2}!")
            break
        pokemon2 = pokelist[random.randint(0,800)]

if __name__ == "__main__" :
    main()