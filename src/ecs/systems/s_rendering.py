import esper
import pygame
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_enemy_spawner import CEnemySpawner
def system_rendering(world:esper.World,screen:pygame.Surface):
    components = world.get_components(CTransform, CSurface,CEnemySpawner)
    c_t:CTransform
    c_s:CSurface
    c_e:CEnemySpawner
    for entity, (c_t,c_s,c_e) in components:
        if(pygame.time.get_ticks() > c_e.time):
           screen.blit(c_s.surf,c_t.pos)