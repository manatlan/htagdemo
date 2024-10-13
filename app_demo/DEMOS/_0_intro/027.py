""" Interaction with JS : the base (with self.call( js:str ) )"""
from htag import Tag


class App(Tag.div):
    """ Interaction with JS : the base (with self.call( js:str ) )"""
    imports = []  # IRL, you don't need this line
    
    def init(self):
        self <= Tag.button("test", _onclick = self.more)
        
    def display(self, width, height):
        self <= Tag.div( f"Client sides : {width}x{height}")
        
    def more(self,o):
        # execute a js statement which will be executed when "more" is executed
        self.call.display( b"window.innerWidth", b"window.innerHeight")  # <- shorcut of self.call( self.bind.display( b"window.innerWidth", b"window.innerHeight") )

    # there are 2 ways, to send js statement to front
    #   "self.js = js"    : is more for "static js" (js which should be executed at each rendering)
    #   "self.call( js )" : is more for "interaction js" (a js statement produced just for the need)