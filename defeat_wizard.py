from classes import *

# ======================= CREATE CHARACTER FUNCTION =========================
'''
Creates a character with the desired class, based on user input.
'''
def create_character():
    # Make sure Warrior, Mage, Archer, Paladin, and Rogue are defined in classes.py
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")
    print("5. Rogue")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)  
    elif class_choice == '4':
        return Paladin(name)  
    elif class_choice == '5':
        return Rogue(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# ========================== BATTLE FUNCTION =============================
'''
Facilitates battle between the player and the Dark Wizard.
Has a user menu for actions.
'''
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
            player.heal(wizard)  # Implement heal method
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

# =========================== HEAL METHOD FOR PLAYER ======================
'''
Adds a heal method to the base character class.
Restores a fixed amount of health, but does not exceed max_health.
'''
def heal(self, target=None):
    heal_amount = 20  # You can adjust the heal amount as needed
    if self.health < self.max_health:
        healed = min(heal_amount, self.max_health - self.health)
        self.health += healed
        print(f"{self.name} heals for {healed} health points! (Current health: {self.health}/{self.max_health})")
    else:
        print(f"{self.name} is already at full health.")

# Monkey-patch heal into all character classes (assuming they inherit from a base class 'Character')
for cls in [Warrior, Mage, Archer, Paladin, Rogue]:
    cls.heal = heal

# =========================== MAIN FUNCTION ==============================
'''
Handles the flow of the game.
'''
def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()