from .Component import Component

class Script(Component):
    def __init__(self, obj, script):
        self.obj = obj
        self.script = script