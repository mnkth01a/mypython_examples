#!/usr/bin/env python
"""Bounces balls around a window and plays noises.

This is a simple demonstration of how pyglet efficiently manages many sound
channels without intervention.
"""

import random
import sys

import pyglet
from pyglet.window import key

BALL_IMAGE = "pics/ball.png"
BALL_SOUND = "sounds/ball.wav"

if len(sys.argv) > 1:
    BALL_SOUND = sys.argv[1]

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

if len(sys.argv) > 2:
    WINDOW_WIDTH = int(sys.argv[2])
if len(sys.argv) > 3:
    WINDOW_HEIGHT = int(sys.argv[3])

window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT)

sound = pyglet.resource.media(BALL_SOUND, streaming=False)
balls_batch = pyglet.graphics.Batch()
balls = []
label = pyglet.text.Label(
    "Press space to add a ball, backspace to remove, escape to quit",
    font_size=14,
    x=window.width // 2,
    y=10,
    anchor_x="center",
)


class Ball(pyglet.sprite.Sprite):
    ball_image = pyglet.resource.image(BALL_IMAGE)
    @property
    def width(self):
        return self.ball_image.width

    @property
    def height(self):
        return self.ball_image.height

    def __init__(self):
        x = random.random() * (window.width - self.width)
        y = random.random() * (window.height - self.height)

        super(Ball, self).__init__(self.ball_image, x, y, batch=balls_batch)

        self.dx = (random.random() - 0.5) * 1000
        self.dy = (random.random() - 0.5) * 1000

    def update_position(self, dt):
        if self.x <= 0 or self.x + self.width >= window.width:
            self.dx *= -1
            sound.play()
        if self.y <= 0 or self.y + self.height >= window.height:
            self.dy *= -1
            sound.play()
        self.x += self.dx * dt
        self.y += self.dy * dt

        self.x = min(max(self.x, 0), window.width - self.width)
        self.y = min(max(self.y, 0), window.height - self.height)


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.SPACE:
        balls.append(Ball())
    elif symbol == key.BACKSPACE:
        if balls:
            del balls[-1]
    elif symbol == key.ESCAPE:
        window.has_exit = True


@window.event
def on_draw():
    window.clear()
    balls_batch.draw()
    label.draw()


def update(dt):
    for ball in balls:
        ball.update_position(dt)


if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1 / 30.0)
    pyglet.app.run()
