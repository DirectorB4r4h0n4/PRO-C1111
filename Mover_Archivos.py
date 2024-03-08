import os
import shutil

# Definir las rutas de origen y destino
from_dir = "Descargas"
to_dir = "Documentos_Archivos"

# Obtener la lista de archivos en la carpeta de origen
list_of_files = os.listdir(from_dir)

# Imprimir la lista de archivos
print("Archivos en la carpeta de origen:")
print(list_of_files)

# Recorrer la lista de archivos y moverlos a la carpeta de destino
for file_name in list_of_files:
    # Obtener la ruta completa de cada archivo
    source_path = os.path.join(from_dir, file_name)
    
    # Utilizar os.path.splitext para obtener el nombre y la extensión del archivo
    base_name, file_extension = os.path.splitext(file_name)

    # Comentar el estado anterior
    # print(f"Archivo: {base_name}, Extensión: {file_extension}")

    # Mover el archivo a la carpeta de destino
    shutil.move(source_path, os.path.join(to_dir, file_name))

print("Archivos movidos exitosamente.")
