from .Component import Component

class Rigidbody(Component):
    def __init__(self, obj, mass: int, drag: int, gravity_scale: int):
        self.obj = obj