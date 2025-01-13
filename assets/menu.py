import pygame as pg
from assets.yaml import safe_load
from assets.components.component import Component
from assets.components.label import Label
from assets.components.img import Img
from assets.components.button import Button
from assets.settings import *

class Menu:
    def __init__(self, id, menu_handler, audio_player):
        self.id = id
        self.menu_handler = menu_handler
        self.audio_player = audio_player
        self.song_selection_on_second_page = False
        self.menu_setup(self.id)

    def menu_setup(self, id):
        # importing data
        with open(resource_path(f'assets/menu_config/{id}.yml')) as file:
            self.data = safe_load(file)

        # creating component groups
        self.visible_components = pg.sprite.Group()
        self.header_components = ComponentGroup()
        self.header = None
        self.body_components = ComponentGroup()
        self.body = None
        self.footer_components = ComponentGroup()
        self.footer = None
        self.build_components()

    def build_components(self):
        # build body
        body_pos = (0,0)
        body_perc = self.data['parts']['body']['info']['perc']
        body_bgcolor = self.data['parts']['body']['info']['bgcolor']
        body_height = int(WIN_HEIGHT * body_perc)
        body_width = WIN_WIDTH
        self.body = Component([self.visible_components, self.body_components],body_pos,body_width,body_height,z=1,part=1,bgcolor=body_bgcolor)
        Img([self.visible_components, self.body_components],resource_path('assets/images/cover.png'),(30,61),1,part=3)
        self.song_btn_1 = Button([self.visible_components, self.body_components],(500,61),675,75,1,part=3,bgcolor='black',hover_behavior=True)
        self.song_btn_2 = Button([self.visible_components, self.body_components],(500,155),675,75,1,part=3,bgcolor='black',hover_behavior=True)
        self.song_btn_3 = Button([self.visible_components, self.body_components],(500,248),675,75,1,part=3,bgcolor='black',hover_behavior=True)
        self.song_btn_4 = Button([self.visible_components, self.body_components],(500,342),675,75,1,part=3,bgcolor='black',hover_behavior=True)
        self.song_btn_5 = Button([self.visible_components, self.body_components],(500,435),675,75,1,part=3,bgcolor='black',hover_behavior=True)
        self.load_song_names()
        self.song_btn_1_label = Label([self.visible_components, self.body_components],'','futura',21,'white',(self.song_btn_1.rect.centerx-325,self.song_btn_1.rect.centery),z=2,part=3,which_pos='midleft',dynamic_func=self.audio_player.get_song_btn_1_song_name)
        self.song_btn_2_label = Label([self.visible_components, self.body_components],'','futura',21,'white',(self.song_btn_2.rect.centerx-325,self.song_btn_2.rect.centery),z=2,part=3,which_pos='midleft',dynamic_func=self.audio_player.get_song_btn_2_song_name)
        self.song_btn_3_label = Label([self.visible_components, self.body_components],'','futura',21,'white',(self.song_btn_3.rect.centerx-325,self.song_btn_3.rect.centery),z=2,part=3,which_pos='midleft',dynamic_func=self.audio_player.get_song_btn_3_song_name)
        self.song_btn_4_label = Label([self.visible_components, self.body_components],'','futura',21,'white',(self.song_btn_4.rect.centerx-325,self.song_btn_4.rect.centery),z=2,part=3,which_pos='midleft',dynamic_func=self.audio_player.get_song_btn_4_song_name) 
        self.song_btn_5_label = Label([self.visible_components, self.body_components],'','futura',21,'white',(self.song_btn_5.rect.centerx-325,self.song_btn_5.rect.centery),z=2,part=3,which_pos='midleft',dynamic_func=self.audio_player.get_song_btn_5_song_name)
        # build header
        header_pos = (0,0)
        header_perc = self.data['parts']['header']['info']['perc']
        header_bgcolor = self.data['parts']['header']['info']['bgcolor']
        header_height = int(WIN_HEIGHT * header_perc)
        header_width = WIN_WIDTH
        self.header = Component([self.visible_components, self.header_components],header_pos,header_width,header_height,z=1,part=2,bgcolor=header_bgcolor)
        Label([self.visible_components, self.header_components],"JOHNIFY", 'futura', 15, (15,15,15), (8,8), 2, part=2, bgcolor=None)
        self.page_button = Img([self.visible_components, self.footer_components],resource_path('assets/images/next_page.png'),(1175,8),2,part=2,which_pos='topleft',dynamic=True,second_img_path=resource_path('assets/images/last_page.png'))
        # build footer
        footer_pos = (0,WIN_HEIGHT)
        footer_perc = self.data['parts']['footer']['info']['perc']
        footer_bgcolor = self.data['parts']['footer']['info']['bgcolor']
        footer_height = int(WIN_HEIGHT * footer_perc)
        footer_width = WIN_WIDTH
        self.footer = Component([self.visible_components, self.footer_components],footer_pos,footer_width,footer_height,z=1,part=3,bgcolor=footer_bgcolor,which_pos='bottomleft')
        Img([self.visible_components, self.footer_components],resource_path('assets/images/cover-min.png'),(20,558),1,part=3)
        Label([self.visible_components, self.footer_components],self.audio_player.current_track_title,'futura',15,'white',(133,593),z=1,part=3,dynamic_func=self.audio_player.get_current_song_title)
        Label([self.visible_components, self.footer_components],'Summer 2000','futura',14,'white',(133,615),z=1,part=3)
        self.track_bar = Component([self.visible_components, self.footer_components],(586,650),550,17,z=1,part=3,bgcolor=(200,200,200),which_pos='bottomleft')
        self.track_pos_bar = Component([self.visible_components, self.footer_components],(586,650),17,17,z=2,part=3,bgcolor=(30,215,96),which_pos='bottomleft')
        self.play_pause = Img([self.visible_components, self.footer_components],resource_path('assets/images/play.png'),(self.track_bar.rect.centerx,self.track_bar.rect.centery-55),2,part=3,which_pos='center',dynamic=True,second_img_path=resource_path('assets/images/pause.png'))
        self.skip_forward = Img([self.visible_components, self.footer_components],resource_path('assets/images/forward.png'),(self.track_bar.rect.centerx+55,self.track_bar.rect.centery-55),2,part=3,which_pos='center')
        self.skip_backward = Img([self.visible_components, self.footer_components],resource_path('assets/images/backward.png'),(self.track_bar.rect.centerx-55,self.track_bar.rect.centery-55),2,part=3,which_pos='center')
    
    def load_song_names(self):
        multiplier = 1 if self.song_selection_on_second_page else 0
        self.song_btn_1_idx = 0 + (5 * multiplier)
        self.song_btn_2_idx = 1 + (5 * multiplier)
        self.song_btn_3_idx = 2 + (5 * multiplier)
        self.song_btn_4_idx = 3 + (5 * multiplier)
        self.song_btn_5_idx = 4 + (5 * multiplier)

    def handle_events(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                if self.audio_player.playing:
                    self.audio_player.pause_loaded_song()
                elif not self.audio_player.playing and not self.audio_player.current_song_paused:
                    self.audio_player.play_loaded_song()
                else:
                    self.audio_player.unpause_loaded_song()
            elif event.key == pg.K_RIGHT:
                self.audio_player.skip_to_next_song()
            elif event.key == pg.K_LEFT:
                self.audio_player.skip_to_previous_song()
            elif event.key == pg.K_UP:
                self.audio_player.bump_up_volume()
            elif event.key == pg.K_DOWN:
                self.audio_player.bump_down_volume()
            elif event.key == pg.K_1:
                self.audio_player.set_new_current_song(0)
            elif event.key == pg.K_2:
                self.audio_player.set_new_current_song(1)
            elif event.key == pg.K_3:
                self.audio_player.set_new_current_song(2)
            elif event.key == pg.K_4:
                self.audio_player.set_new_current_song(3)
            elif event.key == pg.K_5:
                self.audio_player.set_new_current_song(4)
            elif event.key == pg.K_6:
                self.audio_player.set_new_current_song(5)
            elif event.key == pg.K_7:
                self.audio_player.set_new_current_song(6)
            elif event.key == pg.K_8:
                self.audio_player.set_new_current_song(7)
            elif event.key == pg.K_9:
                self.audio_player.set_new_current_song(8)
            elif event.key == pg.K_0:
                self.audio_player.set_new_current_song(9)
        elif event.type == pg.MOUSEBUTTONDOWN:
            if self.play_pause.rect.collidepoint(pg.mouse.get_pos()):
                if self.audio_player.playing:
                    self.audio_player.pause_loaded_song()
                elif not self.audio_player.playing and not self.audio_player.current_song_paused:
                    self.audio_player.play_loaded_song()
                else:
                    self.audio_player.unpause_loaded_song()
            elif self.skip_forward.rect.collidepoint(pg.mouse.get_pos()):
                self.audio_player.skip_to_next_song()
            elif self.skip_backward.rect.collidepoint(pg.mouse.get_pos()):
                self.audio_player.skip_to_previous_song()
            elif self.page_button.rect.collidepoint(pg.mouse.get_pos()):
                self.song_selection_on_second_page = not self.song_selection_on_second_page
                self.load_song_names()
            elif self.song_btn_1.rect.collidepoint(pg.mouse.get_pos()):
                self.audio_player.set_new_current_song(self.song_btn_1_idx)
            elif self.song_btn_2.rect.collidepoint(pg.mouse.get_pos()):
                self.audio_player.set_new_current_song(self.song_btn_2_idx)
            elif self.song_btn_3.rect.collidepoint(pg.mouse.get_pos()):
                self.audio_player.set_new_current_song(self.song_btn_3_idx)
            elif self.song_btn_4.rect.collidepoint(pg.mouse.get_pos()):
                self.audio_player.set_new_current_song(self.song_btn_4_idx)
            elif self.song_btn_5.rect.collidepoint(pg.mouse.get_pos()):
                self.audio_player.set_new_current_song(self.song_btn_5_idx)
        elif event.type == MUSIC_END:
            self.audio_player.skip_to_next_song()

    def update(self, dt):
        self.body_components.update(dt)
        self.header_components.update(dt)
        self.footer_components.update(dt)
        self.track_pos_bar.update_track_bar(self.audio_player.current_song_pos_percentage)
        self.play_pause.dynamic_image(self.audio_player.playing)
        self.page_button.dynamic_image(self.song_selection_on_second_page)

    def render(self):
        self.body_components.custom_draw()
        self.header_components.custom_draw()
        self.footer_components.custom_draw()

class ComponentGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.is_visible = True

    def custom_draw(self):
        if self.is_visible:
            for comp in sorted(self.sprites(), key=lambda comp: comp.true_z):
                self.display_surface.blit(comp.surface, comp.rect)
    
    def toggle_visibility(self):
        self.is_visible = not self.is_visible

    

