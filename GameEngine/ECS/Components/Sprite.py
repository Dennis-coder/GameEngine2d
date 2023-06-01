# import pygame as pg
from ..Component import Component

class Sprite(Component):
    def __init__(self, image_path: str, layer: str="default", order: int=0):
        # self.image = pg.image.load(image_path)
        self.layer = layer
        self.order = order