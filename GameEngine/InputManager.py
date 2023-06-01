import keyboard as kb
import mouse

class InputManager:
    axes = {}
    buttons = {}

    down: set[str] = set()
    up: set[str] = set()

    @classmethod
    def init(cls):
        kb.on_press(cls.on_press)
        kb.on_release(cls.on_release)
        mouse.on_click(lambda: cls.down.add("left"))
        mouse.on_right_click(lambda: cls.down.add("right"))
        mouse.on_middle_click(lambda: cls.down.add("middle"))

    @classmethod
    def on_press(cls, event: kb.KeyboardEvent):
        cls.down.add(event.name)

    @classmethod
    def on_release(cls, event: kb.KeyboardEvent):
        cls.up.add(event.name)

    @classmethod
    def update(cls):
        cls.down.clear()
        cls.up.clear()

    @classmethod
    def get_key_down(cls, button: str):
        return button in cls.down

    @classmethod
    def get_key_pressed(cls, button: str):
        return kb.is_pressed(button) or mouse.is_pressed(button)

    @classmethod
    def get_key_up(cls, button: str):
        return button in cls.up

    @classmethod
    def register_button(cls, name: str, actual_button: str):
        cls.buttons[name] = actual_button

    @classmethod
    def get_button(cls, button: str):
        if button not in cls.buttons:
            raise Exception(f"{button} is not a registered button")
        return cls.buttons[button]

    @classmethod
    def get_button_down(cls, button: str):
        return cls.get_key_down(cls.get_button(button))
    
    @classmethod
    def get_button_pressed(cls, button: str):
        return cls.get_key_pressed(cls.get_button(button))
    
    @classmethod
    def get_button_up(cls, button: str):
        return cls.get_key_up(cls.get_button(button))
