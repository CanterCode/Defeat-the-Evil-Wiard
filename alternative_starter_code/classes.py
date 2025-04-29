import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health

    def attack(self, opponent):
        damage = random.randint(5, self.attack_power)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
            
    def heal(self):
        heal_amount = random.randint(3, 15)
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals for {heal_amount} health! Current health: {self.health}")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
        

# Warrior/Mage/Archer/Paladin classes (inherits from Character)
class Barbarian(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20)
        
    def special_ability(self, opponent):
        print("\nSpecial Abilities:")
        print("1. Rage Fury - Unleashes a ferocious attack, dealing double damage")
        print("2. War Cry - Initimidates enemy, reducing their attack power for one turn.")
        
        action = input("Which ability would you like to use? (1 or 2): ")
        
        if action =="1":
            pass
        elif action == "2":
            pass
        else:
            print("Invalid choice. Try again.")

class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=25)
        
    def special_ability(self, opponent):
        print("\nSpecial Abilities:")
        print("1. Backstab - Deals massive damage from behind, catching the enemy off gaurd.")
        print("2. Evasive Flip - Performs lightning-fast roll to dodge next attack, reducing damage.")

class Ranger(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=25)
        
    def special_ability(self, opponent):
        print("\nSpecial Abilities:")
        print("1. Arrow Barrage - Fires multiple arrows at once, dealing increased damage.")
        print("2. Nature's Shield - Defend against the next attack and gain a slight health boost.")
        
class Sorcerer(Character):
    def __init__(self, name):
        super().__init__(name, health=90, attack_power=30)
        
    def special_ability(self, opponent):
        print("\nSpecial Abilities:")
        print("1. Fireball - Launches a powerful fireball, dealing double damage.")
        print("2. Magic Shield - Blocks some incoming damage using magical protection.")

class Bard(Character):
    def __init__(self, name):
        super().__init__(name, health=85, attack_power=30)
        
    def special_ability(self, opponent):
        print("\nSpecial Abilities:")
        print("1. Heroic Call - Summons nearby allies to aid in battle, increasing attack power for one turn.")
        print("2. Healing Song - Sings a soothing melody, increasing health by a small amount.")

     
# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=20)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")