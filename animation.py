#!/usr/bin/env python
"""Load and display a GIF animation.

Usage::

    animation.py [<filename>]

If the filename is omitted, a sample animation is loaded
"""

__docformat__ = "restructuredtext"
__version__ = "$Id$"

# The dinosaur.gif file packaged alongside this script is in the public
# domain, it was obtained from http://www.gifanimations.com/.

import sys

import pyglet

"""
For whatever reason, the file doesn't load properly when the path is given as an argument.

The file is loaded properly when the path is hardcoded.
"""
if len(sys.argv) > 1:
    # Load the animation from file path
    animation = pyglet.image.load_animation(sys.argv[1])
    texture_bin = pyglet.image.atlas.TextureBin()
    animation.add_to_texture_bin(texture_bin)
else:
    # Load animation from resource (this script's directory).
    animation = pyglet.resource.animation("pics/dinosaur.gif")

window = pyglet.window.Window(
    width=animation.get_max_width() * 3, height=animation.get_max_height() * 3
)

### Center the window on the screen ###
window.set_location(
    (window.screen.width - window.width) // 2,
    (window.screen.height - window.height) // 2,
)

### Create a sprite from the animation ###
sprite = pyglet.sprite.Sprite(animation)

### Set the sprite's position to the center of the window ###
sprite.x = window.width // 2 - sprite.width // 2
sprite.y = window.height // 2 - sprite.height // 2

# Set window background color to white.
pyglet.gl.glClearColor(1, 1, 1, 1)


### Define the on_draw event handler ###
@window.event
def on_draw():
    window.clear()
    sprite.draw()


### Run the Pyglet application ###
pyglet.app.run()
