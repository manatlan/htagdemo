"""htagui using 'basics' ui

This is the "basics UI", home-made UI with pure html/css

Currently, the basics ui is exposed in the htag namespace (when htagui is installed), so you could replace this 2 lines:

    from htag import Tag
    from htagui import basics as ui

by:

    from htag import Tag,ui

**PROS:**

 - work in offline htag'apps
 - short footprint !

**CONS:**

 - ugly (can do better!)
"""
from htag import Tag
from htagui import basics as ui

class App(ui.App): #<- auto add self.ui in the tag !
    imports = ui.ALL  #<- declare all htagui components in one shot !

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