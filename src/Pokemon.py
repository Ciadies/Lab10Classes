'''
Created on Dec. 7, 2023
Pokemon class 
@author: Sebastian
'''
import random

class Pokemon: 
    '''
    an object in this class represents a single pokemon
    a method represents the components to battle
    '''
    def __init__(self, name, attack, defence, max_health, current_health):
        '''
        initialize the stats of the pokemon
        '''
        self.name = name
        self.attack = attack
        self.defense = defence
        self.max_health = max_health
        self.current_health = current_health
    
    def __str__(self):
        '''
        Return a string format of the pokemon
        eg. Pikachu with 35/35 health will return
        Pikachu (health: 35/35)
        '''
        return f"{self.name} (health: {self.current_health}/{self.max_health})"
    
    def lose_health(self, amount):
        '''
        Reduces current health by a specified amount
        if the amount is negative nothing happens, if the amount is >= current health, the current health is set to 0
        otherwise it's simply substracted
        '''
        if amount > 0:
            if amount <= self.current_health:
                self.current_health += -amount
            else:
                self.current_health = 0
    
    def is_alive(self):
        '''
        Checks if the pokemon has greater than 0 health in which case it returns True
        '''
        if self.current_health > 0:
            return True
        return False
    
    def revive(self):
        '''
        Sets current health to maximum
        '''
        self.current_health = self.max_health
        print(f"{self.name} has been revived!")

    def attempt_attack(self, foe):
        '''
        Attempt to make an attack
        '''
        modifier = random.choice([0.7,0.8,0.9,1.0,1.1,1.2,1.3])
        damage = round(self.attack * modifier)
        print(f"{self.name} attack {foe.name} for {damage} damage")
        if damage > foe.defense:
            foe.lose_health(damage-foe.defense)
            print(f"Attack was successful! {foe.name} has {foe.current_health} health remaining")
        else :
            print("Attack was blocked")
        
        