def contar_palabras(archivo):
    with open(archivo, 'r') as f:
        texto = f.read()
        palabras = texto.split()
        return len(palabras)

archivo_texto = 'documento.txt'
total_palabras = contar_palabras(archivo_texto)
print(f'El archivo contiene {total_palabras} palabras.')
