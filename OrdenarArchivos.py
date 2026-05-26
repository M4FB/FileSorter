from pathlib import Path

opcion_seleccionada = 1
p = Path.home()

print(p)

IMAGENES=(
    ".jpeg",".png",".jpg",
    ".webp",".gif",".tiff"
)
DOCUMENTOS=(
    ".pdf",".tex",".pptx",
    ".txt",".csv","docx"
)

CARPETAS={
    1 : "Downloads",
    2 : "Documents",
    3 : "Desktop",
    4 : "Music",
    5 : "Videos",
    6 : "Cancelar / Salir",
}

def create_directories(directory : Path):
    name_doc = "Documentos"
    name_img = "Imagenes"
    if (directory / name_doc).exists():
        print("El directorio ya existe", directory / name_doc)
    else:
        print("Crear directorio")
    if (directory / name_img).exists():
        print("El directorio ya existe",directory / name_img)
    else:
        print("Crear Imagenes")


def find_files(directory : Path):
    contador_directorios = 0
    contador_archivos = 0
    contador_imagenes = 0
    contador_documentos = 0
    imagenes = []
    documentos = []
    for item in directory.iterdir():
        if item.is_file():
            contador_archivos += 1
            if item.suffix in DOCUMENTOS:
                contador_documentos += 1
                documentos.append(item)
            if item.suffix in IMAGENES:
                contador_imagenes += 1
                imagenes.append(item)
        if item.is_dir():
            contador_directorios += 1
    print(f"Numero de archivos: {contador_archivos}")
    print(f"Numero de directorios: {contador_directorios}")
    print(f"Numero de documentos: {contador_documentos}\n Listado de documentos: \n {documentos}")
    print(f"Numero de imagenes: {contador_imagenes}\n Listado de imagenes: \n {imagenes}")


while opcion_seleccionada != 6:
    print("Seleccione una opción:")
    for numero,carpeta in CARPETAS.items():
        print(numero, "=", carpeta)
    
    opcion_seleccionada = int(input(f"{CARPETAS[opcion_seleccionada]}>] Opcion: "))
    
    ruta_seleccionada = p / CARPETAS[opcion_seleccionada]

    # find_files(ruta_seleccionada)
    create_directories(ruta_seleccionada)
