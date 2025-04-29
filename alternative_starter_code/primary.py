from classes import *

def create_character():
    print("Choose your character class:")
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

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
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

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()