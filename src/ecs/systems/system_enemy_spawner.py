import pygame

import esper
from src.create.prefab_creator import crear_cuadrado
from src.ecs.events.e_spawn_data import SpawnEventData


def crear_rect(ecs_world: esper.World):
    spawn = SpawnEventData()
    levels = spawn.levels()
    enemies = spawn.enemies()

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
