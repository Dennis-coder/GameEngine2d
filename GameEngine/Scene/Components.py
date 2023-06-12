from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .Entity import Entity

import pygame as pg
import glm
from ..Graphics.Camera import Camera
from abc import ABC, abstractmethod



class TransformComponent:
    def __init__(self):
        self.transform = Transform()

class Transform:
    def __init__(self):
        self.__matrix__ = glm.mat4()
    
    def translate(self, dpos):
        self.__matrix__ = glm.translate(self.__matrix__, dpos)
    
    @property
    def position(self):
        return self.__matrix__[3]
    
    @property
    def matrix(self):
        return self.__matrix__

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

class RigidbodyComponent:
    def __init__(self):
        self.mass = 1
        self.drag = 0
        self.gravity_scale = 1