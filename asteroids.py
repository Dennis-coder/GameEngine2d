from GameEngine import *

class ShipMovement(BaseScript):
    def __init__(self, ship: Entity):
        self.ship = ship

    def update(self, dt: float):
        dy: int = Input.get_key_pressed(K_s) - Input.get_key_pressed(K_w)
        dx: int = Input.get_key_pressed(K_d) - Input.get_key_pressed(K_a)
        self.ship.transform.position.x += dx*dt*10
        self.ship.transform.position.y += dy*dt*10

def settings():
    Window.set_show_fps(True)
    Assets.set_pixels_per_unit(32)


def load_assets():
    Assets.load_image("assets/ship.png", "ship")

def main():
    scene = Window.create_scene("test")
    Window.change_scene("test")

    camera = scene.create_entity()
    camera.add_component(CameraComponent, Window.get_win_size(), (9, 5), camera.transform)
    scene.set_primary_camera(camera)

    ship = scene.create_entity()
    ship.add_component(SpriteComponent, "ship")
    ship.add_component(ScriptComponent, ShipMovement(ship))
    Window.start()

if __name__ == "__main__":
    settings()
    load_assets()
    main()