import pygame as pg
import json
from assets.settings import *

class AudioPlayer:
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.on_init()

    def on_init(self):
        self.in_test_mode = False
        self.testing_prefix = 'test_' if self.in_test_mode else ''

        with open(resource_path('assets/track_info.json'), 'r') as f:
            self.track_data = json.load(f)['data']
        self.mixer = pg.mixer
        self.mixer.init()
        self.current_song_index = 0
        self.current_song_pos = 0
        self.mixer.music.set_endevent(MUSIC_END)
        self.playing = False
        self.volume = 71
        self.is_muted = False
        self.started = False
        self.volume_increment = 11
        self.volume_decrement = 9
        self.current_song_pos_percentage = 0.0
        self.set_mixer_volume(self.volume)
        self.current_song_paused = False
        self.load_current_song()
        # print(self.mixer.music.get_endevent())

    def load_current_song(self):
        self.mixer.music.load(resource_path(f'assets/{self.testing_prefix}audio/{self.current_song_index}.ogg'))
        self.queue_next_song()
        self.load_current_song_metadata()

    def load_current_song_metadata(self):
        self.current_track_num = self.track_data[self.current_song_index]['track_num']
        self.current_track_title = self.track_data[self.current_song_index]['title']
        self.current_track_length = self.track_data[self.current_song_index]['length']

    def queue_next_song(self):
        self.next_song_index = self.current_song_index + 1 if self.current_song_index < 9 else 0
        self.last_song_index = self.current_song_index - 1 if self.current_song_index > 0 else 9

    def play_loaded_song(self):
        self.playing = True
        self.started = True
        self.current_song_paused = False
        self.mixer.music.play()

    def pause_loaded_song(self):
        self.playing = False
        self.current_song_paused = True
        self.mixer.music.pause()

    def unpause_loaded_song(self):
        self.playing = True
        self.current_song_paused = False
        self.mixer.music.unpause()

    def stop_loaded_song(self):
        self.playing = False
        self.current_song_paused = False
        self.mixer.music.stop()

    def unload_song(self):
        self.playing = False
        self.current_song_paused = False
        self.mixer.music.unload()

    def mute(self):
        self.is_muted = True
        self.set_mixer_volume(0)

    # state update
    def state_update(self):
        self.current_song_pos = self.get_current_song_pos()
        self.current_song_pos_percentage = round((self.current_song_pos / self.current_track_length),5)
        self.volume = int(self.get_mixer_volume()*100)
        if self.volume > 0:
            self.is_muted = False
        else:
            self.is_muted = True
        self.playing = self.get_mixer_busy()
        if not self.started:
            self.current_song_pos = 0
            self.current_song_pos_percentage = 0

    def update(self):
        self.state_update()

    # getters
    def get_current_song(self):
        return self.current_song_index
    
    def get_current_song_title(self):
        return self.current_track_title
    
    def get_current_song_pos(self):
        return self.mixer.music.get_pos()
    
    def get_mixer_busy(self):
        return self.mixer.music.get_busy()
    
    def get_mixer_volume(self):
        return self.mixer.music.get_volume()
    
    # setters
    def set_mixer_volume(self, vol):
        self.mixer.music.set_volume(vol/100)

    def bump_up_volume(self):
        self.volume += self.volume_increment
        if self.volume > 100:
            self.volume = 100
        elif self.volume < 0:
            self.volume = 0
        self.volume = int(self.volume)
        # print(self.volume)
        self.set_mixer_volume(self.volume)

    def bump_down_volume(self):
        self.volume -= self.volume_decrement
        if self.volume > 100:
            self.volume = 100
        elif self.volume < 0:
            self.volume = 0
        self.volume = int(self.volume)
        # print(self.volume)
        self.set_mixer_volume(self.volume)

    def set_new_current_song(self,index):
        self.unload_song()
        self.current_song_index = index
        self.current_song_pos = 0
        self.load_current_song()
        self.play_loaded_song()
        
    def skip_to_next_song(self):
        was_playing = self.playing
        self.unload_song()
        self.current_song_index = self.next_song_index
        self.current_song_pos = 0
        self.load_current_song()
        if was_playing:
            self.play_loaded_song()
        else:
            self.started = False
    
    def skip_to_previous_song(self):
        was_playing = self.playing
        self.unload_song()
        self.current_song_index = self.last_song_index
        self.current_song_pos = 0
        self.load_current_song()
        if was_playing:
            self.play_loaded_song()
        else:
            self.started = False

    def get_song_btn_1_song_name(self):
        return f'{self.app.menu_handler.menu.song_btn_1_idx + 1}.  {self.track_data[self.app.menu_handler.menu.song_btn_1_idx]['title']}'

    def get_song_btn_2_song_name(self):
        return f'{self.app.menu_handler.menu.song_btn_2_idx + 1}.  {self.track_data[self.app.menu_handler.menu.song_btn_2_idx]['title']}'
    
    def get_song_btn_3_song_name(self):
        return f'{self.app.menu_handler.menu.song_btn_3_idx + 1}.  {self.track_data[self.app.menu_handler.menu.song_btn_3_idx]['title']}'
    
    def get_song_btn_4_song_name(self):
        return f'{self.app.menu_handler.menu.song_btn_4_idx + 1}.  {self.track_data[self.app.menu_handler.menu.song_btn_4_idx]['title']}'
    
    def get_song_btn_5_song_name(self):
        return f'{self.app.menu_handler.menu.song_btn_5_idx + 1}.  {self.track_data[self.app.menu_handler.menu.song_btn_5_idx]['title']}'
    


