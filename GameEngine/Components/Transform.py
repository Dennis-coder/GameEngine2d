from .Component import Component

class Transform(Component):
    def __init__(self, obj, x: int, y: int, scale_x: int, scale_y: int):
        self.obj = obj
        self.x: int = x
        self.y: int = y
        self.scale_x: int = scale_x
        self.scale_y: int = scale_y