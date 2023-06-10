from .Component import Component

class Camera(Component):
    def __init__(self, obj, width, height):
        self.obj = obj
        clear_color = (20,20,20)
        self.width = width
        self.height = height
