from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .Entity import Entity

import glm
from ..Graphics.Camera import Camera
from abc import ABC, abstractmethod


class TransformComponent:
    def __init__(self):
        self.size = glm.vec2()
        self.scale = glm.mat2()
        self.position = glm.vec2()
        self.rotation = 0

class TagComponent:
    def __init__(self, tag="Unnamed"):
        self.tag = tag

class SpriteComponent:
    def __init__(self, image, layer="default", order=0):
        self.image = image
        self.layer = layer
        self.order = order

class CameraComponent:
    def __init__(self, win_size, size, transform):
        self.camera = Camera(win_size, size, transform)

class ScriptComponent:
    def __init__(self, script):
        self.script = script

class BaseScript(ABC):
    @abstractmethod
    def update(self, obj: Entity, dt: float):
        raise NotImplementedError()
    
class BoxCollider:
    def __init__(self, position, size, trigger=None):
        self.position = glm.vec2(*position)
        self.size = glm.mat2(*size)
        self.trigger = trigger
        self.collided_with_last_frame = set()

class CircleCollider:
    def __init__(self, position, size, trigger):
        self.position = glm.vec2(*position)
        self.size = size
        self.trigger = trigger
        self.collided_with_last_frame = set()

class RigidbodyComponent:
    def __init__(self):
        self.mass = 1
        self.drag = 0
        self.gravity_scale = 1