from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team


class Arena:
    def __init__(self):
        '''Instantiate properties: team_one and team_two'''
        self.team_one = Team("Team One")
        self.team_two = Team("Team Two")

    # ---------- Creation Helpers ----------

    def create_ability(self):
        '''Prompt for Ability information and return Ability object'''
        name = input("What is the ability name? ")
        max_damage = int(input("What is the max damage of the ability? "))
        return Ability(name, max_damage)

    def create_weapon(self):
        '''Prompt for Weapon information and return Weapon object'''
        name = input("What is the weapon name? ")
        max_damage = int(input("What is the max damage of the weapon? "))
        return Weapon(name, max_damage)

    def create_armor(self):
        '''Prompt for Armor information and return Armor object'''
        name = input("What is the armor name? ")
        max_block = int(input("What is the max block of the armor? "))
        return Armor(name, max_block)

    def create_hero(self):
        '''Prompt user for Hero information and return Hero object'''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)

        add_item = None
        while add_item != "4":
            add_item = input(
                "\n[1] Add ability\n"
                "[2] Add weapon\n"
                "[3] Add armor\n"
                "[4] Done adding items\n\n"
                "Your choice: "
            )

            if add_item == "1":
                ability = self.create_ability()
                hero.add_ability(ability)

            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)

            elif add_item == "3":
                armor = self.create_armor()
                hero.add_armor(armor)

        return hero

    # ---------- Team Builders ----------

    def build_team_one(self):
        '''Prompt user to build team_one'''
        num = int(input("How many members would you like on Team One?\n"))
        for _ in range(num):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        '''Prompt user to build team_two'''
        num = int(input("How many members would you like on Team Two?\n"))
        for _ in range(num):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    # ---------- Battle ----------

    def team_battle(self):
        '''Battle team_one and team_two'''
        self.team_one.attack(self.team_two)

    # ---------- Statistics ----------

    def show_stats(self):
        '''Print battle statistics'''

        print("\n================ ARENA RESULTS ================\n")

        print(self.team_one.name + " statistics:")
        self.team_one.stats()
        print("\n")

        print(self.team_two.name + " statistics:")
        self.team_two.stats()
        print("\n")

        # Average K/D Team One
        team_one_kills = sum(hero.kills for hero in self.team_one.heroes)
        team_one_deaths = sum(hero.deaths for hero in self.team_one.heroes) or 1
        print(self.team_one.name + " average K/D: " +
              str(team_one_kills / team_one_deaths))

        # Average K/D Team Two
        team_two_kills = sum(hero.kills for hero in self.team_two.heroes)
        team_two_deaths = sum(hero.deaths for hero in self.team_two.heroes) or 1
        print(self.team_two.name + " average K/D: " +
              str(team_two_kills / team_two_deaths))

        print("\nSurvivors:")

        team_one_alive = 0
        for hero in self.team_one.heroes:
            if hero.is_alive():
                print("Survived from " + self.team_one.name + ": " + hero.name)
                team_one_alive += 1

        team_two_alive = 0
        for hero in self.team_two.heroes:
            if hero.is_alive():
                print("Survived from " + self.team_two.name + ": " + hero.name)
                team_two_alive += 1

        print("\nWinner:")

        if team_one_alive > team_two_alive:
            print(self.team_one.name + " wins! 🏆")
        elif team_two_alive > team_one_alive:
            print(self.team_two.name + " wins! 🏆")
        else:
            print("It's a draw! ⚖️")

if __name__ == "__main__":
    game_is_running = True

    arena = Arena()

    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:
        arena.team_battle()
        arena.show_stats()

        play_again = input("\nPlay Again? Y or N: ")

        if play_again.lower() == "n":
            game_is_running = False
        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
