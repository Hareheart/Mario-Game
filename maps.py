import pygame
from layerinfo import import_csv_layout

class mapdata:
    def __init__(self, map_data, surface):
        self.display_surface = surface
        tlayout = import_csv_layout(map_data['Main'])
        self.terrain_sprites = self.create_tile_group(tlayout, 'Main')
    def create_tile_group(self, layout, type):
        tilesize = 16
        sprite_group = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tilesize
                    y = row_index * tilesize

                    if type == 'Main':
                        sprite = Tile(tilesize,x,y) 
                        sprite_group.add(sprite)
        return sprite_group
    def run(self):
        self.terrain_sprites.draw(self.display_surface)

class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = (x, y))