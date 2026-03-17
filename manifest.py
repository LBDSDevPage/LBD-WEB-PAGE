import json
from pathlib import Path


CONFIGS = [
    {
        "directorio": "Audios/Pistas",
        "salida": "Audios/Pistas/audios.json",
        "extensiones": [".mp3"],
    },
    {
        "directorio": "Media/Presentaciones",
        "salida": "Media/Presentaciones/presentaciones.json",
        "extensiones": [".mp4", ".pptx"],
    },
    {
        "directorio": "Partituras/Corario",
        "salida": "Partituras/Corario/corario.json",
        "extensiones": [".pdf", ".doc", ".docx"],
    },
]


def generar_manifest(directorio: Path, salida: Path, extensiones: list[str]) -> list[str]:
    """Recorre un directorio y genera un JSON con los nombres de archivos encontrados."""
    if not directorio.exists() or not directorio.is_dir():
        print(f"  ⚠ Directorio no encontrado, se omite: {directorio}")
        return []

    archivos = sorted(
        entrada.name
        for entrada in directorio.iterdir()
        if entrada.is_file() and entrada.suffix.lower() in extensiones
    )

    salida.parent.mkdir(parents=True, exist_ok=True)
    with salida.open("w", encoding="utf-8") as f:
        json.dump(archivos, f, ensure_ascii=False, indent=2)

    return archivos


if __name__ == "__main__":
    raiz = Path(__file__).parent

    for config in CONFIGS:
        directorio = raiz / config["directorio"]
        salida = raiz / config["salida"]
        extensiones = config["extensiones"]

        print(f"\nProcesando: {directorio}")
        lista = generar_manifest(directorio, salida, extensiones)

        if lista:
            print(f"  ✓ Generado {salida} con {len(lista)} archivo(s):")
            for nombre in lista:
                print(f"    - {nombre}")
        else:
            print(f"  ✗ No se encontraron archivos con extensiones {extensiones}")