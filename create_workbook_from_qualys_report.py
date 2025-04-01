#!/usr/bin/python3

import os
import sys
import re
import csv
import importlib.util
from openpyxl import Workbook

#workaround because big csv fields
csv.field_size_limit(sys.maxsize)

def split_file(input_filename, output_file):
    try:
        with open(input_filename, "r", encoding="utf-8") as file:
            current_section = None
            skip_this_line = False

            # Regular expressions to detect sections with exact match
            patterns = {
                "summary": re.compile(r"^Host Statistics \(Percentage of Controls Passed per Host\)$"),
                "assets": re.compile(r"^ASSET TAGS$"),
                "results": re.compile(r"^RESULTS$"),
                "errors": re.compile(r"^Possible reason for empty report$")
            }

            wb = Workbook(write_only=True)

            for row in csv.reader(file):
                if row:
                    for section, regex in patterns.items():
                        if regex.match(row[0]):
                            current_section = section
                            current_ws = wb.create_sheet(current_section)
                            skip_this_line = True
                            print ("Processing "+ current_section)
                            break  # Let's get out of the loop
                        else:
                            skip_this_line=False
                                      
                    if(current_section and skip_this_line == False):
                        current_ws.append(row)
        
        print("Saving output file: " + output_file)
        wb.save(output_file)

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{input_filename}'.")
    except IndexError:
        print(len(row))
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Check before run
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage : python " + sys.argv[0] + " input_file.csv output_file")
        sys.exit(1)

    spec = importlib.util.find_spec("lxml")
    if spec is None:
        print("You should install lxml package ! Or the script will be slow and eats lot of memory")
        
    split_file(sys.argv[1], sys.argv[2])
