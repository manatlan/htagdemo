""" Interaction with JS : using events """
from htag import Tag

class App(Tag.div):
    """ Interaction with JS : using events """
    imports = []  # IRL, you don't need this line
    
    def init(self):
        # using "_onclick=self.method" (like previously) is "not binded"
        # so the caller object is passed as the first arg (after self)
        # but you could bind the method using this form :
        self <= Tag.button("Sizes?", _onclick = self.bind.display( b"window.innerWidth", b"window.innerHeight") )

        # or this form :
        self <= Tag.button("Sizes??", _onclick = self.bind( self.display, b"window.innerWidth", b"window.innerHeight") )

        # if we omit the b"" prefix, it just sends the string
        self <= Tag.button("badSizes?", _onclick = self.bind.display( "window.innerWidth", "window.innerHeight") )
        self <= Tag.button("badSizes??", _onclick = self.bind( self.display, 42, 42) )        
        
        # difference between self.bind.<method>() vs self.bind( <method> ) ?
        # the first one was the historic way, and produce a "javascript string"
        # the 2nd one is the new way, but only for events, because it produces a "Caller" instance
        # which can only work in a event context.
        
        
    def display(self,width,height):
        # here, we just display the results
        self <= Tag.div( f"Client sides : {width}x{height}")
        
    