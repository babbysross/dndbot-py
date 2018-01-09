#DnD 5e Bot.py

import string
from random import *
from openpyxl import *

def char_gen():
	# Generate character race
	char_race = random.choice(['Human', 'Elf' 'Halfling', 'Dwarf', 'Dragonborn', 'Gnome', 'Half-Elf', 'Half-Orc', 'Tiefling', 'Aasimar', 'Aarakocra', 'Goliath', 'Genasi', 'Bugbear', 'Firbolg', 'Goblin', 'Hobgoblin', 'Kenku', 'Kobold', 'Lizardfolk', 'Orc', 'Yuan-Ti', 'Tabaxi', 'Triton', 'Tortle'])
	# Load spreadsheets with openpyxl
	wb_name = load_workbook('character_names.xlsx')
	ws_name = wb_name[char_race]
	# Generate a character for the user. Ask for a name and provide a race, class and random stats tailored to the class.
	print("Initialising character generator.")
	# This is a hack, will update to use a spreadsheet
	print("Shall I generate a name or do you have one in mind? (generate/type)")
	name_method = input()
	if name_method == "generate":
		fname_no = randint(1,)
		fname_ltr = random.choice('BC') # proof of concept, use in a function or something
		print("Your name is %s and you are a %s %s" % (char_name, char_race, char_class))
	elif name_method == "type":
		custom_name = input("Please enter your character's name: ")
		print("Your name is %s and you are a %s %s" % (custom_name, char_race, char_class))

def encounter_gen():
	# Generates an encounter for the user, giving a situation, number of enemies and enemy types/stats.
	print("Initialising encounter generator.")

def dun_gen():
	# Generates a dungeon for the user. Produces a map, 3 encounters and a boss (all highlighted on map). Also details treasure that boss is guarding.
	print("Initialising dungeon generator.")

def boss_gen():
	# Generatees a final boss for the user. Asks for a name and provides a type, attacks and stats.
	print("Initialising boss generator.")
	 

def start_prompt():
	# Asks user if they want to generate a character, an encounter, a dungeon or a boss.
	print("What would  you like to do? \n 1 - Generate a character \n 2 - Generate an encounter \n 3 - Generate a dungeon \n 4 - Generate a final boss \n")
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




start_prompt()