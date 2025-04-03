import os
import zipfile
import shutil
import argparse
import glob
import subprocess
from pathlib import Path
from datetime import datetime


python_binary="python/python.exe"

def list_zip_files(input_folder):
    return glob.glob(os.path.join(input_folder, "*.zip"))

def unzip_file(zip_path, temp_folder):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(temp_folder)

def process_files(temp_folder, output_folder, transformation_script):
    for file in os.listdir(temp_folder):
        file_base = Path(file).stem
        file_path = os.path.join(temp_folder, file)
        output_file = os.path.join(output_folder, file_base+".xlsx")
        if os.path.isfile(file_path):  # Vérifie que c'est bien un fichier
            print(f"Processing {file_path}...")
            subprocess.run([python_binary, transformation_script, file_path, output_file], check=True)

def main(input_folder, temp_folder, output_folder, transformation_script):
    print(datetime.today())

    zip_files = list_zip_files(input_folder)

    if not zip_files:
        print("No ZIP file found.")
        return

    os.makedirs(temp_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)

    for zip_file in zip_files:
        print(f"Uncompressing {zip_file}...")
        unzip_file(zip_file, temp_folder)

        print(f"Processing files from {zip_file}...")
        process_files(temp_folder, output_folder, transformation_script)

        # Cleanup
        shutil.rmtree(temp_folder)
        os.makedirs(temp_folder, exist_ok=True)

    print("Processed all files !")
    print(datetime.today())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ZIP files processing automation")
    parser.add_argument("input_folder", help="Folder where ZIP files are stored")
    parser.add_argument("temp_folder", help="Temporary folder")
    parser.add_argument("output_folder", help="Output folder to store XLSX files")
    parser.add_argument("transformation_script", help="Python script to convert files")

    args = parser.parse_args()
    main(args.input_folder, args.temp_folder, args.output_folder, args.transformation_script)
