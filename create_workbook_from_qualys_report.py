#!/usr/bin/python3

import os
import sys
import re
import csv
from openpyxl import Workbook

#workaround because big csv fields
csv.field_size_limit(sys.maxsize)

def split_file(input_filename, output_file):
    try:
        with open(input_filename, "r", encoding="utf-8") as file:
            current_section = None
            skip_this_line=False

            # Expressions régulières pour détecter les sections avec correspondance exacte
            patterns = {
                "summary": re.compile(r"^Host Statistics \(Percentage of Controls Passed per Host\)$"),
                "assets": re.compile(r"^ASSET TAGS$"),
                "results": re.compile(r"^RESULTS$")
            }

            wb = Workbook(write_only=True)

            for row in csv.reader(file):
                for section, regex in patterns.items():
                    if regex.match(row[0]):
                        current_section = section
                        current_ws=wb.create_sheet(current_section)
                        skip_this_line=True
                        print ("Processing "+ current_section)
                        break  # On sort de la boucle dès qu'on trouve une correspondance
                    else:
                        skip_this_line=False
                        
                if(current_section and skip_this_line == False):
                    current_ws.append(row)
                    
        #print("Removing default sheet")
        #wb.remove(wb["Sheet"])
        print("Saving output file: " + output_file)
        wb.save(output_file)


    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Vérification et exécution
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage : python " + sys.argv[0] + " input_file.csv output_file")
        sys.exit(1)

    split_file(sys.argv[1], sys.argv[2])
