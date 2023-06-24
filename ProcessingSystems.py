from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Scene.Scene import Scene

from abc import ABC
from .Scene.Components import *

class ProcessingSystem(ABC):
    def __init__(self, scene: Scene, is_active: bool=True, interval: int=None):
        self.is_active = is_active
        self.interval: int or None = interval
        self.buffered_time: int = 0
        self.scene = scene

class UpdateRunner(ProcessingSystem):
    def process(self, dt: float):
        for entity in self.scene.view(ScriptComponent):
            entity.script.update(dt)

class BoxCollisionSystem(ProcessingSystem):
    def process(self, dt: float):
        for entity in self.scene.view(BoxCollider):
            if not entity.box_collider.trigger:
                continue
            pos1 = entity.box_collider.position + entity.transform.position
            size1 = entity.box_collider.size * entity.transform.scale * entity.transform.size
            for entity2 in self.scene.view(BoxCollider):
                if entity == entity2:
                    continue

                pos2 = entity2.box_collider.position + entity2.transform.position
                size2 = entity2.box_collider.size * (entity2.transform.scale * entity2.transform.size)
                if abs(pos1.x-pos2.x) < size1.x/2 + size2.x/2 and abs(pos1.y-pos2.y) < size1.y/2 + size2.y/2:
                    if entity2.entity_id not in entity.box_collider.collided_with_last_frame:
                        entity.box_collider.trigger(entity2)
                        entity.box_collider.collided_with_last_frame.add(entity2.entity_id)
                elif entity2.entity_id in entity.box_collider.collided_with_last_frame:
                    entity.box_collider.collided_with_last_frame.remove(entity2.entity_id)