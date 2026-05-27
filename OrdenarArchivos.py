from pathlib import Path

opcion_seleccionada = 1
p = Path.home()

IMAGENES=(
    ".jpeg",".png",".jpg",
    ".webp",".gif",".tiff"
)
DOCUMENTOS=(
    ".pdf",".tex",".pptx",
    ".txt",".csv",".docx"
)
VIDEOS = (
    ".mp4",".mov",".mkv",".webm",
    ".avi",".wmv"
)
COMPRIMIDOS = (
    ".rar",".tar.gz",".tar",".zip",".7zip",
    ".tar.xz"
)


FILE_TYPE = {
    "Imagenes" : IMAGENES,
    "Documentos" : DOCUMENTOS,
    "Videos" : VIDEOS,
    "Comprimidos" : COMPRIMIDOS,
}

CARPETAS={
    1 : "Downloads",
    2 : "Documents",
    3 : "Desktop",
    4 : "Music",
    5 : "Videos",
    6 : "Cancelar / Salir",
}

def create_directories(directory : Path):
    for carpeta,extensiones in FILE_TYPE.items():
        if not (directory / carpeta).exists():
            print(f"Creando directorio {carpeta}...")
            (directory / carpeta).mkdir() 
        else:
            print(f"El directorio {carpeta} ya existe.")


def move_files(directory : Path):
    print("Moviendo archivos...")
    contador_directorios = 0
    contador_archivos = 0
    dict_contador_filetype = {}
    for item in directory.iterdir():
        if item.is_file():
            contador_archivos += 1
            for carpeta,extension in FILE_TYPE.items():
                if item.suffix in extension:
                    dict_contador_filetype[carpeta] += 1
                    item.move_into(directory / carpeta)
                    break
        if item.is_dir():
            contador_directorios += 1
    print(dict_contador_filetype)
    print(f"Numero de archivos: {contador_archivos}")
    print(f"Numero de directorios: {contador_directorios}")

while opcion_seleccionada != 6:
    print("Seleccione una opción:")
    for numero,carpeta in CARPETAS.items():
        print(numero, "=", carpeta)
    
    try:
        opcion_seleccionada = int(input(f"[{str(p / CARPETAS[opcion_seleccionada])}]> Opcion: "   ))
        if opcion_seleccionada == 6: break
        ruta_seleccionada = p / CARPETAS[opcion_seleccionada]

        create_directories(ruta_seleccionada)
        move_files(ruta_seleccionada)
    except (ValueError, KeyError):
        print("Ingrese un numero valido, del 1 al 6")
        opcion_seleccionada = 1
        