#!/usr/bin/python3

import sys
import re

def split_file(input_filename):
	with open(input_filename, "r", encoding="utf-8") as file:
		sections = {"summary": [], "assets": [], "results": []}
		current_section = None
		skip_this_line=0

		# Expressions régulières pour détecter les sections avec correspondance exacte
		patterns = {
			"summary": re.compile(r"^\"SUMMARY\"\s*$"),
			"assets": re.compile(r"^ASSET TAG\s*$"),
			"results": re.compile(r"^\"RESULTS\"\s*$")
		}

		for line in file:
			stripped_line = line.strip()  # Enlève les espaces inutiles en début/fin

			# Vérifie si la ligne correspond exactement à une section attendue
			for section, regex in patterns.items():
				if regex.match(stripped_line):
					current_section = section
					skip_this_line=1
					break  # On sort de la boucle dès qu'on trouve une correspondance
				else:
					skip_this_line=0

			# Si une section est définie, ajoute la ligne correspondante
			if (current_section and skip_this_line==0):
				sections[current_section].append(line)

	# Écriture des sections dans des fichiers séparés
	for section, lines in sections.items():
		if lines:  # Vérifie qu'il y a bien du contenu avant d'écrire
			output_filename = f"{section.replace(' ', '_')}.txt"
			with open(output_filename, "w", encoding="utf-8") as out_file:
				out_file.writelines(lines)
			print(f"File generated : {output_filename}")

# Vérification et exécution
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage : python script.py fichier.txt")
		sys.exit(1)

	filename = sys.argv[1]
	split_file(filename)