from GameEngine import *

class Player1Movement(BaseScript):
    def __init__(self, player: Entity):
        self.player = player

    def update(self, dt: float):
        dy: int = Input.get_key_pressed(K_s) - Input.get_key_pressed(K_w)
        self.player.transform.position.y += dy*dt*10
        if self.player.transform.position.y < -4:
            self.player.transform.position.y = -4
        if self.player.transform.position.y > 4:
            self.player.transform.position.y = 4

class Player2Movement(BaseScript):
    def __init__(self, player: Entity):
        self.player = player

    def update(self, dt: float):
        dy: int = Input.get_key_pressed(K_DOWN) - Input.get_key_pressed(K_UP)
        self.player.transform.position.y += dy*dt*10

        if self.player.transform.position.y < -4:
            self.player.transform.position.y = -4
        if self.player.transform.position.y > 4:
            self.player.transform.position.y = 4

class BallMovement(BaseScript):
    def __init__(self, ball):
        self.ball = ball
        self.dx = 3
        self.dy = 2

    def update(self, dt: float):
        self.ball.transform.position.x += self.dx*dt
        self.ball.transform.position.y += self.dy*dt

        if self.ball.transform.position.y < -4.5:
            self.ball.transform.position.y = -4.5
            self.dy *= -1
        if self.ball.transform.position.y > 4.5:
            self.ball.transform.position.y = 4.5
            self.dy *= -1
    
    def on_collision(self, other):
        self.dx *= -1.1

def settings():
    Window.set_show_fps(True)
    Assets.set_pixels_per_unit(32)


def load_assets():
    Assets.load_image("assets/pepsi.png", "pepsi")
    Assets.load_image("assets/coke.png", "coke")
    Assets.load_image("assets/ball.png", "ball")

def main():
    scene = Window.create_scene("test")
    Window.change_scene("test")

    camera = scene.create_entity()
    player1 = scene.create_entity()
    player2 = scene.create_entity()
    ball = scene.create_entity()

    camera.add_component(CameraComponent, Window.get_win_size(), (9, 5), camera.transform)
    scene.set_primary_camera(camera)

    player1.transform.size = glm.vec2(0.6, 2)
    player1.transform.position.x = -8
    player1.add_component(SpriteComponent, "coke")
    player1.add_component(ScriptComponent, Player1Movement(player1))
    player1.add_component(BoxCollider, (0,0), (1,1))

    player2.transform.size = glm.vec2(0.6, 2)
    player2.transform.position.x = 8
    player2.add_component(SpriteComponent, "pepsi")
    player2.add_component(ScriptComponent, Player2Movement(player2))
    player2.add_component(BoxCollider, (0,0), (1,1))
    
    ball.transform.size = glm.vec2(1,1)
    ball.add_component(SpriteComponent, "ball")
    ball.add_component(ScriptComponent, BallMovement(ball))
    ball.add_component(BoxCollider, (0,0), (1,1), ball.script.on_collision)

    Window.start()

if __name__ == "__main__":
    settings()
    load_assets()
    main()