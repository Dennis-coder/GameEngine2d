from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .GameObject import GameObject

from abc import ABC, abstractclassmethod

class BaseScript(ABC):
    @abstractclassmethod
    def update(self, obj: GameObject, dt: float):
        raise NotImplementedError()