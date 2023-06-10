from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..ECS.Entity import Entity
    from ..Scene import Scene

from abc import ABC, abstractclassmethod

class ProcessingSystem(ABC):
    interval: int or None = None
    buffered_time: int = 0
    is_active: bool = False

    @classmethod
    def process(cls, scene: Scene, dt: float):
        raise NotImplementedError()

class RenderingSystem(ABC):
    interval: int or None = None
    buffered_time: int = 0
    is_active: bool = False
    
    @classmethod
    def render(cls, scene: Scene, surface):
        raise NotImplementedError()