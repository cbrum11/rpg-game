class Character():
    def __init__(self, name, health, power):
        self.health = health
        self.power = power
        self.name = name

    def attack(self, enemy):
        enemy.health -= self.power
        print("The {} does {} damage to the {}.".format(self.name, self.power, enemy.name))
        if enemy.health <= 0:
            print(f"The {enemy.name} is dead.")

    def alive(self):
        if self.health >=0:
            return True
        else:
            return False

    def print_status(self):
        print(f"Current health of the {self.name} = {self.health}")

# Initialize Characters
goblin = Character('goblin', 6, 2)
hero = Character('hero', 10, 5)
zombie = Character('zombie', 1000000, 1000000)

while goblin.alive() and hero.alive():
    print("You have {} health and {} power.".format(hero.health, hero.power))
    print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
    print("The zombie has {} health and {} power.".format(zombie.health, zombie.power))
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("4. fight zombie")
    print("> ", end=' ')
    raw_input = input()
    if raw_input == "1":
        hero.attack(goblin)            
    elif raw_input == "2":
        pass
    elif raw_input == "3":
        print("Goodbye.")
        break
    elif raw_input == "4":
        hero.attack(zombie)
        zombie_fg = True # Skip goblin once
    else:
        print("Invalid input {}".format(raw_input))

    if goblin.health > 0 and zombie_fg == False:
        goblin.attack(hero)
    else:
        zombie.attack(hero)
        zombie_fg == False
    