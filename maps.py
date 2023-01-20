import pygame
from layerinfo import import_csv_layout, import_cut_graphics, stattile
class mapdata1:
    def __init__(self, map_data, surface):
        # general setup
        self.display = surface
        self.world_shift = 0

        # terrain setup
        tlayout = import_csv_layout(map_data['Main'])
        self.terrain_sprites = self.create_tile_group(tlayout, 'Main')
    def create_tile_group(self, layout, type):
        enemysize = 29 # size of melee enemy
        tilesize = 16 # Pixels each tile is (16x16)
        sprite_group = pygame.sprite.Group() #The group each sprite is in
        for row_index, row in enumerate(layout):
            for col_index,val in enumerate(row):
                if val != '-1':
                    if type == 'main':
                        x = col_index * tilesize
                        y = row_index * tilesize
                        tilesheet1 = import_cut_graphics('../Mario-Game/terrain.png')
                        tilesurf = tilesheet1[int(val)]
                        sprite = stattile(tilesize, x, y, tilesurf) 
                        sprite_group.add(sprite)  
        return sprite_group

    def enemy_collision_reverse(self):
        for enemy in self.enemy_sprites.sprites():
            if pygame.sprite.spritecollide(enemy,self.constraint_sprites,False):
                enemy.reverse()

    def run(self):
        # map run
        self.terrain_sprites.draw(self.display)
        self.terrain_sprites.update(self.world_shift)




