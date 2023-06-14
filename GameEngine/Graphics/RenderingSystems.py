from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..Scene.Scene import Scene

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
            image, _ = Assets.get(entity.sprite.image)
            size = entity.transform.size
            topleft = glm.vec2(-size[0]/2, -size[1]/2) + entity.transform.position
            bottomright = glm.vec2(size[0]/2, size[1]/2) + entity.transform.position

            topleft = view_matrix * (entity.transform.scale * topleft)
            bottomright = view_matrix * (entity.transform.scale * bottomright)
            pos = view_matrix * entity.transform.position

            new_image = pg.transform.scale(image, (bottomright.x - topleft.x, bottomright.y - topleft.y))
            surface.blit(new_image, new_image.get_rect(center=(pos.x, pos.y)))
                
class UnitLinesRenderer(RenderingSystem):
    is_active = True

    @classmethod
    def render(cls, scene: Scene, surface: pg.Surface):
        camera = scene.get_primary_camera()
        view_matrix = camera.camera.get_view_proj()

class BoxColliderRenderer(RenderingSystem):
    is_active = True

    @classmethod
    def render(cls, scene: Scene, surface: pg.Surface):
        camera = scene.get_primary_camera()
        view_matrix = camera.camera.get_view_proj()
        for entity in scene.view(BoxCollider):
            size = entity.box_collider.size * entity.transform.scale * entity.transform.size
            topleft = entity.transform.position - size/2
            bottomright = entity.transform.position + size/2

            topleft = view_matrix * topleft
            bottomright = view_matrix * bottomright
            pg.draw.lines(surface, (200,200,200), 1, [(topleft.x, topleft.y), (bottomright.x, topleft.y), (bottomright.x, bottomright.y), (topleft.x, bottomright.y)])