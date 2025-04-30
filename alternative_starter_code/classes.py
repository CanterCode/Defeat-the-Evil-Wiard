import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.defensive_mode = False

    def receive_attack(self, damage):
        if self.defensive_mode:
            damage = int(damage / 2)
            self.defensive_mode = False

        self.health -= damage
        if self.health < 0:
            self.health = 0

        print(f"{self.name} receives {damage} damage! Current health: {self.health}")

    def attack(self, opponent):
        damage = random.randint(5, self.attack_power)
        print(f"\n{self.name} attacks {opponent.name} for {damage} damage!")
        opponent.receive_attack(damage)
            
    def heal(self):
        heal_amount = random.randint(5, 15)
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals for {heal_amount} health! Current health: {self.health}")
        
    def double_damage(self, opponent):
        damage = (random.randint(5, self.attack_power)) * 2
        print(f"{self.name} unleashes a powerful strike on {opponent.name} for {damage} damage!")
        opponent.receive_attack(damage)

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
        

# Barbarian/Rogue/Ranger/Sorcerer/Bard classes (inherits from Character)
class Barbarian(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)
        
    def special_ability(self, opponent):
        print("\nSpecial Abilities:")
        print("1. Rage Fury - Unleashes a ferocious attack, dealing double damage")
        print("2. War Cry - Initimidates enemy, reducing their attack power for one turn.")
        
        action = input("Which ability would you like to use? (1 or 2): ")
        
        if action =="1":
            print(f"\n{self.name} used Rage Fury!")
                        
            self.double_damage(opponent)
            
        elif action == "2":
            print(f"\n{self.name} used War Cry!")
            
            self.defensive_mode = True
            print(f"The enemy's attack has been weakened!")
            
        else:
            print("Invalid choice. Special ability was not used.")

class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)
        
    def special_ability(self, opponent):
        print("\nSpecial Abilities:")
        print("1. Backstab - Deals massive damage from behind, catching the enemy off guard.")
        print("2. Evasive Flip - Performs lightning-fast roll to dodge next attack, reducing damage.")
        
        action = input("Which ability would you like to use? (1 or 2): ")
        
        if action =="1":
            print(f"\n{self.name} used Backstab!")
            
            self.double_damage(opponent)

        elif action == "2":
            print(f"\n{self.name} used Evasive Flip!")
            
            self.defensive_mode = True
            print(f"{self.name} is ready to evade the next attack!")
        
        else:
            print("Invalid choice. Special ability was not used.")

class Ranger(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)
        
    def special_ability(self, opponent):
        print("\nSpecial Abilities:")
        print("1. Arrow Barrage - Fires multiple arrows at once, dealing increased damage.")
        print("2. Nature's Shield - Defend against the next attack and gain a slight health boost.")
        
        action = input("Which ability would you like to use? (1 or 2): ")
        
        if action =="1":
            print(f"{self.name} used Arrow Barrage!")
            
            self.double_damage(opponent)
            
        elif action == "2":
            print(f"{self.name} used Nature's Shield!")
            
            self.health += 5
            self.defensive_mode = True
            print(f"{self.name} increased their health by 5 and is ready to defend the next attack!")
            
        else:
            print("Invalid choice. Special ability was not used.")
        
class Sorcerer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)
        
    def special_ability(self, opponent):
        print("\nSpecial Abilities:")
        print("1. Fireball - Launches a powerful fireball, dealing double damage.")
        print("2. Magic Shield - Blocks some incoming damage using magical protection.")
        
        action = input("Which ability would you like to use? (1 or 2): ")
        
        if action =="1":
            print(f"{self.name} used Fireball!")
            
            self.double_damage(opponent)
            
        elif action == "2":
            print(f"{self.name} used Magic Shield!")
            
            self.defensive_mode = True
            
            print(f"{self.name} is ready to defend against the next attack!")
            
        else:
            print("Invalid choice. Special ability was not used.")

class Bard(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30)
        
    def special_ability(self, opponent):
        print("\nSpecial Abilities:")
        print("1. Heroic Call - Summons nearby allies to aid in battle.")
        print("2. Healing Song - Sings a soothing melody. Increase health and protect against the next attack.")
        
        action = input("Which ability would you like to use? (1 or 2): ")
        
        if action =="1":
            print(f"{self.name} used Heroic Call!")
            
            self.double_damage(opponent)
            
        elif action == "2":
            print(f"{self.name} used Healing Song!")
            
            self.health += 10
            self.defensive_mode = True
            
            print(f"{self.name} increased their health by 10 and is protected against the next attack!")
            
        else:
            print("Invalid choice. Special ability was not used.")

     
# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=20)

    def regenerate(self):
        self.health += 5
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"\n{self.name} regenerates 5 health! Current health: {self.health}")