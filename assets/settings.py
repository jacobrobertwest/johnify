import pygame as pg

# window
WIN_HEIGHT = 675
WIN_WIDTH = 1200
BG_COLOR = 'gray'

MUSIC_END = pg.USEREVENT + 1

import os
import sys

def resource_path(relative_path):
    """ Get the absolute path to a resource, works for both development and PyInstaller bundles. """
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
