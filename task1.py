import os
import shutil
from concurrent.futures import ThreadPoolExecutor


def create_target_dirs(target_dir, extensions):
    for ext in extensions:
        os.makedirs(os.path.join(target_dir, ext), exist_ok=True)


def copy_file(file, target_dir):
    ext = file.split('.')[-1]
    target_subdir = os.path.join(target_dir, ext)
    shutil.copy(file, target_subdir)


def process_directory(src_dir, target_dir):
    extensions = set()
    file_paths = []
    for root, _, files in os.walk(src_dir):
        for file in files:
            file_path = os.path.join(root, file)
            ext = file.split('.')[-1]
            extensions.add(ext)
            file_paths.append(file_path)

    create_target_dirs(target_dir, extensions)

    with ThreadPoolExecutor() as executor:
        executor.map(lambda file: copy_file(file, target_dir), file_paths)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python sort_files.py <source_directory> [<target_directory>]")
        sys.exit(1)

    src_dir = sys.argv[1]
    target_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    process_directory(src_dir, target_dir)
    print(f"Files from {src_dir} have been sorted and copied to {target_dir}.")
