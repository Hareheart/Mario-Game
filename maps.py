import pygame
from layerinfo import import_csv_layout, import_cut_graphics, stattile
from characters import Player, Enemy, Boss, MiniBoss
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

    def horizontalcollision(self, damage):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        collidable_sprites = self.enemy_sprites.sprites() + self.boss_sprite.sprite() + self.miniboss_sprites.sprite()
        for sprite in collidable_sprites:
            if player.rect == collidable_sprites:
                player.health -= 1
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0: 
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right
        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False



    def enemy_collision_reverse(self):
        for enemy in self.enemy_sprites.sprites():
            if pygame.sprite.spritecollide(enemy,self.constraint_sprites,False):
                enemy.reverse()


    def run(self):
        # map run
        self.terrain_sprites.draw(self.display)
        self.terrain_sprites.update(self.world_shift)
        # player run
        self.player.update()
        self.horizontal_movement_collision()
        self.scroll_x()
        self.player.draw(self.display_surface)
        self.goal.update(self.world_shift)
        self.goal.draw(self.display_surface)
