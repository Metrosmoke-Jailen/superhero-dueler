from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:
    def __init__(self, name, health=100):
        self.name = name
        self.starting_health = health
        self.current_health = health
        self.abilities = []
        self.armors = []
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        '''Add ability to abilities list'''
        self.abilities.append(ability)

    def add_armor(self, armor):
        '''Add armor to self.armors'''
        self.armors.append(armor)

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount'''
        self.kills += num_kills

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
        '''Battle another hero until one or both are defeated'''

        if self.abilities == [] and opponent.abilities == []:
            print("Draw! Both heroes have no abilities.")
        return

        while self.current_health > 0 and opponent.current_health > 0:
            opponent.take_damage(self.attack())
        self.take_damage(opponent.attack())

        if self.current_health > 0:
            self.add_kill(1)
            opponent.add_death(1)
        elif opponent.current_health > 0:
            opponent.add_kill(1)
            self.add_death(1)
        else:
            # both died
            self.add_death(1)
            opponent.add_death(1)

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