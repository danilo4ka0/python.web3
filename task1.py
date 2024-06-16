import os
import shutil


def process_directory(source_dir: str, target_dir: str = "dist"):
    # Проверяем существование целевой директории
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Рекурсивно обходим исходную директорию
    for root, _, files in os.walk(source_dir):
        for file in files:
            source_path = os.path.join(root, file)
            _, extension = os.path.splitext(file)
            extension = extension[1:]  # убираем точку в начале расширения

            # Создаем поддиректорию в целевой директории, если её нет
            target_subdir = os.path.join(target_dir, extension)
            os.makedirs(target_subdir, exist_ok=True)

            # Копируем файл в целевую директорию
            target_path = os.path.join(target_subdir, file)
            shutil.copy(source_path, target_path)


if __name__ == "__main__":
    import sys

    # Проверяем аргументы командной строки
    if len(sys.argv) < 2:
        print("Usage: python sort_files.py <source_directory> [<target_directory>]")
        sys.exit(1)

    source_directory = sys.argv[1]
    target_directory = sys.argv[2] if len(sys.argv) > 2 else "dist"

    process_directory(source_directory, target_directory)

    print("Files sorted successfully.")
