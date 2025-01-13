import pygame as pg
from assets.components.component import Component
from assets.settings import *

class Label(Component):
    def __init__(self, groups, text, font, font_size, font_color, pos, z, part, bgcolor = None, which_pos='topleft', dynamic_func = None):
        self.text = text
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.which_pos = which_pos
        self.dynamic_func = dynamic_func
        self.label_setup(pos)
        super().__init__(groups, pos, self.rect.width, self.rect.height, z, part, None, which_pos, False)
        topleft = self.rect.topleft
        self.bgcolor = bgcolor
        self.surface = self.font_renderer.render(self.text, True, self.font_color, self.bgcolor)
        self.rect = self.surface.get_rect(topleft=topleft)

    def label_setup(self, pos):
        self.font_renderer = pg.font.Font(resource_path('assets/fonts/CircularStd-Black.ttf'),self.font_size)
        self.surface = self.font_renderer.render(self.text, True, self.font_color)
        if self.which_pos == 'topleft':
            self.rect = self.surface.get_rect(topleft=pos)
        elif self.which_pos == 'center':
            self.rect = self.surface.get_rect(center=pos)
        elif self.which_pos == 'midleft':
            self.rect = self.surface.get_rect(midleft=pos)

    def enforce_status(self):
        if not self.dynamic_func:
            self.text = self.text
        else:
            self.text = self.dynamic_func()
            self.surface = self.font_renderer.render(self.text, True, self.font_color)