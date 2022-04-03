import random
player_hp = 50
monster_hp = 50

#New options: Attack bravely, defend sensibly, flail wildly
#Attack bravely: executes a standard attack
#Defend sensibly: does not attack, but raises defense 50% for the monster's next attack
#Flail wildly: lowers attack accuracy, increases damage significantly

#At the beginning of each turn, the player is prompted to choose an action.
#To add maybe in the next iteration: attack closer to D&D, to include critical hits and critical fails.
#If critical fail, flavour text + monster expressing sympathy and offering another turn.  Up to player whether to take monster up on it.

class Player:
    def __init__(self, attack, damage, defense):
        self.attack = attack
        self.damage = damage
        self.defense = defense
        self.defending = False
        self.flailing = False

    def attack_bravely(self):
        atk_score = random.randint(1, self.attack)
        return atk_score

    def defend_sensibly(self):
        self.defending = True
        atk_score = 0

    def flail_wildly(self):
        self.flailing = True
        atk_score = random.randint(2, self.attack)/2
        return atk_score
        
player1 = Player(10, 10, 10)

class Monster:
    def __init__(self, attack, damage, defense):
        self.attack = attack
        self.damage = damage
        self.defense = defense
monster1 = Monster(9, 9, 9)

def player_turn():
    mon_def = random.randint(1, monster1.defense)
    global monster_hp
    player1.defending = False
    player1.flailing = False
    print("\nYOUR TURN")
    action = input(">>> ")
    action_dict = {"attack": ["a", "attack", "attack bravely"], "defend": ["d", "defend", "defend sensibly"], "flail": ["f", "flail", "flail wildly"]}
    if action in action_dict:
        if action in action_dict["attack"]:
            atk_score = player1.attack_bravely()
            print("You go in for the attack.")
        elif action in action_dict["defend"]:
            atk_score = player1.defend_sensibly()
        elif action in action_dict["flail"]:
            atk_score = player1.flail_wildly()
            print("You are Kermit on caffeine.  You are a Muppet on a mission.  You are not sure this was a good choice.")
        if player1.defending:
            print("You put up your dukes.  This monster can't hurt you.")
        elif atk_score > 0 and atk_score > mon_def:
            if player1.flailing:
                monster_hp = max(0, monster_hp - (random.randint(1, player1.damage) * 2))
                print("Somehow your wild swing connects!  Blood and teeth fly!  You are mad with power!")
                print("The monster has {} hp remaining".format(monster_hp))
            else:
                monster_hp = max(0, monster_hp - random.randint(1, player1.damage))
                print("A devastating blow!  The monster reels!")
                print("The monster has {} hp remaining".format(monster_hp))
        else:
            print("Swing and a miss, cowboy.")
    else:
        print("I'm sorry, that action is not recognised in the fight test module.  Please attack bravely, defend sensibly, or flail wildly.")
        player_turn()
        
def monster_turn():
    atk_score = random.randint(1, monster1.attack)
    play_def = random.randint(1, player1.defense)
    global player_hp
    print("\nMONSTER\'S TURN")
    if player1.defending:
        play_def = 2 * random.randint(1, player1.defense)
    if atk_score > play_def:
        player_hp = max(0, player_hp - random.randint(1, monster1.damage))
        print("That looked like it hurt.")
        print("You have {} hp remaining.".format(player_hp))
    else:
        print("The monster flails wildly, but can't land a blow.")

def fight():
    global monster_hp
    global player_hp
    while player_hp > 0:
        player_turn()
        if monster_hp > 0:
            monster_turn()
        else:
            print("""The monster groans, shudders, convulses, and goes down in a pool of spittle and viscera.
It's a death scene for the ages.

Honestly, you think he's overdoing it.""")
            break
    else:
        print("""You have been slain, finished, crushed to a pulp.
              You, sir, are an ex-adventurer.""")
              
def start_fight():
    fight_choice = input(">>> ").lower()
    if fight_choice in ("y","n"):
        if fight_choice == "y":
            fight()
        else:
            print("\nYou back away from the monster and right out of the module.  Have a nice day!")
    else:
        print("\nHuh?")
        start_fight()

print("""Welcome, adventurer!  You have entered the fight test module.
Don't be alarmed: no harm will come to you...we hope.

Standing in front of you is a monster.  Big, hairy, very grumpy.
Armed with nothing but your fists, your task is to defeat the monster.

This is a very polite sort of fight: in each round, you and the monster will take turns trying to hit each other.
If a hit is successful, the target's HP will go down.  If the monster runs out of HP before you do, you win!

For each turn, you may choose one of three actions:
\t(1) Attack bravely
\t(2) Defend sensibly
\t(3) Flail wildly

Choose \"Attack bravely\" to throw a punch at the monster.
\tThis will deal normal damage if it hits.
Choose \"Defend sensibly\" to take a defensive stance.
\tYou will not deal any damage, but the monster's next attack will be weakened.
Choose \"Flail wildly\" to wave your arms around like a Muppet and hope for the best.
\tYour chances of hitting will go down, but you will do extra damage if you do hit.

Ready? [Y/N]""")

start_fight()
        





    
