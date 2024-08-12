import os
os.environ['SDL_AUDIODRIVER'] = 'dummy'  # Menghilangkan ALSA warning

import pygame
import PIL
import cv2
import moviepy
import pydub
import tkinter as tk

def check_installation():
    print("✅ Pygame version:", pygame.__version__)
    print("✅ Pillow version:", PIL.__version__)
    print("✅ OpenCV version:", cv2.__version__)
    print("✅ MoviePy version:", moviepy.__version__)

    try:
        from pkg_resources import get_distribution
        pydub_version = get_distribution("pydub").version
    except:
        pydub_version = None
    
    if pydub_version:
        print("✅ Pydub version:", pydub_version)
    else:
        print("✅ Pydub is installed, but the version could not be determined.")

    print("✅ Tkinter is installed and working!")

if __name__ == "__main__":
    check_installation()
