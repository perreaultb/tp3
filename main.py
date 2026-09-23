"""
jeu combat des monstres
par Bradley Perreault
groupe 4567
"""



# imports

import random

# variables

hp_max : int = 20
hp : int = 20

days_survived : int = 1

enemies = {
    "gobelin": [15, 1],
    "loup": [5, 3],
    "dragon": [20, 2]
}
enemy_hp : int = None
chosen_enemy : str = None
enemy_damage : int = None


inventory = {
    "hp_potion": 0,
}

days_skipped : int = 0

# functions



def choose_enemy():
    """
    Choisit un ennemi aléatoire parmi les ennemis disponibles.
    """
    global chosen_enemy, enemy_hp, enemy_damage
    chosen_enemy = random.choice(list(enemies.keys()))
    enemy_hp = enemies[chosen_enemy][0]
    enemy_damage = enemies[chosen_enemy][1]
 


def handle_day_start():
    """
    Gère le début de la journée, affiche les informations sur le joueur et demande s'il veut combattre un monstre.
    """
    global days_survived, enemies, hp, chosen_enemy
    choose_enemy()
    print(f"Jour {days_survived} :")
    print(f"Vous avez {hp} points de vie.")
    choice = input(f"Un {chosen_enemy} apparait devant vous ! Voulez-vous le combattre ? (o/n/règles)")
    return choice


def dont_fight():
    """
    Gère le choix de ne pas combattre un monstre, applique une pénalité et affiche les informations sur le joueur.
    """
    global hp, days_survived, days_skipped
    if days_skipped >= 3:
        hp = 0
        return False
    penalty = random.randint(1, 3)
    hp -= penalty
    print(f"Vous avez choisi de ne pas combattre le monstre.")
    print(f"Vous subissez une pénalité de {penalty} points de vie. Il vous reste {hp} points de vie.")
    if not hp > 0:
        return False
    days_survived += 1
    days_skipped += 1
    return True

line1 = "\n"
line2 = "\n"
line3 = "\n"

def handle_fight():
    """
    Gère le combat contre un monstre, applique les dégâts et affiche les informations sur le joueur.
    """


    global hp, days_survived, chosen_enemy, enemy_hp, enemy_damage, line1, line2, line3
    line1 = "\n"
    line2 = "\n"
    line3 = "\n"
    print(f"Vous avez choisi de combattre le {chosen_enemy} !")
    while enemy_hp > 0 and hp > 0:
        print("/----------------------------\\")
        print(f"Vous avez {hp} points de vie.")
        print(f"Le {chosen_enemy} a {enemy_hp} points de vie.")
        print("Que voulez-vous faire ? (attaquer / inventaire)")
        if not line1 == "\n":
            print("\n")
        print(line1)
        print(line2)
        print(line3)
        choice = input().lower()
        if choice == "attaquer":
            player_damage = random.randint(1, 5)
            enemy_hp -= player_damage
            if enemy_hp > 0:
                line1 = f"Vous infligez {player_damage} points de dégâts au {chosen_enemy}. Il lui reste {enemy_hp} points de vie."
            else:
                line1 = f"Vous infligez {player_damage} points de dégâts au {chosen_enemy}. Il lui reste 0 points de vie!"
            if enemy_hp <= 0:
                random_loot = random.randint(1, 3)
                if random_loot == 1:
                    inventory["hp_potion"] += 1
                    print(f"Vous avez vaincu le {chosen_enemy} ! Vous trouvez une potion de vie dans son corps. Vous avez maintenant {inventory['hp_potion']} potions de vie.")
                else:
                    print(f"Vous avez vaincu le {chosen_enemy} !")
                break
            damage_taken = random.randint(1, 3) * enemy_damage
            hp -= damage_taken
            line3 = f"Le {chosen_enemy} vous inflige {damage_taken} points de dégâts. Il vous reste {hp} points de vie."
        elif choice == "inventaire":
            print(f"Vous avez {inventory['hp_potion']} potions de vie.")
            if inventory["hp_potion"] > 0:
                print("Voulez-vous utiliser une potion de vie ? (o/n)")
            elif hp == max_hp:
                print("Vous avez le maximum de HV! Pesser sur Entrer pour continuer.")
            else:
                print("Vous n'avez pas de potions de vie. Pesser sur Entrer pour continuer.")
            
            choice_inv = input().lower()
            if choice_inv == "o" and inventory["hp_potion"] > 0 and not hp == max_hp:
                if (hp + 5) > hp_max:
                    hp = hp_max
                    inventory["hp_potion"] -= 1
                    print(f"Vous utilisez une potion de vie et récupérez {hp_max - (hp - 5)} points de vie. Il vous reste {hp} points de vie et {inventory['hp_potion']} potions de vie.")
                else:
                    hp += 5
                    inventory["hp_potion"] -= 1
                    print(f"Vous utilisez une potion de vie et récupérez 5 points de vie. Il vous reste {hp} points de vie et {inventory['hp_potion']} potions de vie.")
            elif choice_inv == "n" and inventory["hp_potion"] > 0 and not hp == max_hp:
                print("Vous décidez de ne pas utiliser de potion de vie.")
            

        else:
            line3 = "Choix invalide. Veuillez choisir 'attaquer' ou 'inventaire'."


    if hp <= 0: 
        #print("Vous êtes mort !")
        return False
        

    days_survived += 1
    return True

# main loops

difficulty_select = True
while difficulty_select:
    difficulty = input("Choisissez la difficulté (facile, normal, difficile) : ").lower()
    if difficulty == "facile":
        max_hp = 125
        difficulty_select = False
    elif difficulty == "normal":
        max_hp = 65
        difficulty_select = False
    elif difficulty == "difficile":
        max_hp = 35    
        difficulty_select = False
    else:
        print("Choix invalide. Veuillez choisir 'facile', 'normal' ou 'difficile'.")


hp = max_hp

loop = True
while loop:

    playing = True

    while playing:
        if days_survived > 10:
            print("Félicitations ! Vous avez survécu 10 jours !")
            playing = False
            break
            

        choice = handle_day_start().lower()
        day_start = True
        while day_start:
            if choice == "o":
                survived = handle_fight()
                if not survived:
                    print("\n")
                    print("\n")
                    print("\n")
                    print("\n")
                    print("\n")
                    print("Vous etes mort !")
                    playing = False
                    break
                day_start = False
            elif choice == "n":
                survived = dont_fight()
                if not survived:
                    print("\n")
                    print("\n")
                    print("\n")
                    print("\n")
                    if days_skipped >= 3:
                        print("Vous avez choisi de ne pas combattre un monstre 3 fois. Vous sentez vos forces vous quitter.")
                    else:
                        print("Vous avez choisi de ne pas combattre le monstre et vous subissez une pénalité, ce qui vous a fait perdre tous vos points de vie.")
                    print("Vous etes mort !")
                    playing = False
                    break
                day_start = False
            elif choice == "règles":
                print("Règles du jeu :")
                print("Vous devez survivre un certain nombre de jours en combattant des monstres.")
                print("Chaque jour, vous pouvez choisir de combattre un monstre ou de ne pas le faire.")
                print("Si vous choisissez de ne pas combattre, vous subirez une pénalité.")
                print("Les monstres ont des points de vie et des dégâts différents.")
                print("Vous gagnez en survivant le nombre de jours requis (10).")
                print("Vous perdez en ne survivant pas le nombre de jours requis ou en choisissant de ne pas combattre plus de 3 monstres.")
                print("Essaie de pas mourrir!")
                input("Appuyez sur Entrée pour continuer...")
            else:
                print("Choix invalide. Veuillez choisir 'o', 'n' ou 'règles'.")
                choice = input(f"Un {chosen_enemy} apparait devant vous ! Voulez-vous le combattre ? (o/n/règles)").lower()
    replay = input("rejouer ? (o/n)")
    if replay.lower() == "o":
        hp = max_hp
        days_survived = 1
        line1 = "\n"
        line2 = "\n"
        line3 = "\n"
        inventory = {
            "hp_potion": 0,
        }
        difficulty_select = True
        while difficulty_select:
            difficulty = input("Choisissez la difficulté (facile, normal, difficile) : ").lower()
            if difficulty == "facile":
                max_hp = 125
                difficulty_select = False
            elif difficulty == "normal":
                max_hp = 65
                difficulty_select = False
            elif difficulty == "difficile":
                max_hp = 35    
                difficulty_select = False
            else:
                print("Choix invalide. Veuillez choisir 'facile', 'normal' ou 'difficile'.")
        
        hp = max_hp
    elif replay.lower() == "n":
        loop = False
        print("Au revoir !")
    else:
        print("Choix invalide. Au revoir !")
        loop = False

