from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..Scene import Scene

import pygame as pg 
import glm
from abc import ABC
from ..Scene.Components import *
from .Assets import Assets


class RenderingSystem(ABC):
    interval: int or None = None
    buffered_time: int = 0
    is_active: bool = False
    
    @classmethod
    def render(cls, scene: Scene, surface):
        raise NotImplementedError()

class SpriteRenderer(RenderingSystem):
    is_active = True
    
    @classmethod
    def render(cls, scene: Scene, surface: pg.Surface):
        camera = scene.get_primary_camera()
        view_matrix = camera.camera.get_view_proj()
        for entity in scene.view([SpriteComponent, TransformComponent]):
            image, size = Assets.get(entity.sprite.image)
            topleft = glm.vec4(entity.transform.position.x - size[0]/2, entity.transform.position.y - size[1]/2, 0, 1)
            bottomright = glm.vec4(topleft.x + size[0], topleft.y + size[1], 0, 1)

            topleft = view_matrix * topleft
            bottomright = view_matrix * bottomright
            pos = view_matrix * entity.transform.position

            new_image = pg.transform.scale(image, (bottomright.x - topleft.x, bottomright.y - topleft.y))
            surface.blit(new_image, new_image.get_rect(center=(pos.x, pos.y)))
                
class LineRenderer(RenderingSystem):
    is_active = True

    @classmethod
    def render(cls, scene: Scene, surface: pg.Surface):
        camera = scene.get_primary_camera()
        view_matrix = camera.camera.calc_view_proj(camera.transform.matrix)
