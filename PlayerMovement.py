from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from GameEngine import Entity

from GameEngine import Input, BaseScript
from GameEngine.Components import *
import pygame as pg

class PlayerMovement(BaseScript):
    @classmethod
    def update(cls, entity: Entity, dt: float):
        transform, = entity.get_component([TransformComponent])

        dx: int = Input.get_key_pressed(pg.K_d) - Input.get_key_pressed(pg.K_a)
        dy: int = Input.get_key_pressed(pg.K_s) - Input.get_key_pressed(pg.K_w)

        transform.x += 200*dt*dx
        transform.y += 200*dt*dy