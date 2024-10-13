"""A calc component 

Here is a simple component !


(it's an old example ! nowadays I'll make it differently !)"""
from htag import Tag


class App(Tag.div):
    """A calc component """

    imports = []  # IRL, you don't need this line
    statics = Tag.style("* {font-size:40px}")
    
    def init(self):
        self.txt=""
        self.aff = Tag.Div("&nbsp;",_style="border:1px solid black")
        
        self <= self.aff
        self <= Tag.button("C", _onclick=self.bind( self.clean), js="self.focus()" )
        self <= [Tag.button(i,  _onclick=self.bind( self.press, i) ) for i in "0123456789+-x/."]
        self <= Tag.button("=", _onclick=self.bind( self.compute ) )

#     #-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ 
#     # theses lines of code, add a real keyboard interactions
#     #-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ 
#         self["onkeyup"] = self.bind( self.presskey, b"event.key" )

#     def presskey(self,key):
#         if key in "0123456789+-*/.":
#             self.press(key)
#         elif key=="Enter":
#             self.compute()
#         elif key in ["Delete","Backspace"]:
#             self.clean()
#     #-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ 

    def press(self,val):
        self.txt += val
        self.aff.set( self.txt )
        
    def compute(self):
        try:
            comp=self.txt.replace("x","*")
            self.txt = str(eval(comp))
            self.aff.set( self.txt )
        except Exception as e:
            self.txt = ""
            self.aff.set( "Error (%s)" % comp )

    def clean(self):
        self.txt=""
        self.aff.set("&nbsp;")
  