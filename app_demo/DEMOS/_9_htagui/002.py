"""htagui using 'bulma' ui

This is the "bulma UI", same as previous, but styled with bulma css

**PROS:**

 - Same rendering as the good old [htbulma][8] 
 - work offline
 
**CONS:**

 - embbed 80ko of css

"""
from htag import Tag
from htagui import bulma as ui

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