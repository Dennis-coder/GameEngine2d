import pygame as pg

class Assets:
    __assets__ = {}
    __pixels_per_unit__ = 32

    @classmethod
    def load_image(cls, image_path, name, pos=None, size=None):
        image = pg.image.load(image_path)

        if pos and size:
            new_image = pg.Surface(size)
            new_image.blit(image, (0,0), new_image.get_rect(topleft=pos))
            image = new_image
        
        cls.__assets__[name] = (image, (image.get_width()/cls.__pixels_per_unit__, image.get_height()/cls.__pixels_per_unit__))

    @classmethod
    def get(cls, name):
        return cls.__assets__[name]

    @classmethod
    def set_pixels_per_unit(cls, val: int) -> None:
        cls.__pixels_per_unit__ = val