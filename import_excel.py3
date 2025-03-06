#!/usr/bin/python3

import os
import sys
import pandas as pd

# Nom du fichier Excel de sortie
fichier_excel = "rapport_qualys.xlsx"

def create_excel_file(input_folder, output_folder):

    # Création d'un writer Excel avec openpyxl
    with pd.ExcelWriter(os.path.join(output_folder, fichier_excel), engine="openpyxl") as writer:
        for fichier in os.listdir(input_folder):
            if(fichier!="assets.csv"):
                if fichier.endswith(".csv"):
                    chemin_complet = os.path.join(input_folder, fichier)
                    nom_feuille = os.path.splitext(fichier)[0]  # Enlève .csv pour le nom de l'onglet
                    
                    df = pd.read_csv(chemin_complet, dtype="unicode")
                    df.to_excel(writer, sheet_name=nom_feuille, index=False)
                    print (fichier + " imported")
            else:
                print ("assets.csv file skipped")


    print(f"Output file generated : {fichier_excel}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage : python " + sys.argv[0] + " input_folder output_folder")
        sys.exit(1)

    create_excel_file(sys.argv[1], sys.argv[2])