from ..Component import Component

class Transform(Component):
    def __init__(self, x: int=0, y: int=0, width: int=0, height: int=0, scale_x: int=0, scale_y: int=0):
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height
        self.scale_x: int = scale_x
        self.scale_y: int = scale_y