from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        '''Add ability to abilities list'''
        self.abilities.append(ability)

    def add_armor(self, armor):
        '''Add armor to self.armors'''
        self.armors.append(armor)

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)

    def attack(self):
        '''Calculate total damage from all abilities'''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self):
        '''Calculate total block from all armor'''
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        '''Update current_health after applying defense'''
        defense = self.defend()
        damage_taken = damage - defense

        # Prevent negative damage (no accidental healing)
        if damage_taken > 0:
            self.current_health -= damage_taken

    def is_alive(self):
        '''Return True if hero still has health'''
        return self.current_health > 0

    def fight(self, opponent):
        '''Fight opponent until someone wins or draw'''

        # 0) Check if neither hero has abilities
        if not self.abilities and not opponent.abilities:
            print("Draw")
            return

        # 1) Fight loop
        while self.is_alive() and opponent.is_alive():

            # Each hero calculates attack first
            self_damage = self.attack()
            opponent_damage = opponent.attack()

            # Apply damage
            opponent.take_damage(self_damage)
            self.take_damage(opponent_damage)

            # 3) Check outcomes
            if not self.is_alive() and not opponent.is_alive():
                print("Draw")
                return
            elif not opponent.is_alive():
                print(f"{self.name} won!")
                return
            elif not self.is_alive():
                print(f"{opponent.name} won!")
                return


if __name__ == "__main__":

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)

    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)

    hero1.fight(hero2)

    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)

    hero.add_weapon(weapon)
    print(hero.attack())