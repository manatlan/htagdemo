""" Using components, in a reactive context"""
from htag import Tag

#------------------------------------------------------------
#from c30 import App as Stars # but could be imported
#------------------------------------------------------------
class Stars(Tag.div): # it's a component ;-)
    def init(self,value=0):
        self.value=value
        self.bless = Tag.Button( "-", _onclick = lambda o: self.inc(-1) )
        self.bmore = Tag.Button( "+", _onclick = lambda o: self.inc(+1) )
    def inc(self,v):
        self.value+=v
    def render(self):
        self.clear()
        self += self.bless + self.bmore + ("⭐"*self.value)
#------------------------------------------------------------

class App(Tag.div): # it's a component ;-)
    """ Using components, in a reactive context
    """
    imports = []  # IRL, you don't need this line

    def init(self):
        # here we use the previous component "Stars"
        # in a a reactive way (with a render method)      
        self.s1= Stars()
        self.s2= Stars(2)
        self.s3= Stars(4)

    def render(self): # it's present -> it's used
        self.clear()
        # so the rendering is managed by htag
        self <= self.s1+self.s2+self.s3
        self <= Tag.Button( "Reset", _onclick = lambda o: self.reset() )  # BAD PRACTICE (avoid tag creation in render!!)
        
        # and so, this div will be updated at reset !
        self <= Tag.div("Values: %s,%s,%s" % (self.s1.value,self.s2.value,self.s3.value)) # BAD PRACTICE (avoid tag creation in render!!)
        
    def reset(self):
        # so, resetting values, will redraw this component (App) automatically
        self.s1.value=0
        self.s2.value=2
        self.s3.value=4
  
    # it's really important to understand this concept
    # the differences between c40 & c50 !!!!!
    