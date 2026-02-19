import random

class Hero:
  def __init__(self, name, starting_health=100):
    '''Instance properties:
      name: String
      starting_health: Integer
      current_health: Integer
    '''

    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health

  def fight(self, opponent):
        '''Current Hero will take turns fighting the opponent hero passed in.'''

        winner = random.choice([self, opponent])
        loser = opponent if winner == self else self

        print(f"{winner.name} defeats {loser.name}!")
        return winner


if __name__ == "__main__":
  my_hero = Hero("Grace Hopper", 200)
  print(my_hero.name)
  print(my_hero.current_health)

  print("\n--- Battle Test ---")

  hero1 = Hero("Wonder Woman")
  hero2 = Hero("Dumbledore")

  hero1.fight(hero2)