from python_json_config import ConfigBuilder


class SpawnEventData:
    def __init__(self):
        self.builder = ConfigBuilder()

    def enemies(self):
        enemies = self.builder.parse_config('src/configs/enemies.json')
        return enemies

    def levels(self):
        levels = self.builder.parse_config('src/configs/level_01.json')
        return levels
