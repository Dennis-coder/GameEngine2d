from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pygame import Surface

from ..EnTT.Registry import Registry
from .Entity import Entity
from .Components import *
from ..ProcessingSystems import *
from ..Graphics.RenderingSystems import *

class Scene:
    def __init__(self, name: str):
        self.__name__ = name
        self.__registry__ = Registry()
        self.__processing_systems__: list = [
            UpdateRunner(self),
            BoxCollisionSystem(self),
        ]
        self.__rendering_systems__: list = [
            # UnitLinesRenderer,
            SpriteRenderer,
            # BoxColliderRenderer,
        ]
        self.__primary_camera__ = None

    def update(self, dt: int) -> None:
        for system in self.__processing_systems__:
            if not system.is_active:
                continue
            if system.interval:
                system.buffered_time += dt
                while system.buffered_time >= system.interval:
                    system.process(dt)
                    system.buffered_time -= system.interval
            else:
                system.process(dt)
    
    def render(self, surface: Surface):
        surface.fill((20,20,20))
        for system in self.__rendering_systems__:
            if system.is_active:
                system.render(self, surface)

    def create_entity(self):
        entity = Entity(self.__registry__.create(), self)
        entity.add_component(TransformComponent)
        entity.add_component(TagComponent)
        return entity
    
    def view(self, components):
        for entity_id in self.__registry__.view(components):
            yield Entity(entity_id, self)
    
    def set_primary_camera(self, camera):
        self.__primary_camera__ = camera
    
    def get_primary_camera(self) -> Entity:
        return self.__primary_camera__

    @property
    def name(self):
        return self.__name__
