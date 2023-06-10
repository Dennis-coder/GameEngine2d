from GameEngine import Window
from GameEngine.Components import *
from PlayerMovement import PlayerMovement
import pygame as pg

def main():
    scene = Window.create_scene("test")
    Window.change_scene("test")
    
    camera = scene.create_entity()
    camera.add_component(CameraComponent)
    camera.add_component(ScriptComponent, PlayerMovement)

    player = scene.create_entity()
    player.add_component(SpriteComponent, pg.image.load("assets/ship.png"))

    Window.set_show_fps(True)
    Window.start()

if __name__ == "__main__":
    main()