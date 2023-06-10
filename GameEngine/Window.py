import pygame as pg
from .Scene import Scene
from .ECS.Entity import Entity
from .InputManager import InputManager

class Window:
    active_scene: Scene or None = None
    scenes: dict[str, Scene] = {}
    show_fps = False

    @classmethod
    def create_scene(cls, name):
        new_scene = Scene(name)
        cls.scenes[name] = new_scene
        return new_scene

    @classmethod
    def get_active_scene(cls):
        return cls.active_scene
    
    @classmethod
    def change_scene(cls, new_scene: str):
        cls.active_scene = cls.scenes[new_scene]

    @classmethod
    def set_show_fps(cls, val: bool) -> None:
        cls.show_fps = val

    @classmethod
    def start(cls):
        pg.init()
        surface = pg.display.set_mode((640,360))
        pg.display.set_caption(cls.active_scene.name)
        font: pg.font.Font = pg.font.SysFont(pg.font.get_default_font(), 16)

        clock = pg.time.Clock()
        cls.running = True
        scene = cls.get_active_scene()
        while cls.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    cls.running = False
            
            InputManager.update()
            scene.update(clock.get_time() / 1000)
            scene.render(surface)

            if cls.show_fps:
                text = font.render(f"FPS: {int(clock.get_fps())}", True, (0, 255, 100))
                surface.blit(text, (590, 8))

            pg.display.update()
            clock.tick()
