from dataclasses import dataclass
import pygame as pg

@dataclass
class TransformComponent:
    x: int = 0
    y: int = 0
    scale_x: int = 1
    scale_y: int = 1

@dataclass
class TagComponent:
    tag: str = "Unnamed"

@dataclass
class SpriteComponent:
    image: pg.Surface
    layer: str = 'default'
    order: int = 0

@dataclass
class CameraComponent:
    width: int = 16
    height: int = 9
    clear_color: tuple[int, int, int] = (20,20,20)

@dataclass
class RigidbodyComponent:
    mass: int = 1
    drag: int = 0
    gravity_scale: int = 1

@dataclass
class ScriptComponent:
    script: any