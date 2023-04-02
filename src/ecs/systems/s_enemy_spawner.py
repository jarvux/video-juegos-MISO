
import pygame
import esper
from src.create.prefab_creator import crear_cuadrado
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_enemy_spawner import CEnemySpawner
from src.ecs.events.e_spawn_data import getData
def crear_rect(ecs_world:esper.World): 
    enemies = getData('src/config/enemies.json') 
    levels  = getData('src/config/level_01.json') 
    for enemie in levels['enemy_spawn_events'] : 
        if not enemie :
           continue
        config = enemies[enemie['enemy_type']]
        crear_cuadrado(ecs_world,
                    pygame.Vector2(config['size']['x'],config['size']['y']),
                    pygame.Vector2(enemie['position']['x'],enemie['position']['y']),
                    pygame.Vector2(config['velocity_min'],config['velocity_max']),
                    pygame.Color(config['color']['r'],config['color']['g'],config['color']['b']),
                    enemie['time']
                    )
    