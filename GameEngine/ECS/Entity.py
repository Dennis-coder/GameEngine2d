from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .Component import Component
    from ..Scene import Scene

class UID:
    id: int = 0
    @classmethod
    def get(cls):
        cls += 1
        return cls.id

class Entity:
    def __init__(self, scene: Scene, components: list[Component]):
        self.id = UID.get()
        self.scene = scene
        self.components = {}
        for component in components:
            self.add(component)
    
    def add(self, component: Component):
        self.components[component.__class__] = component
    
    def remove(self, component: Component):
        self.components.pop(component)
    
    def __getitem__(self, component: Component):
        return self.components[component]