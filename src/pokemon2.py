'''
Created on Dec. 7, 2023
Simple pokemon battle script
@author: Sebastian
'''
from Pokemon import Pokemon

def main():
    """
    Battle of two Pokemon
    """
    pokemon1 = Pokemon("Pikachu", 55, 40, 35, 35)
    pokemon2 = Pokemon("Bulbasaur", 49, 49, 45, 45)
    print(f"Welcome, {pokemon1} and {pokemon2}!")

if __name__ == "__main__" :
    main()