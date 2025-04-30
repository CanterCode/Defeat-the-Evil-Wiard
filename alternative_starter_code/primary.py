from classes import *

def create_character():
    print("\nChoose your character class:")
    print("1. Barbarian")
    print("2. Rogue")
    print("3. Ranger") 
    print("4. Sorcerer")
    print("5. Bard")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Barbarian(name)
    elif class_choice == '2':
        return Rogue(name)
    elif class_choice == '3':
        return Ranger(name)
    elif class_choice == '4':
        return Sorcerer(name)
    elif class_choice == '5':
        return Bard(name)
    else:
        print("Invalid choice. Defaulting to Barbarian.")
        return Barbarian(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        print("5. Quit")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")
        
def rules():
    print("\nWelcome to Wizard Smackdown!")
    print("The interactive battle game where you face off against the Evil Wizard.")
    print("This game has been craeted using Python, by Josh Canterbury.")
    print("\nGame Rules:")
    print("1. Each character has health and attack power.")
    print("2. Players can attack, use special abilities, heal, or view stats during their turn.")
    print("3. Attack damage is randomly generated within the character's attack power range (sort of like rolling a dice).")
    print("4. The wizard regenerates a small amount of health after each turn.")
    print("5. The game ends when either the player or the wizard's health reaches zero.")
    print("\nHave fun and good luck!")
    
def main():
    rules()
    player = create_character()
    print(f"\nWelcome, {player.name}!")
    print(f"You have chosen the {player.__class__.__name__} class!")
    print("Here are your starting stats:")
    player.display_stats()
    print("Prepare for battle!")
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()