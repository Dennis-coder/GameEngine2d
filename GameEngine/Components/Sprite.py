import pygame as pg
from .Component import Component
from ..GameObject import GameObject

class Sprite(Component):
    def __init__(self, obj: GameObject, image_path: str, layer: str, order: int):
        self.obj = obj
        self.image = pg.transform.scale(pg.image.load(image_path), (self.obj.transform.scale_x, self.obj.transform.scale_y))
        self.rect = self.image.get_rect(center=(self.obj.transform.x, self.obj.transform.y))
        self.layer = layer
        self.order = order