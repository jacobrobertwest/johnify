import pygame as pg
from assets.settings import *
from assets.menu_handler import MenuHandler
from assets.audio_player import AudioPlayer
from assets.pgtimer import PGTimer
import sys

VERSION = '0.1'

class App:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT), flags=pg.DOUBLEBUF)
        icon_surf = pg.image.load(resource_path('assets/images/icon.png')).convert_alpha()
        pg.display.set_icon(icon_surf)
        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0
        self.version = VERSION
        pg.display.set_caption(f"Johnify (v{self.version})")
        self.is_running = True
        self.on_init()

    def on_init(self):
        self.audio_player = AudioPlayer(self)
        self.menu_handler = MenuHandler(self, self.audio_player)
        self.timers = {
            "input": PGTimer(150)
        }

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False
            elif event.type in (pg.KEYDOWN, pg.MOUSEBUTTONDOWN):
                if not self.timers['input'].active: # buffering any input from making its way down the stack at the top
                    self.menu_handler.handle_events(event)
                    self.timers['input'].activate()
            else:
                self.menu_handler.handle_events(event)

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def update(self):
        self.delta_time = self.clock.tick()
        self.time = pg.time.get_ticks() * 0.001
        self.menu_handler.update(self.delta_time)
        self.update_timers()
        # pg.display.set_caption(f'{pg.mouse.get_pos()} | {self.audio_player.current_song_paused} | Johnify: {self.audio_player.current_track_title} - {self.audio_player.playing} - Volume: {self.audio_player.volume} - Pos: {round((self.audio_player.get_current_song_pos() / self.audio_player.current_track_length)*100,0)}%')

    def render(self):
        self.screen.fill(BG_COLOR)
        self.menu_handler.render()
        pg.display.flip()

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
            self.audio_player.update()
            self.clock.tick(60)
        pg.quit()
        sys.exit()


if __name__ == '__main__':
    app = App()
    app.run()
