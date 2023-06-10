import pygame as pg

class InputManager:
    axes = {}
    buttons: dict[str, int] = {}

    down: list[bool] = [False] * 512
    pressed: list[bool] = [False] * 512
    up: list[bool] = [False] * 512

    @classmethod
    def update(cls):
        new_pressed = pg.key.get_pressed()
        for key, is_pressed in enumerate(new_pressed):
            cls.down[key] = is_pressed and not cls.pressed[key]
            cls.up[key] = not is_pressed and cls.pressed[key]
        cls.pressed = new_pressed

    @classmethod
    def get_key_down(cls, key: int) -> bool:
        return cls.down[key]

    @classmethod
    def get_key_pressed(cls, key: int) -> bool:
        return cls.pressed[key]

    @classmethod
    def get_key_up(cls, key: int) -> bool:
        return cls.up[key]

    @classmethod
    def register_button(cls, name: str, actual_button: int) -> None:
        cls.buttons[name] = actual_button

    @classmethod
    def get_button(cls, button: str) -> int:
        if button not in cls.buttons:
            raise Exception(f"{button} is not a registered button")
        return cls.buttons[button]

    @classmethod
    def get_button_down(cls, button: str) -> bool:
        return cls.get_key_down(cls.get_button(button))
    
    @classmethod
    def get_button_pressed(cls, button: str) -> bool:
        return cls.get_key_pressed(cls.get_button(button))
    
    @classmethod
    def get_button_up(cls, button: str) -> bool:
        return cls.get_key_up(cls.get_button(button))
