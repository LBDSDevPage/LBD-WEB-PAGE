import json
from pathlib import Path


def generar_manifest_mp3(directorio='Pistas', nombre_json='audios.json'):
    """Recorre la carpeta Pistas y genera audios.json con mp3."""
    carpeta = Path(directorio)

    if not carpeta.exists() or not carpeta.is_dir():
        raise FileNotFoundError(f"Directorio no válido: {carpeta}")

    archivos_mp3 = []
    for entrada in carpeta.iterdir():
        if entrada.is_file() and entrada.suffix.lower() == '.mp3':
            archivos_mp3.append(entrada.name)

    archivos_mp3 = sorted(archivos_mp3)

    salida = carpeta / nombre_json
    with salida.open('w', encoding='utf-8') as f:
        json.dump(archivos_mp3, f, ensure_ascii=False, indent=2)

    return archivos_mp3


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Generar audios.json desde un directorio MP3')
    parser.add_argument('-d', '--directorio', default='Pistas',
                        help='Directorio donde buscar MP3 (por defecto: Pistas)')
    args = parser.parse_args()

    posibles = [
        Path(args.directorio),
        Path(__file__).parent / args.directorio,
        Path('/home/nicodev/Documentos/Coding/Web Page LDB/Audios') / args.directorio,
        Path('/home/nicodev/Documentos/Coding/Web Page LDB') / args.directorio,
        Path('/home/nicodev/Documentos/Coding/Web Page LDB/Audios/Pistas'),
        Path('/home/nicodev/Documentos/Coding/Web Page LDB/Audios/Pistas 2020'),
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
            lista = generar_manifest_mp3(encontrado, 'audios.json')
            print(f'Generado {encontrado / "audios.json"} con {len(lista)} mp3')
            for pista in lista:
                print('-', pista)
        except Exception as e:
            print('Error:', e)
