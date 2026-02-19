import random

class Ability:
    def __init__(self, name, max_damage):
        '''
        Initialize the values passed into this
        method as instance variables.

        name: String
        max_damage: Integer
        '''
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        '''Return a value between 0 and the value set by self.max_damage.'''
        return random.randint(0, self.max_damage)


if __name__ == "__main__":
    # Test code
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())