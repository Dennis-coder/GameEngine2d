from __future__ import annotations
from typing import TYPE_CHECKING
import pygame as pg
if TYPE_CHECKING:
    from ..Scene import Scene
    from ..GameObject import GameObject

from .System import RenderingSystem
from ..Components import *
from pygame import Surface


class SpriteRenderer(RenderingSystem):
    is_active = True
    
    @classmethod
    def render(cls, scene: Scene, surface):
        for camera in scene.query([Camera]):
            for obj in scene.query([Sprite]):
                view_coords = (obj.transform.x - camera.transform.x, obj.transform.y - camera.transform.y)
                surface.blit(obj.sprite.image, obj.transform.image.get_rect(center=view_coords))

