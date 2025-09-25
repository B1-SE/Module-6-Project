import random
'''
REMINDER:
In addition to completing the Warrior and Mage classes, you need to create two more classes that inherit from Character, such as:
- Archer
- Paladin
You don't have to create these EXACT classes, you have creative freedom about which additional classes to create. It doesn't have to be Archer & Paladin.

Each custom class must have two unique abilities, such as:
- Archer: "Quick Shot" (double arrow attack) and "Evade" (avoid next attack).
- Paladin: "Holy Strike" (bonus damage) and "Divine Shield" (blocks the next attack).

Additionally, you need to implement a heal() method in the base Character class.
Lastly, you need to randomize the damage done in the Character class' attack() method.
'''
# ====================== BASE CHARACTER CLASS ============================
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit

    '''
    Modify this function so that the character does a random amount of damage.
    Hint: Look up the randint() function from Python's random library.
    '''
    def attack(self, opponent):
        # Randomize damage between 80% and 120% of attack_power
        damage = random.randint(int(self.attack_power * 0.8), int(self.attack_power * 1.2))
        # Check for evade logic before applying damage
        if not hasattr(opponent, 'evadeNextAttack'):
            opponent.health -= damage
            print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        elif hasattr(opponent, 'evadeNextAttack') and opponent.evadeNextAttack == False:
            opponent.health -= damage
            print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        elif hasattr(opponent, 'evadeNextAttack') and opponent.evadeNextAttack == True:
            print(f"{self.name} attacks {opponent.name}, but {opponent.name} evades the attack!")
            opponent.evadeNextAttack = False

    def heal(self):
        heal_amount = random.randint(15, 30)
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals for {heal_amount} health! Current health: {self.health}/{self.max_health}")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
       
# ============================ SUBCLASSES ================================ 

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.shield_block_active = False

    def special_ability(self, opponent):
        print("\nAbilities:")
        print("1. Heroic Strike (Bonus Damage)")
        print("2. Shield Block (Reduce next attack's damage)")
        action = input("Which ability do you want to use? ")
        if action == "1":
            # Heroic Strike: A powerful attack with bonus damage
            bonus_damage = random.randint(10, 20)
            total_damage = self.attack_power + bonus_damage
            opponent.health -= total_damage
            print(f"{self.name} uses Heroic Strike on {opponent.name} for {total_damage} damage!")
        elif action == "2":
            # Shield Block: Reduce damage from the next incoming attack
            self.shield_block_active = True
            print(f"{self.name} raises their shield, preparing to block part of the next attack!")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def special_ability(self, opponent):
        # For now, a simple message. You can expand this with more abilities.
        print(f"{self.name} channels arcane energy but has not yet mastered any special abilities.")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")
        
class Rogue(Character):
    def __init__(self, name):
        # Call the superclass (parent class) __init__() method and pass required data to it.
        super().__init__(name, health=120, attack_power=30)
        self.evadeNextAttack = False
        
    def special_ability(self, opponent):
        print("\nAbilities:")
        print("1. Gathering Shadows")
        print("2. Siphoning Strikes")
        print("3. Preemptive Dodge (Evade)")
        action = input("Which ability do you want to use? ")
        
        if action == "1":
            '''
            Ability: Gathering Shadows
            Description: Increases the rogue's damage by 30 but does not attack.
            '''
            self.attack_power += 30
            print(f"\nShadows gather around {self.name} increasing their damage to {self.attack_power}.")
        elif action == "2":
            '''
            Ability: Siphoning Strikes
            Description: Strikes the opponent & heals for half of the damage dealt.
            '''
            opponent.health -= self.attack_power
            self.health += self.attack_power // 2 # Floor division rounds to the nearest integer (whole number)
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"\n{self.name} strikes {opponent.name} with vampiric daggers, dealing {self.attack_power} damage and siphoning the wizard's health to {self.health} health.")
        elif action == "3":
            '''
            Ability: Preemptive Dodge (Evade)
            Description: Dodges the next attack.
            '''
            self.evadeNextAttack = True
            print(f"\n{self.name} uses Preemptive Dodge. He will dodge the next attack!")

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=28)
        self.evadeNextAttack = False

    def special_ability(self, opponent):
        print("\nAbilities:")
        print("1. Quick Shot (Double Arrow Attack)")
        print("2. Evade (Avoid next attack)")
        action = input("Which ability do you want to use? ")
        if action == "1":
            # Quick Shot: Attack twice with reduced damage
            for i in range(2):
                damage = random.randint(int(self.attack_power * 0.5), int(self.attack_power * 0.8))
                opponent.health -= damage
                print(f"{self.name} fires a quick arrow at {opponent.name} for {damage} damage!")
        elif action == "2":
            # Evade: Avoid next attack
            self.evadeNextAttack = True
            print(f"{self.name} prepares to evade the next attack!")

class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=22)
        self.shielded = False

    def special_ability(self, opponent):
        print("\nAbilities:")
        print("1. Holy Strike (Bonus Damage)")
        print("2. Divine Shield (Block next attack)")
        action = input("Which ability do you want to use? ")
        if action == "1":
            # Holy Strike: Attack with bonus damage
            bonus = random.randint(10, 20)
            total_damage = self.attack_power + bonus
            opponent.health -= total_damage
            print(f"{self.name} uses Holy Strike on {opponent.name} for {total_damage} damage!")
        elif action == "2":
            # Divine Shield: Block next attack
            self.shielded = True
            print(f"{self.name} is shielded and will block the next attack!")

    def take_damage(self, damage):
        if self.shielded:
            print(f"{self.name}'s Divine Shield blocks the attack!")
            self.shielded = False
        else:
            self.health -= damage

def choose_action(player, opponent):
    print(f"\n{player.name}'s turn!")
    print("Choose an action:")
    print("1. Attack")
    print("2. Heal")
    print("3. Use Special Ability")
    print("4. View Stats")
    action = input("Enter the number of your action: ")
    if action == "1":
        # Handle Paladin's shield logic
        if hasattr(opponent, 'shielded') and opponent.shielded:
            print(f"{opponent.name}'s Divine Shield blocks the attack!")
            opponent.shielded = False
        else:
            player.attack(opponent)
    elif action == "2":
        player.heal()
    elif action == "3":
        if hasattr(player, 'special_ability'):
            player.special_ability(opponent)
        else:
            print(f"{player.name} does not have a special ability.")
    elif action == "4":
        player.display_stats()
        opponent.display_stats()
        # Allow the player to choose again after viewing stats
        choose_action(player, opponent)
    else:
        print("Invalid action. Try again.")
        choose_action(player, opponent)

def is_alive(character):
    return character.health > 0

def battle(player1, player2):
    turn = 0
    while is_alive(player1) and is_alive(player2):
        current_player = player1 if turn % 2 == 0 else player2
        opponent = player2 if turn % 2 == 0 else player1
        choose_action(current_player, opponent)
        # Clamp health to zero if negative
        if opponent.health < 0:
            opponent.health = 0
        print(f"\n{player1.name}: {player1.health}/{player1.max_health} | {player2.name}: {player2.health}/{player2.max_health}")
        turn += 1
    winner = player1 if is_alive(player1) else player2
    print(f"\n{winner.name} wins the battle!")

if __name__ == "__main__":
    # Example: let user pick classes for two players
    classes = {
        "1": Warrior,
        "2": Mage,
        "3": Rogue,
        "4": Archer,
        "5": Paladin,
        "6": EvilWizard
    }
    print("Choose class for Player 1:")
    print("1. Warrior\n2. Mage\n3. Rogue\n4. Archer\n5. Paladin\n6. EvilWizard")
    p1_class = input("Enter number: ")
    p1_name = input("Enter Player 1's name: ")
    player1 = classes.get(p1_class, Warrior)(p1_name)

    print("\nChoose class for Player 2:")
    print("1. Warrior\n2. Mage\n3. Rogue\n4. Archer\n5. Paladin\n6. EvilWizard")
    p2_class = input("Enter number: ")
    p2_name = input("Enter Player 2's name: ")
    player2 = classes.get(p2_class, Warrior)(p2_name)

    battle(player1, player2)
