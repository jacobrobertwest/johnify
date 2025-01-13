import pygame as pg
from assets.settings import *

class Img(pg.sprite.Sprite):
    def __init__(self, groups, img_path, pos, z, part, which_pos='topleft', dynamic=False, second_img_path=None):
        super().__init__(groups)
        self.z = z
        self.part = part # 1 = body, 2 = header, 3 = footer
        self.true_z = self.z + (self.part * 100)
        self.img_path = img_path
        self.second_img_path = second_img_path
        self.surface = pg.image.load(self.img_path).convert_alpha()
        self.dynamic = dynamic
        if which_pos == 'topleft':
            self.rect = self.surface.get_rect(topleft=pos)
        elif which_pos == 'center':
            self.rect = self.surface.get_rect(center=pos)

    def dynamic_image(self,playing):
        if self.dynamic:
            if not playing:
                self.surface = pg.image.load(self.img_path).convert_alpha()
            else:
                self.surface = pg.image.load(self.second_img_path).convert_alpha()