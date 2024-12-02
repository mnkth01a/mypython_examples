#!/usr/bin/env python
"""
"""

__docformat__ = 'restructuredtext'
__version__ = '$Id$'

import pyglet

window = pyglet.window.Window()
image = pyglet.resource.image('pics/kitten.jpg')


@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)

### Center the image in the window ###
    image_x = (window.width - image.width) // 2
    image_y = (window.height - image.height) // 2

    @window.event
    def on_draw():
        window.clear()
        image.blit(image_x, image_y)
pyglet.app.run()
