from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..Scene import Scene
    from pygame import Surface

from ..ECS import Entity
from .System import RenderingSystem
from ..Components import *


class SpriteRenderer(RenderingSystem):
    is_active = True
    
    @classmethod
    def render(cls, scene: Scene, surface: Surface):
        for (camera_id, camera, camera_transform) in scene.registry.view([CameraComponent, TransformComponent]):
            for (entity_id, entity_sprite, entity_transform) in scene.registry.view([SpriteComponent, TransformComponent]):
                view_coords = (entity_transform.x - camera_transform.x, entity_transform.y - camera_transform.y)
                surface.blit(entity_sprite.image, entity_sprite.image.get_rect(center=view_coords))

