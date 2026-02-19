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