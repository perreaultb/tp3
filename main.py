"""
jeu combat des monstres
par Bradley Perreault
groupe 4567
"""

"""
notes

20 max hp

every day you either

fight

no fight (penalty)

enemy randomized from dict

win by surviving # of days



"""

# imports

import random

# variables

hp_max : int = 20
hp : int = 20

days_survived : int = 1

enemies = {
    "gobelin": [15, 1],
    "loup": [5, 5],
    "dragon": [20, 3]
}
enemy_hp : int = None
chosen_enemy : str = None
enemy_damage : int = None

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
    global hp, days_survived
    penalty = random.randint(1, 3)
    hp -= penalty
    print(f"Vous avez choisi de ne pas combattre le monstre.")
    print(f"Vous subissez une pénalité de {penalty} points de vie. Il vous reste {hp} points de vie.")
    if not hp > 0:
        return False
    days_survived += 1
    return True

line1 = "\n"
line2 = "\n"
line3 = "\n"

def handle_fight():
    """
    Gère le combat contre un monstre, applique les dégâts et affiche les informations sur le joueur.
    """
    global hp, days_survived, chosen_enemy, enemy_hp, enemy_damage, line1, line2, line3
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
                line2 = f"Vous avez vaincu le {chosen_enemy} !"
                break
            hp -= random.randint(1, 3) * enemy_damage
            line3 = f"Le {chosen_enemy} vous inflige {enemy_damage} points de dégâts. Il vous reste {hp} points de vie."
        elif choice == "inventaire":
            pass
        else:
            line3 = "Choix invalide. Veuillez choisir 'attaquer' ou 'inventaire'."

    if hp <= 0: 
        #print("Vous êtes mort !")
        return False

    days_survived += 1
    return True

# main loop


loop = True

while loop:

    playing = True

    while playing:
        choice = handle_day_start().lower()
        day_start = True
        while day_start:
            if choice == "o":
                survived = handle_fight()
                if not survived:
                    playing = False
                    break
                day_start = False
            elif choice == "n":
                survived = dont_fight()
                if not survived:
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
                print("Essaie de pas mourrir yk")
                input("Appuyez sur Entrée pour continuer...")


    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("Vous etes mort !")
    replay = input("rejouer ? (o/n)")
    if replay.lower() == "o":
        hp = hp_max
        days_survived = 1
        line1 = "\n"
        line2 = "\n"
        line3 = "\n"
    elif replay.lower() == "n":
        loop = False
        print("ciao")
    else:
        print("Choix invalide. ciao")
        loop = False