from PIL import Image
import numpy as np

# Cargar la imagen
imagen = Image.open('C:/Users/Suseth Sandoval/Pictures/cat.png')

# Convertir la imagen a escala de grises (opcional, si quieres simplificar la matriz)
##imagen_gris = imagen.convert('L')

# Convertir la imagen en una matriz de números
matriz = np.array(imagen)

# Mostrar la matriz resultante
print(matriz)
