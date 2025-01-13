import pygame as pg
from assets.menu import Menu
from assets.settings import *

class MenuHandler:
    def __init__(self, app, audio_player):
        self.app = app
        self.audio_player = audio_player
        self.on_init()

    def on_init(self):
        self.previous_menu_id = None
        self.menu_id = 0
        self.menu = Menu(self.menu_id, self, self.audio_player)

    def switch_menu(self, new_menu_id):
        self.previous_menu_id = self.menu_id
        self.menu_id = new_menu_id
        self.menu = Menu(self.menu_id, self.app, self.audio_player)

    def handle_events(self, event):
        self.menu.handle_events(event)

    def update(self, dt):
        self.menu.update(dt)

    def render(self):
        self.menu.render()


