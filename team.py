import random

class Team:
    def __init__(self, name):
        '''Initialize your team with its team name and an empty list of heroes'''
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        self.heroes.append(hero)

    def remove_hero(self, name):
        '''
        Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        foundHero = False

        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True

        if not foundHero:
            return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        for hero in self.heroes:
            print(hero.name)
    
    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths:{kd}")

    def revive_heroes(self):
        '''Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        '''Battle each team against each other'''

        living_heroes = self.heroes.copy()
        living_opponents = other_team.heroes.copy()

        while len(living_heroes) > 0 and len(living_opponents) > 0:

            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            hero.fight(opponent)

            if hero.current_health <= 0:
                living_heroes.remove(hero)

            if opponent.current_health <= 0:
                living_opponents.remove(opponent)

if __name__ == "__main__":
    from hero import Hero

    team = Team("Justice Programmers")

    hero1 = Hero("Batman")
    hero2 = Hero("Superman")

    team.add_hero(hero1)
    team.add_hero(hero2)

    team.view_all_heroes()

    team.remove_hero("Batman")

    print("\nAfter removal:")
    team.view_all_heroes()