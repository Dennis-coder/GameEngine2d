from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .Systems import ProcessingSystem, RenderingSystem
    from pygame import Surface

from .ECS import Registry, Entity
from .Components import *
from .Systems import *

class Scene:
    def __init__(self, name: str):
        self.name: str = name
        self.registry: Registry = Registry()
        self.processing_systems: list[ProcessingSystem] = [
            UpdateRunner
        ]
        self.rendering_systems: list[RenderingSystem] = [
            SpriteRenderer
        ]

    def update(self, dt: int) -> None:
        for system in self.processing_systems:
            if not system.is_active:
                continue
            if system.interval:
                system.buffered_time += dt
                while system.buffered_time >= system.interval:
                    system.process(self, dt)
                    system.buffered_time -= system.interval
            else:
                system.process(self, dt)
    
    def render(self, surface: Surface):
        surface.fill(((20,20,20)))
        for system in self.rendering_systems:
            if not system.is_active:
                continue
            system.render(self, surface)

    def create_entity(self):
        entity = Entity(self.registry.create(), self)
        entity.add_component(TransformComponent)
        entity.add_component(TagComponent)
        return entity
