import os
import shutil
import random
import string


# Función para generar una cadena aleatoria de letras mayúsculas A-Z
def generate_random_letters(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))


# Función para generar una cadena aleatoria de dígitos 0-9
def generate_random_digits(length):
    return ''.join(random.choice(string.digits) for _ in range(length))


# Función para cambiar el contenido de un archivo
def modify_file_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    modified_content = ''
    for char in content:
        if char.isalpha():
            modified_content += random.choice(string.digits)
        elif char.isdigit():
            modified_content += random.choice(string.ascii_uppercase)
        else:
            modified_content += char

    with open(file_path, 'w') as file:
        file.write(modified_content)


# Función para copiar y modificar archivos y carpetas de manera recursiva
def copy_and_modify_folder(src_folder, dest_folder):
    try:
        shutil.copytree(src_folder, dest_folder)
        print(f"Copiando archivos y carpetas de '{src_folder}' a '{dest_folder}'...")

        for foldername, subfolders, filenames in os.walk(dest_folder):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                modify_file_content(file_path)

        print(f"Modificación de archivos y carpetas en '{dest_folder}' completada.")
    except Exception as e:
        print(f"Error: {str(e)}")


def process_folder(folder_path):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        if os.path.isfile(item_path):
            modify_file_content(item_path)
            new_name = generate_random_digits(6) + generate_random_letters(2)  # Cambiar el nombre del archivo
            os.rename(item_path, os.path.join(folder_path, new_name))
        elif os.path.isdir(item_path):
            new_name = generate_random_digits(6) + generate_random_letters(2)  # Cambiar el nombre de la carpeta
            os.rename(item_path, os.path.join(folder_path, new_name))
            process_folder(os.path.join(folder_path, new_name))


if __name__ == "__main__":
    source_folder = input("Ingrese la ubicación de la carpeta a copiar y modificar: ")

    dest_folder = source_folder + "_copia"

    copy_and_modify_folder(source_folder, dest_folder)
    process_folder(dest_folder)

    final_folder_name = generate_random_digits(6) + generate_random_letters(
        2)  # Cambiar el nombre de la carpeta copiada finalmente
    os.rename(dest_folder, final_folder_name)

    print(f"Se ha copiado y modificado la carpeta y su contenido en '{final_folder_name}'.")
