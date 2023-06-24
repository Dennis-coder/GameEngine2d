import pygame as pg

class InputManager:
    __axes__ = {}
    __buttons__: dict[str, int] = {}

    __down__: list[bool] = [False] * 512
    __pressed__: list[bool] = [False] * 512
    __up__: list[bool] = [False] * 512

    @classmethod
    def update(cls):
        new_pressed = pg.key.get_pressed()
        # for key, is_pressed in enumerate(new_pressed):
        #     cls.__down__[key] = is_pressed and not cls.__pressed__[key]
        #     cls.__up__[key] = not is_pressed and cls.__pressed__[key]
        cls.__pressed__ = new_pressed

    @classmethod
    def get_key_down(cls, key: int) -> bool:
        return cls.__down__[key]

    @classmethod
    def get_key_pressed(cls, key: int) -> bool:
        return cls.__pressed__[key]

    @classmethod
    def get_key_up(cls, key: int) -> bool:
        return cls.__up__[key]

    @classmethod
    def register_button(cls, name: str, actual_button: int) -> None:
        cls.__buttons__[name] = actual_button

    @classmethod
    def get_button(cls, button: str) -> int:
        if button not in cls.__buttons__:
            raise Exception(f"{button} is not a registered button")
        return cls.__buttons__[button]

    @classmethod
    def get_button_down(cls, button: str) -> bool:
        return cls.get_key_down(cls.get_button(button))
    
    @classmethod
    def get_button_pressed(cls, button: str) -> bool:
        return cls.get_key_pressed(cls.get_button(button))
    
    @classmethod
    def get_button_up(cls, button: str) -> bool:
        return cls.get_key_up(cls.get_button(button))
