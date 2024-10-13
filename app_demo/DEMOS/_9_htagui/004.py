"""htagui using 'fluent' ui

This is the "fluent UI", using fluentUI web components.

**PROS:**

 - fluentUI's Components are good !
 - good choice if you want to use more [fluent-components][15]
 
**CONS:**

 - only online app (but plan to embbed the 400ko of js)

"""
from htag import Tag
from htagui import fluent as ui

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