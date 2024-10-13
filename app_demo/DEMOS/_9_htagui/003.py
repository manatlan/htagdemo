"""htagui using 'shoelace' ui

This is the "shoelace UI", using shoelace web components.

**PROS:**

 - Shoelace's Components are state of the art !
 - Top choice if you want to use more advanced [sl-components][14] (example sl-tree which is not implemented in [htagui][4])
 
**CONS:**

 - only online app (as shoelace use a js/autoloader (magic), and it can't be otherwise)


"""
from htag import Tag
from htagui import shoelace as ui

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