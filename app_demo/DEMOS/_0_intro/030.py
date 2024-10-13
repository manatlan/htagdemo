""" rendering lately (using a render())"""
from htag import Tag

class App(Tag.div): # it's a component ;-)
    """ rendering lately (using a render())
    """
    imports = []  # IRL, you don't need this line
    
    def init(self,value=0):
        self.value=value
        self.bless = Tag.Button( "-", _onclick = lambda o: self.inc(-1) )
        self.bmore = Tag.Button( "+", _onclick = lambda o: self.inc(+1) )

    def inc(self,v):
        self.value+=v
        
    # when a "render" method is present
    # htag will use it to build the rendering form
    # this method is called during __str__ phase.
    # if not present -> it let your 'init' and 'interactions' play with the rendering
    def render(self): # <- ensure dynamic rendering
        self.clear()
        self += self.bless + self.bmore + ("⭐"*self.value)

    # using a render() method : is easier, and really adapted for short component
    # not using a render() method : is more adapted for complex component, which won't render all everytime
        