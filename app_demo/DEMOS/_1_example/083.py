""" A class which embed the A-Frame js (VR/AR)

The [AFrame](https://aframe.io/) is an amazing js library to render 3D thing in a AR/VR context !
And it's simple to embbed them in an htag app.

If you are on your mobile : choose the AR (augmented reality) : it's amazing ;-)

"""
from htag import Tag

class App(Tag.div):
    imports = []  # IRL, you don't need this line

    statics=Tag.script(_src="https://aframe.io/releases/1.3.0/aframe.min.js")

    def init(self):
        scene = Tag.a_scene()

        scene += Tag.a_box(_position="-1 0.5 -3",_rotation="0 45 0",_color="#4CC3D9")
        scene += Tag.a_sphere(_position="0 1.25 -5",_radius="1.25",_color="#EF2D5E")
        scene += Tag.a_cylinder(_position="1 0.75 -3",_radius="0.5",_height="1.5",_color="#FFC65D")
        scene += Tag.a_plane(_position="0 0 -4",_rotation="-90 0 0",_width="4",_height="4",_color="#7BC8A4")
        #scene += Tag.a_sky(_color="#ECECEC")

        self += scene