from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..Scene import Scene

class Entity:
    def __init__(self, entity_id: int, scene: Scene):
        self.entity_id: int = entity_id
        self.scene: Scene = scene
    
    def add_component(self, component, *args, **kwargs):
        return self.scene.registry.emplace(self.entity_id, component, *args, *kwargs)
    
    def remove_component(self, component):
        self.scene.registry.erase(self.entity_id, component)

    def has_component(self, component):
        return self.scene.registry.has(self.entity_id, component)

    def get_component(self, components):
        return self.scene.registry.get(self.entity_id, components)

    def __getitem__(self, component):
        return self.get_component(component)