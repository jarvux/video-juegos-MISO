import pygame

import esper
from src.create.prefab_creator import crear_cuadrado
from python_json_config import ConfigBuilder

builder = ConfigBuilder()


def crear_rect(ecs_world: esper.World):

    levels = builder.parse_config('src/config/level_01.json')
    enemies = builder.parse_config('src/config/enemies.json')

    for level in levels.enemy_spawn_events:
        if not level:
            continue

        time = level['time']
        enemy_type = level['enemy_type']
        position = level['position']
        enemy = getattr(enemies, enemy_type)

        if enemy is None:
            continue

        crear_cuadrado(ecs_world,
                       pygame.Vector2(enemy.size.x, enemy.size.y),
                       pygame.Vector2(position['x'], position['y']),
                       pygame.Vector2(enemy.velocity_min, enemy.velocity_max),
                       pygame.Color(enemy.color.r, enemy.color.g, enemy.color.b),
                       time)
