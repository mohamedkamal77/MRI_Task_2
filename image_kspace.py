# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 23:38:33 2020

@author: kimoo
"""

from PIL import Image
import numpy as np

def image_to_kspace(img):
    
    shift_img =  np.fft.ifftshift(img)
    fft = np.fft.fftn(shift_img)
    kspace = np.fft.fftshift(fft)
    kspace =  kspace / np.sqrt(kspace)
    return kspace

im = np.asarray(Image.open('Images/brain_mri.jpeg'))
kspace_img =  image_to_kspace(im)

Image.fromarray(np.uint8(np.abs(kspace_img))).save("Images/kspace_brain.png")

