"""Hierarchy sample application"""

import time
import math
import pygame

from quaternion import Quaternion

from scene import Scene
from object3d import Object3d
from camera import Camera
from mesh import Mesh
from material import Material
from color import Color
from vector3 import Vector3
from vector3 import *
from scene import *

# Define a main function, just to keep things nice and tidy
def main():
    """Main function, it implements the application loop"""
    # Initialize pygame, with the default parameters
    pygame.init()

    # Define the size/resolution of our window
    res_x = 640
    res_y = 480

    # Create a window and a display surface
    screen = pygame.display.set_mode((res_x, res_y))

    # Create a scene
    scene = Scene("TestScene")
    scene.camera = Camera(False, res_x, res_y)

    # Moves the camera back 2 units
    scene.camera.position = Vector3(0, 0, -2)

    # Create a pyramid of n sides and place it in a scene, at position (0,0,0)
    obj1 = Object3d("Pyramid")
    obj1.scale = Vector3(1, 1, 1)
    obj1.position = Vector3(0, 0, 0)
    # To change the amount of sides of the pyramid trade the 3 for the amount wanted
    obj1.mesh = Mesh.create_pyramid((0.5, 0.5, 0.5), 3, None)
    obj1.material = Material(Color(1,0,0,1), "PyramidMaterial")
    scene.add_object(obj1)



    angle = 15
    axis = Vector3(0, 0, 0)


    # Timer
    delta_time = 0
    prev_time = time.time()

    pygame.mouse.set_visible(False)
    pygame.event.set_grab(True)

    # Keys
    aKey = False
    dKey = False
    eKey = False
    qKey = False
    sKey = False
    wKey = False
    upKey = False
    downKey = False
    leftKey = False
    rightKey = False
    pUpKey = False
    pDownKey = False

    # Keys List
    keys = [ aKey, dKey, eKey, qKey, sKey, wKey, upKey, downKey, leftKey, rightKey, pUpKey, pDownKey ]

    run = True
    obj = True

    # Game loop, runs forever
    while (run):
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    run = False

                if (event.key == pygame.K_a):
                    aKey = True

                if (event.key == pygame.K_d):
                    dKey = True

                if (event.key == pygame.K_e):
                    eKey = True

                if (event.key == pygame.K_q):
                    qKey = True

                if (event.key == pygame.K_s):
                    sKey = True

                if (event.key == pygame.K_w):
                    wKey = True

                if (event.key == pygame.K_UP):
                    upKey = True

                if (event.key == pygame.K_DOWN):
                    downKey = True

                if (event.key == pygame.K_LEFT):
                    leftKey = True

                if (event.key == pygame.K_RIGHT):
                    rightKey = True

                if (event.key == pygame.K_PAGEUP):
                    pUpKey = True

                if (event.key == pygame.K_PAGEDOWN):
                    pDownKey = True

            elif (event.type == pygame.KEYUP):
                if (event.key == pygame.K_a):
                    aKey = False

                if (event.key == pygame.K_d):
                    dKey = False

                if (event.key == pygame.K_e):
                    eKey = False

                if (event.key == pygame.K_q):
                    qKey = False

                if (event.key == pygame.K_s):
                    sKey = False

                if (event.key == pygame.K_w):
                    wKey = False

                if (event.key == pygame.K_UP):
                    upKey = False

                if (event.key == pygame.K_DOWN):
                    downKey = False

                if (event.key == pygame.K_LEFT):
                    leftKey = False

                if (event.key == pygame.K_RIGHT):
                    rightKey = False

                if (event.key == pygame.K_PAGEUP):
                    pUpKey = False

                if (event.key == pygame.K_PAGEDOWN):
                    pDownKey = False

        # Moves the object
        if aKey:
            scene.camera.position += scene.camera.right() * -0.001

        if dKey:
            scene.camera.position += scene.camera.right() * 0.001

        if sKey:
            scene.camera.position += scene.camera.forward() * -0.001

        if wKey:
            scene.camera.position += scene.camera.forward() * 0.001
        
        if qKey:
            scene.camera.position += Vector3(0,0,0.01)

        if eKey:
            scene.camera.position -= Vector3(0,0,0.01)
        
        # Rotates the object, considering the time passed (not linked to frame rate)
        q = Quaternion.AngleAxis(axis, math.radians(angle) * delta_time)
        obj1.rotation = q * obj1.rotation


        #Rotate keys
        if upKey:
            axis = Vector3(3,0,0)
            scene.camera.rotation = q * scene.camera.rotation

        if downKey:
            axis = Vector3(-3,0,0)
            scene.camera.rotation = q * scene.camera.rotation

        if leftKey:
            axis = Vector3(0,3,0)
            scene.camera.rotation = q * scene.camera.rotation

        if rightKey:
            axis = Vector3(0,-3,0)
            scene.camera.rotation = q * scene.camera.rotation

        if pUpKey:
            axis = Vector3(0,0,3)
            scene.camera.rotation = q * scene.camera.rotation

        if pDownKey:
            axis = Vector3(0,0,-3)
            scene.camera.rotation = q * scene.camera.rotation

        # Stop objects that are behind the camera from being renderered
        if (dot_product(scene.camera.forward(), obj1.forward() - scene.camera.position) < 0):
            if (obj):
                scene.remove_object(obj1)
                obj = False
        else:
            obj = True
            if (obj1 not in scene.objects):
                scene.add_object(obj1)

        screen.fill((0,0,0))
        scene.render(screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()

        # Updates the timer, so we we know how long has it been since the last frame
        delta_time = time.time() - prev_time
        prev_time = time.time()


# Run the main function
main()
