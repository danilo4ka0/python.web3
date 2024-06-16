import os
import shutil
from concurrent.futures import ThreadPoolExecutor
import argparse

def copy_file(file_path, target_dir):
    ext = os.path.splitext(file_path)[1].lstrip('.').lower()
    if not ext:
        ext = 'unknown'
    dest_dir = os.path.join(target_dir, ext)
    os.makedirs(dest_dir, exist_ok=True)
    shutil.copy2(file_path, dest_dir)

def process_directory(source_dir, target_dir, executor):
    for root, _, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            executor.submit(copy_file, file_path, target_dir)

def main(source_dir, target_dir):
    with ThreadPoolExecutor() as executor:
        process_directory(source_dir, target_dir, executor)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sort and copy files by extension.")
    parser.add_argument("source_dir", help="Path to the directory with files to process.")
    parser.add_argument("target_dir", nargs='?', default="dist", help="Path to the directory where sorted files will be placed.")
    args = parser.parse_args()

    main(args.source_dir, args.target_dir)
