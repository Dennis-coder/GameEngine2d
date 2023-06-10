from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..Scene import Scene
    from ..GameObject import GameObject

from .System import ProcessingSystem
from ..Components import *


class UpdateRunner(ProcessingSystem):
    is_active = True

    @classmethod
    def process(cls, scene: Scene, dt: float):
        for obj in scene.query([Script]):
            obj.script.script.update(obj, dt)