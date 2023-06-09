import pygame

import esper
from src.ecs.systems.system_enemy_spawner import crear_rect
from src.ecs.systems.s_movement import system_movement
from src.ecs.systems.s_rendering import system_rendering
from src.ecs.systems.s_screen_bounce import system_screen_bounce
from python_json_config import ConfigBuilder


def _clean():
    pygame.quit()


class GameEngine:
    def __init__(self) -> None:
        builder = ConfigBuilder()
        data = builder.parse_config('src/configs/window.json')
        self.title = data.title
        self.size = data.size
        self.background = data.bg_color
        self.framerate = data.framerate
        self.screen = pygame.display.set_mode((self.size.w, self.size.h), pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.is_running = False
        self.framerate = self.framerate
        self.delta_time = 0
        self.ecs_world = esper.World()
        pygame.display.set_caption(self.title)

    def run(self) -> None:
        self._create()
        self.is_running = True
        while self.is_running:
            self._calculate_time()
            self._process_events()
            self._update()
            self._draw()
        _clean()

    def _create(self):
        crear_rect(self.ecs_world)

    def _calculate_time(self):
        self.clock.tick(self.framerate)
        self.delta_time = self.clock.get_time() / 1000.0

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def _update(self):
        system_movement(self.ecs_world, self.delta_time)
        system_screen_bounce(self.ecs_world, self.screen)

    def _draw(self):
        self.screen.fill((self.background.r, self.background.g, self.background.b))
        system_rendering(self.ecs_world, self.screen)
        pygame.display.flip()
