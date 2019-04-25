import random

class Character():
    def __init__(self, name, health, power):
        self.health = health
        self.power = power
        self.name = name

    def roll_dice(self):
        dice_rolled = int(input("Joker Battle! Enter '1' to take 3 damage.  Enter 0 to roll the dice (possible damage between 1-6"))
        if dice_rolled == 1:
            print("Dice Rolled!")
            return random.randit(1,10)
        elif dice_rolled == 0:
            return 3
        else:
            print("BAD ROLL!  10 DAMAGE!!!")
            return 10

    def attack(self, enemy):
        # Hero does double damanage 1/5 of the time
        pct_20_case = random.randint(1,5)
        pct_10_case = random.randint(1,10)
        if self.name == 'hero': 
            # Hero does double damage 1/5 of the time
            if pct_20_case == 1 and (enemy.name != 'medic' and enemy.name == 'shadow'):
                print(f"The {self.name} does DOUBLE DAMAGE [{self.power*2}] to the {enemy.name}")
                enemy.health -= (self.power)*2
            # Shadow skips damage 1/10 of the time
            elif pct_10_case > 1 and enemy.name == 'shadow':
                print(f"The {self.name} attacked the {enemy.name}, but the {enemy.name} is elusive.")
                print(f'No Damage done!')
            # Medic healts themselves with 2 points 1/5 of the time
            elif enemy.name == 'medic' and pct_20_case == 1:
                enemy.health -= self.power
                print("The {} does {} damage to the {}.".format(self.name, self.power, enemy.name))
                print(f"***BUT WAIT!, the {enemy.name} restores 2 health points!***")
                enemy.health = enemy.health + 2
                print(f"The {enemy.name} health is not {enemy.health}")
            # Not a special case
            else:
                enemy.health -= self.power
                print("The {} does {} damage to the {}.".format(self.name, self.power, enemy.name))
        elif self.name == 'joker':
            damage = self.roll_dice()
            enemy.health -= damage
            print("The {} does {} damage to the {}.".format(self.name, damage, enemy.name))
        elif self.name == 'eagle':
            print("Eagle flies high and slaps the hero with both wings.")
            enemy.health -= (self.power)
        elif self.name == 'yourself':
            print(f"Fighting Yourself!  You win... and lose... DEATH!!!")
            enemy.health -= 1000000
        else:
            enemy.health -= self.power
            print("The {} does {} damage to the {}.".format(self.name, self.power, enemy.name))
           
        # If enemy has no more health
        if enemy.health <= 0 and enemy.name != "zombie":
            print(f"The {enemy.name} is dead.")
        elif enemy.health <= 0 and enemy.name == 'zombie':
            print(f"The {enemy.name} has {enemy.health} but is still fighting!!!!")

    def alive(self):
        if self.health >0:
            return True
        else:
            return False

    def print_status(self):
        print(f"Current health of the {self.name} = {self.health}")

    

# Initialize Characters
goblin = Character('goblin', 6, 2)
hero = Character('hero', 10, 5)
zombie = Character('zombie', 1000000, 1000000)
medic = Character('medic', 10, 10)
shadow = Character('shadow', 1, 2)
joker = Character('joker',10,10)
eagle = Character('eagle',6,4)
yourself = Character('yourself',100,100)


print("-----------------")
print("YOU ARE THE HERO!")
print("-----------------")
while (goblin.alive() or medic.alive() or shadow.alive() or joker.alive() or eagle.alive() or yourself.alive()) and hero.alive():
    print("-------------------------------------")
    print("The hero has {} health and {} power.".format(hero.health, hero.power))
    print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
    print("The zombie has {} health and {} power.".format(zombie.health, zombie.power))
    print("The medic has {} health and {} power.".format(medic.health, medic.power))
    print("The shadow has {} health and {} power.".format(shadow.health, shadow.power))
    print("The joker has {} health and {} power.".format(joker.health, joker.power))
    print("The eagle has {} health and {} power.".format(eagle.health, eagle.power))
    print("Yourself has {} health and {} power.".format(yourself.health, yourself.power))

    print("-------------------------------------")
    print('-----------------------')
    print("What do you want to do?")
    print('-----------------------')
    print("1. fight goblin")
    print("2. fight zombie")
    print("3. fight medic")
    print("4. fight shadow")
    print("5. fight joker")
    print("6. fight eagle")
    print("7, fight yourself")
    print("8. do nothing")
    print("9. flee")
    print("> ", end=' ')
    raw_input = input()


    if raw_input == "1":
        hero.attack(goblin) 
        if goblin.health > 0:
            goblin.attack(hero)
    elif raw_input == "2":
        hero.attack(zombie) 
        zombie.attack(hero)                  
    elif raw_input == "3":
        hero.attack(medic) 
        if medic.health > 0:
            medic.attack(hero)
    elif raw_input == "4":
        hero.attack(shadow) 
        if shadow.health > 0:
            shadow.attack(hero)
    elif raw_input == "5":
        hero.attack(joker) 
        if joker.health > 0:
            joker.attack(hero)
    elif raw_input == "6":
        hero.attack(eagle) 
        if eagle.health > 0:
            eagle.attack(hero)
    elif raw_input == "7":
        hero.attack(yourself) 
        if yourself.health > 0:
            yourself.attack(hero)
    elif raw_input == "8":
        pass
    elif raw_input == "9":
        print("Goodbye.")
        break
    else:
        print("Invalid input {}".format(raw_input))
