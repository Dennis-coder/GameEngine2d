from GameEngine import Window, GameObject
from GameEngine.Components import *
from PlayerMovement import PlayerMovement

def main():
    scene = Window.create_scene("test")
    Window.change_scene("test")
    camera = GameObject() \
        .add_camera() \
        .add_script(PlayerMovement)
    player = GameObject(scale_x=0.5, scale_y=0.3) \
        .add_sprite("assets/ship.png")
    
    scene.add_object(camera)
    scene.add_object(player)

    Window.set_show_fps(True)
    Window.start()

if __name__ == "__main__":
    main()