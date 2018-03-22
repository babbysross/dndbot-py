'''python dnd bot'''

from random import randint, choice
from openpyxl import load_workbook
from dice import roll

def char_gen():
    """Generate character name, race, class and stats"""
    # Generate Race and Class
    char_race = choice(['Human', 'Elf', 'Halfling', 'Dwarf', 'Dragonborn', 'Gnome', 'Half-Elf',
                        'Half-Orc', 'Tiefling'])
    char_class = choice(['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin',
                         'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard'])
    # Generate and sort stats, high to low
    stats = []
    for _ in range(6):
        stats.append(sum(roll('4d6^3')))
        stats.sort()
    # Load spreadsheets with openpyxl
    wb_name = load_workbook('character_names.xlsx')
    ws_name = wb_name[str(char_race)]
    """Generate a character for the user.
	Ask for a name and provide a race, class and random stats tailored to the class."""
    print("Initialising character generator.")
    while True:
        print("Shall I generate a name or do you have one in mind? (generate/type)")
        name_method = input()
        if name_method == "generate":
            # Find excel field for first name
            fname = ws_name[choice('BC') + str(randint(2, 51))]
            # Find excel field for last name
            lname = ws_name['D' + str(randint(2, 51))]
            # Print generated name, race, class and stats.
            print("Your name is %s %s and you are a %s %s" % (fname.value, lname.value,
                                                            char_race, char_class))
            print("Stats: STR: %s DEX: %s CON: %s INT: %s WIS: %s CHA: %s" %
                (stats[0], stats[1], stats[2], stats[3], stats[4], stats[5]))
            break
        elif name_method == "type":
            custom_name = input("Please enter your character's name: ")
            # Print custom name, as well as race, class and stats.
            print("Your name is %s and you are a %s %s" % (custom_name, char_race, char_class))
            print("Stats: STR: %s DEX: %s CON: %s INT: %s WIS: %s CHA: %s" %
                (stats[0], stats[1], stats[2], stats[3], stats[4], stats[5]))
            break

def encounter_gen():
    """Generate an encounter for the user.
	Gives a situation, number of enemies and enemy types/stats."""
    print("Initialising encounter generator.")

def dun_gen():
    """Generate a dungeon for the user.
    Produces map, 3 encounters, a boss & details treasure guarded by boss."""
    print("Initialising dungeon generator.")

def boss_gen():
    """Generate a final boss for the user. Asks for a name & provides a type, attacks & stats."""
    print("Initialising boss generator.")

def start_prompt():
    """Asks user if they want to generate a character, an encounter, a dungeon or a boss."""
    print("What would  you like to do? \n 1 - Generate a character \n 2 - Generate an encounter")
    print(" 3 - Generate a dungeon \n 4 - Generate a final boss \n")
    repeat_me = 1
    while repeat_me > 0:
        prompt_choice = input()
        if prompt_choice == "1":
            repeat_me = 0
            char_gen()
        elif prompt_choice == "2":
            repeat_me = 0
            encounter_gen()
        elif prompt_choice == "3":
            repeat_me = 0
            dun_gen()
        elif prompt_choice == "4":
            repeat_me = 0
            boss_gen()
        else:
            print("Please enter one of the numbers, 1 to 4.")
            repeat_me += 1


# Run Program
start_prompt()
