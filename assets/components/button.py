import pygame as pg
from assets.settings import *

class Button(pg.sprite.Sprite):
    def __init__(self, groups, pos, w, h, z, part, bgcolor = None, which_pos='topleft', hover_behavior=False):
        super().__init__(groups)
        self.pos = pos
        self.height = h
        self.width = w
        self.z = z
        self.part = part
        self.true_z = self.z + (self.part * 100)
        self.bgcolor = pg.Color(bgcolor) if bgcolor is not None else None
        self.hover_behavior = hover_behavior
        self.bgcolor_hov = pg.Color(max(self.bgcolor.r + 30,0), max(self.bgcolor.g + 30,0), max(self.bgcolor.b + 30,0)) if bgcolor is not None else None
        self.button_setup(which_pos)
    
    def button_setup(self, which_pos):
        self.surface = pg.Surface((self.width,self.height))
        if self.bgcolor is not None:
            self.surface.fill(self.bgcolor)
        if which_pos == 'topleft':
            self.rect = self.surface.get_rect(topleft=self.pos)
        elif which_pos == 'center':
            self.rect = self.surface.get_rect(center=self.pos)
        elif which_pos == 'bottomleft':
            self.rect = self.surface.get_rect(bottomleft=self.pos)

    def enforce_status(self):
        if self.bgcolor is not None:
            self.surface.fill(self.bgcolor)

    def check_hover(self):
        if self.hover_behavior:
            mouse_pos = pg.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                self.surface.fill(self.bgcolor_hov)

    def update(self, dt):
        self.enforce_status()
        self.check_hover()