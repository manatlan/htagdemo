"""htagui using 'material design' ui

This is the "material design", using "material design" web components.

**PROS:**

 - use "material design" ?
 
**CONS:**

 - very heavy !
 - only online app !
 - ... and bugged (a popmenu over a dialog box is not possible) : so I plan to remove this savour. It's just here for the show ! Don't use it !

"""
from htag import Tag
from htagui import md as ui

class App(ui.App):
    imports = ui.ALL

    def init(self):
        ph = Tag.b()
       
        OPTS = {1:"v1",2:"v2",3:"v3"}

        self <= ui.IText("", onchange=lambda ev: ph.clear(ev.target.value),_label="input some text here") 
        self <= ui.ITextarea("", onchange=lambda ev: ph.clear(ev.target.value),_label="input some text here") 
        self <= ui.ISelect(2,OPTS, onchange=lambda ev: ph.clear(ev.target.value)) 
        self <= Tag.hr()
        self <= ui.Button("Hello world",_onclick=lambda ev: self.ui.alert("hello"))
        self <= Tag.hr()
        self <=Tag.i("Changes will be reflected here:")
        self <= ph