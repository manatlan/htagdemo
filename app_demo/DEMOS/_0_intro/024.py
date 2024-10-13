""" anatomy of events/methods 

Here are examples using different methods types

- "b0" does nothing
- "b1" is a classic method (synchrone)
- "b2" is a generator (it uses a `yield` statement) : at each yield; a rendering on client-side is done !
- "b3" is an asynchrone method
- "b4" is an asynchrone generator

Note that, all rendering are happening in "self" (not a placeholder like previous example) ! So **htag** will redraw the full component at each interaction !
"""
from htag import Tag

class App(Tag.div):
    """ anatomy of events/methods """
    imports = []  # IRL, you don't need this line
    
    def init(self):
        self <= Tag.button( "b0", _onclick=self.b0 )
        self <= Tag.button( "b1", _onclick=self.b1 )
        self <= Tag.button( "b2", _onclick=self.b2 )
        self <= Tag.button( "b3", _onclick=self.b3 )
        self <= Tag.button( "b4", _onclick=self.b4 )

    def b0(self, object):       # As a sync method (classic)
        # it doesn't change the state/rendering
        # of the object
        # so it shouldn't force a redraw/interaction
        pass
    
    def b1(self, object):       # As a sync method (classic)
        self <= "*b1*"
        
    def b2(self, object):       # As a (sync) generator
        self <= "*b2_1*"
        yield # force a full redraw, between the 2 statements
        self <= "*b2_2*"
        
    async def b3(self, object): # As a async method
        self <= "*b3*"
        
    async def b4(self, object): # as a async generator
        self <= "*b4_1*"
        yield # force a full redraw, between the 2 statements
        self <= "*b4_2*"    
