from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .Scene import Scene

from .Components import *

class Entity:
    def __init__(self, entity_id: int, scene: Scene):
        self.entity_id: int = entity_id
        self.scene: Scene = scene
    
    def add_component(self, component, *args, **kwargs):
        return self.scene.__registry__.emplace(self.entity_id, component, *args, *kwargs)
    
    def remove_component(self, component):
        self.scene.__registry__.erase(self.entity_id, component)

    def has_component(self, components):
        return self.scene.__registry__.has(self.entity_id, components)

    def get_component(self, components):
        return self.scene.__registry__.get(self.entity_id, components)

    @property
    def transform(self) -> TransformComponent:
        return self.get_component(TransformComponent)
    
    @property
    def tag(self) -> str:
        return self.get_component(TagComponent).tag

    @property
    def camera(self) -> Camera:
        return self.get_component(CameraComponent).camera
    
    @property
    def sprite(self) -> SpriteComponent:
        return self.get_component(SpriteComponent)
    
    @property
    def script(self) -> BaseScript:
        return self.get_component(ScriptComponent).script
    
    @property
    def box_collider(self) -> BoxCollider:
        return self.get_component(BoxCollider)

    def __getitem__(self, component):
        return self.get_component(component)
    
    def __eq__(self, other: Entity):
        return self.entity_id == other.entity_id