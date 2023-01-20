from csv import reader
import pygame

level_1 = {
    'Main': 'map1/map1_Main .csv',
    'Enemies': 'map1/map1_Enemies.csv',
    'miniboss': 'map1/map1_Enemies Borders.csv',
    'Lava': 'map1/map1_Lava.csv'}

def import_cut_graphics(path):
    tile_size = 16
    surface = pygame.image.load(path).convert_alpha()
    tilenum_x = int(surface.get_size()[0] / tile_size)
    tilenum_y = int(surface.get_size()[1] / tile_size)

    cuttiles = []

    for row in range(tilenum_y): 
        for col in range(tilenum_x):
            x = col * tile_size
            y = row * tile_size
            newsurf = pygame.Surface((tile_size,tile_size), flags = pygame.SRCALPHA)
            newsurf.blit(surface,(0, 0), pygame.Rect(x,y,tile_size,tile_size))
            cuttiles.append(newsurf)
    return cuttiles


class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, shift):  # Camera
        self.rect.x += shift
class stattile(Tile):
    def __init__(self, size, x, y, surface):
        super().__init__(size, x, y)
        self.image = surface
        

def import_csv_layout(path):
    terr_map = []
    with open(path) as map:
        level = reader(map, delimiter = ',')
        for row in level:
            terr_map.append(list(row))
        return terr_map
