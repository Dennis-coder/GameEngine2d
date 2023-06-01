from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
if TYPE_CHECKING:
    from .Entity import Entity
    from .Component import Component
    from ..Scene import Scene

class System(ABC):
    filter: list[Component] or None = None
    interval: int or None = None
    buffered_time: int = 0
    def __init__(self, scene: Scene):
        self.scene = scene
        self.is_active = True

    def update(self, dt: int):
        for entity in self.scene.query(self.filter):
            self.process(entity, dt)
    
    @abstractmethod
    def process(self, entity: Entity, dt: int):
        raise NotImplementedError()