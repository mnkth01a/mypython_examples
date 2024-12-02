import pyglet

### Create a Pyglet window by calling its default constructor ###
window = pyglet.window.Window()

### To display the text, we'll create a label ###
label = pyglet.text.Label(
    "Hello, World!",
    font_name="Times New Roman",
    font_size=36,
    x=window.width // 2,
    y=window.height // 2,
    anchor_x="center",
    anchor_y="center",
)


### Define the on_draw event handler ###
@window.event
def on_draw():
    window.clear()
    label.draw()


### Run the Pyglet application ###
pyglet.app.run()
""" """
