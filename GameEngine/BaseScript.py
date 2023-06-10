from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .ECS.Entity import Entity

from abc import ABC, abstractclassmethod

class BaseScript(ABC):
    @abstractclassmethod
    def update(self, obj: Entity, dt: float):
        raise NotImplementedError()