class Hero():
    def __init__(self, health, pohwer):
    self.health = health
    self.power = power
    self.name = "Hero"

    def attack(enemy):
        enemy.health -= self.power
        print("You do {} damage to the goblin.".format(self.power))
        if enemy.health <= 0:
            print(f"The {enemy.name} is dead.")


class Goblin():
    def __init__(self, health, pohwer):
    self.health = health
    self.power = power
    self.name = "Goblin"

goblin = Goblin(6,2)
hero = Hero(10,5)

while goblin.health > 0 and hero.health > 0:
    print("You have {} health and {} power.".format(hero.health, hero.power))
    print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
    print()
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ", end=' ')
    raw_input = input()
    if raw_input == "1":
            hero.attack(goblin)            
    elif raw_input == "2":
        pass
    elif raw_input == "3":
        print("Goodbye.")
        break
    else:
        print("Invalid input {}".format(raw_input))