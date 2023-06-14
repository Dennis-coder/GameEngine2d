from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Scene.Scene import Scene

from abc import ABC
from .Scene.Components import *

class ProcessingSystem(ABC):
    interval: int or None = None
    buffered_time: int = 0
    is_active: bool = False

    @classmethod
    def process(cls, scene: Scene, dt: float):
        raise NotImplementedError()

class UpdateRunner(ProcessingSystem):
    is_active = True

    @classmethod
    def process(cls, scene: Scene, dt: float):
        for entity in scene.view(ScriptComponent):
            entity.script.update(dt)

class BoxCollisionSystem(ProcessingSystem):
    is_active = True

    @classmethod
    def process(cls, scene: Scene, dt: float):
        for entity in scene.view(BoxCollider):
            if not entity.box_collider.trigger:
                continue
            pos1 = entity.box_collider.position + entity.transform.position
            size1 = entity.box_collider.size * entity.transform.scale * entity.transform.size
            for entity2 in scene.view(BoxCollider):
                if entity == entity2:
                    continue

                pos2 = entity2.box_collider.position + entity2.transform.position
                size2 = entity2.box_collider.size * (entity2.transform.scale * entity2.transform.size)
                if abs(pos1.x-pos2.x) < size1.x/2 + size2.x/2 and abs(pos1.y-pos2.y) < size1.y/2 + size2.y/2:
                    entity.box_collider.trigger(entity2)