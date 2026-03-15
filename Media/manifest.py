import json
from pathlib import Path


def generar_manifest_pptx(directorio='Presentaciones', nombre_json='presentaciones.json'):
    """Recorre la carpeta Presentaciones y genera presentaciones.json con PPTX."""
    carpeta = Path(directorio)

    if not carpeta.exists() or not carpeta.is_dir():
        raise FileNotFoundError(f"Directorio no válido: {carpeta}")

    archivos_pptx = []
    for entrada in carpeta.iterdir():
        if entrada.is_file() and entrada.suffix.lower() == '.pptx':
            archivos_pptx.append(entrada.name)

    archivos_pptx = sorted(archivos_pptx)

    salida = carpeta / nombre_json
    with salida.open('w', encoding='utf-8') as f:
        json.dump(archivos_pptx, f, ensure_ascii=False, indent=2)

    return archivos_pptx


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Generar presentaciones.json desde un directorio PPTX')
    parser.add_argument('-d', '--directorio', default='Presentaciones',
                        help='Directorio donde buscar PPTX (por defecto: Presentaciones)')
    args = parser.parse_args()

    posibles = [
        Path(args.directorio),
        Path(__file__).parent / args.directorio,
        Path('/home/nicodev/Documentos/Coding/Web Page LDB/Media') / args.directorio,
        Path('/home/nicodev/Documentos/Coding/Web Page LDB') / args.directorio,
        Path('/home/nicodev/Documentos/Coding/Web Page LDB/Media/Presentaciones'),
    ]

    encontrado = None
    for ruta in posibles:
        if ruta.exists() and ruta.is_dir():
            encontrado = ruta
            break

    if not encontrado:
        print('Error: no se encontró un directorio válido. Probadas:', ', '.join(str(r) for r in posibles))
    else:
        try:
            lista = generar_manifest_pptx(encontrado, 'presentaciones.json')
            print(f'Generado {encontrado / "presentaciones.json"} con {len(lista)} pptx')
            for presentacion in lista:
                print('-', presentacion)
        except Exception as e:
            print('Error:', e)
