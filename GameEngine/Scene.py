from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .GameObject import GameObject
    from .Components import Component
    from .Systems import ProcessingSystem, RenderingSystem
    from pygame import Surface

import GameEngine.Components
import inspect
from .Systems import *

class Scene:
    def __init__(self, name):
        self.name = name
        self.objects: dict[Component: set[GameObject]] = {
            cls_obj: set()
            for _, cls_obj in inspect.getmembers(GameEngine.Components)
            if inspect.isclass(cls_obj)
        }
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

    def add_object(self, obj: GameObject) -> None:
        for component in obj.components.keys():
            self.objects[component].add(obj)

    def remove_object(self, obj: GameObject) -> None:
        self.objects.remove(obj)

    def query(self, filter: list[Component]):
        objects: set = self.objects[filter[0]]
        for component in filter[1:]:
            objects.intersection_update(self.objects[component])
        return objects
        
    def make_active_scene(self):
        Scene.active_scene = self
