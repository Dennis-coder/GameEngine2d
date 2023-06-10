from __future__ import annotations
from typing import TYPE_CHECKING
from Components import *
if TYPE_CHECKING:
    from .BaseScript import BaseScript

class GameObject:
    def __init__(self, x: int=0, y: int=0, scale_x: int=1, scale_y: int=1):
        self.components: set[Component] = set()

        # self.x = x
        # self.y = y
        # self.scale_x = scale_x
        # self.scale_y = scale_y

        self.add_transform(x, y, scale_x, scale_y)
    
    def remove_component(self, component: Component):
        self.components.remove(component)
        return self

    def add_camera(self, size: int=5):
        self.camera = Camera(self, size)
        self.components.add(Camera)
        return self

    def add_rigidbody(self, mass: int=1, drag: int=0, gravity_scale: int=1):
        self.rigidbody = Rigidbody(self, mass, drag, gravity_scale)
        self.components.add(Rigidbody)
        return self

    def add_script(self, script: BaseScript):
        self.script = Script(self, script)
        self.components.add(Script)
        return self

    def add_sprite(self, image_path: str):
        self.sprite = Sprite(self, image_path, "default", 0)
        self.components.add(Sprite)
        return self

    def add_transform(self, x: int=0, y: int=0, scale_x: int=1, scale_y: int=1):
        self.transform = Transform(self, x, y, scale_x, scale_y)
        self.components.add(Transform)
        return self


    def __getitem__(self, component: Component):
        return self.components[component]