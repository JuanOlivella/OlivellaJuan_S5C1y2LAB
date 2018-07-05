# Descarga los paquetes necesarios para la solucion del ejercicio

import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq, fft2, ifft2, fftshift, ifftshift
from matplotlib.colors import LogNorm
from scipy import ndimage



# Guarda la imagene en un arreglo

imagen = plt.imread('moonlanding.png')


# Encuentra la transformada de Fourier de las imagen

transformadaImagen = fft2(imagen)

transformadaShift = fftshift(transformadaImagen)


# Genera el plot de la transformada de fourier de las imagen

plt.figure()
plt.imshow(np.abs(transformadaShift), norm = LogNorm(vmin=5))
plt.colorbar()
plt.savefig("Transformada.pdf")


# Funcion que me devuelve el punto medio de la lista

def mitadPunto(transformadaImagen):

    x = np.shape(transformadaImagen)[0]//2
    
    y = np.shape(transformadaImagen)[1]//2
    
    return x, y


# Recuadro que no se recorta

def recuadro(transformadaImagen, numero):
    x1 = mitadPunto(transformadaImagen)[0]-numero
    x2 = mitadPunto(transformadaImagen)[0]+numero
    y1 = mitadPunto(transformadaImagen)[1]-numero
    y2 = mitadPunto(transformadaImagen)[1]+numero

    return x1,x2,y1,y2

numero = 45

x1,x2,y1,y2 = (recuadro(transformadaShift, numero))

corte = transformadaShift[x1:x2,y1:y2]


# Encuentra los maximos del arreglo

menor = [np.where(abs(transformadaShift) >  150 , 0, transformadaShift)]

menorsi = np.squeeze(menor, axis=0)

menorsi[x1:x2,y1:y2] = corte


#  Encuentra la transformada inversa de Fourier de la imagen

ImagenShift = ifftshift(menorsi)

ImagenFiltrada = ifft2(ImagenShift).real

plt.figure()
plt.imshow(ImagenFiltrada, cmap = 'gray')
plt.savefig("ImagenFiltrada.pdf")


