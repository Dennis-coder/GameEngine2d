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