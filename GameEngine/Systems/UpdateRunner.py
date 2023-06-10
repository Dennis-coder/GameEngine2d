from __future__ import annotations
from typing import TYPE_CHECKING

from ..ECS import Entity
if TYPE_CHECKING:
    from ..Scene import Scene

from .System import ProcessingSystem
from ..Components import *


class UpdateRunner(ProcessingSystem):
    is_active = True

    @classmethod
    def process(cls, scene: Scene, dt: float):
        for (entity_id, script) in scene.registry.view([ScriptComponent]):
            entity = Entity(entity_id, scene)
            script.script.update(entity, dt)