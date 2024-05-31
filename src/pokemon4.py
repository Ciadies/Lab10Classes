'''
Created on Dec. 7, 2023
Fully fledged pokemon battle script
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
    while True: #ensure battle between diffferent mons
        if pokemon1 != pokemon2 :
            print(f"Welcome, {pokemon1} and {pokemon2}!")
            break
        pokemon2 = pokelist[random.randint(0,800)]
    
    round = 0
    turn = 1
    while pokemon1.is_alive() and pokemon2.is_alive():
        if round >= 10 :
            pokemon1.lose_health(pokemon1.current_health)
            pokemon2.lose_health(pokemon2.current_health)
            break
        print(f"\nRound {round+1} Begins")
        
        if turn == 1:#pokemon1 turn to attack
            pokemon1.attempt_attack(pokemon2)
            turn = 2
        else:
            pokemon2.attempt_attack(pokemon1)
            turn = 1
            
        round += 1 # increase the round counter
        
        if not pokemon1.is_alive() and random.choice([True,False]) :
            pokemon1.revive()
        if not pokemon2.is_alive() and random.choice([True,False]) :
            pokemon2.revive()  
    
    if pokemon1.is_alive():
        print(f"{pokemon1} has won in {round} rounds")
    elif pokemon2.is_alive():
        print(f"{pokemon2} has won in {round} rounds")
    else: 
        print("The match has ended in a draw after 10 rounds")
                
if __name__ == "__main__" :
    main()