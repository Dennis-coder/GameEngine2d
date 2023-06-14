import pygame as pg
from .Scene.Scene import Scene
from .Events.InputManager import InputManager

class Window:
    __active_scene__: Scene or None = None
    __scenes__: dict[str, Scene] = {}
    __show_fps__ = False
    __win_size__ = (640, 360)

    @classmethod
    def create_scene(cls, name: str):
        new_scene = Scene(name)
        cls.__scenes__[name] = new_scene
        return new_scene

    @classmethod
    def change_scene(cls, new_scene: str):
        cls.__active_scene__ = cls.__scenes__[new_scene]

    @classmethod
    def start(cls):
        pg.init()
        surface = pg.display.set_mode(cls.__win_size__)
        pg.display.set_caption(cls.__active_scene__.__name__)
        font = pg.font.SysFont(pg.font.get_default_font(), 16)

        clock = pg.time.Clock()
        cls.running = True
        scene = cls.__active_scene__
        while cls.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    cls.running = False
            
            InputManager.update()
            scene.update(clock.get_time() / 1000)
            scene.render(surface)

            if cls.__show_fps__:
                text = font.render(f"FPS: {int(clock.get_fps())}", True, (0, 255, 100))
                surface.blit(text, (cls.__win_size__[0]-50, 8))

            pg.display.update()
            clock.tick()
    
    @classmethod
    def set_show_fps(cls, val: bool) -> None:
        cls.__show_fps__ = val
    
    @classmethod
    def set_pixels_per_unit(cls, val: int) -> None:
        cls.__pixels_per_unit__ = val

    @classmethod
    def get_win_size(self):
        return self.__win_size__

    @classmethod
    def set_win_size(cls, new_size):
        cls.__win_size__ = new_size

    @classmethod
    def get_active_scene(cls):
        return cls.__active_scene__
