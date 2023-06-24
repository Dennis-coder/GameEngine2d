import pygame as pg
from .Scene.Scene import Scene
from .Scene.Entity import Entity
from .Scene.Components import CameraComponent
from .Events.InputManager import InputManager

class Window:
    __active_scene__: Scene or None = None
    __scenes__: dict[str, Scene] = {}
    __show_fps__ = False
    __win_size__ = (640, 360)
    __max_fps__ = 60

    @classmethod
    def create_scene(cls, name: str) -> tuple[Scene, Entity]:
        new_scene = Scene(name)
        cls.__scenes__[name] = new_scene
        camera = new_scene.create_entity()
        camera.add_component(CameraComponent, Window.get_win_size(), (9, 5), camera.transform)
        new_scene.set_primary_camera(camera)
        cls.__active_scene__ = new_scene
        return new_scene, camera

    @classmethod
    def start_prod(cls):
        pg.init()
        surface = pg.display.set_mode(cls.__win_size__)
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
            clock.tick(cls.__max_fps__)

    @classmethod
    def start_dev(cls):
        pg.init()
        surface = pg.display.set_mode(cls.__win_size__)
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
            clock.tick(cls.__max_fps__)
    
    @classmethod
    def get_fps(cls) -> int:
        return cls.__max_fps__
    @classmethod
    def set_fps(cls, val) -> None:
        cls.__max_fps__ = val

    @classmethod
    def get_show_fps(cls) -> bool:
        return cls.__show_fps__
    @classmethod
    def set_show_fps(cls, val: bool) -> None:
        cls.__show_fps__ = val

    @classmethod
    def get_pixels_per_unit(self) -> int:
        return self.__pixels_per_unit__
    @classmethod
    def set_pixels_per_unit(cls, val: int) -> None:
        cls.__pixels_per_unit__ = val

    @classmethod
    def get_win_size(self) -> tuple[int, int]:
        return self.__win_size__
    @classmethod
    def set_win_size(cls, new_size) -> None:
        cls.__win_size__ = new_size

    @classmethod
    def get_active_scene(cls) -> Scene:
        return cls.__active_scene__
    @classmethod
    def set_active_scene(cls, scene_name: str) -> None:
        cls.__active_scene__ = cls.__scenes__[scene_name]
        pg.display.set_caption(scene_name)