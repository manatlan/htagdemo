""" Using components, in a non-reactive context"""
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
    """ Using components, in a non-reactive context
    """
    imports = []  # IRL, you don't need this line

    def init(self):
        # here we use the previous component "Stars"
        # in a non reactive way (without render method)
        self.s1= Stars()
        self.s2= Stars(2)
        self.s3= Stars(4)
        
        # so we create the rendering at init time
        self <= self.s1+self.s2+self.s3
        self <= Tag.Button( "Reset", _onclick = lambda o: self.reset() )

        # this div will not be updated at reset()
        self <= Tag.div("Values: %s,%s,%s" % (self.s1.value,self.s2.value,self.s3.value))
        
    def reset(self):
        # theses components are reactives, from scratch
        # since, they use a "render()" method
        # to redraw itself according its states
        self.s1.value=0
        self.s2.value=2
        self.s3.value=4