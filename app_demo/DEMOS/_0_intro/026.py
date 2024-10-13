""" Interaction with JS : the base (with js attribut)"""
from htag import Tag

class App(Tag.div):
    """ Interaction with JS : the base (with js attribut)"""
    imports = []  # IRL, you don't need this line
    
    def init(self):
        # tag instances owns a special attribut called "js"
        # which will let you define a "js statement" which will be
        # called after at each interaction (a global js)
        
        # here we instruct the tag to call "display" method with 2 arguments
        # so we use the "self.bind" method to generate our interaction.
        # arguments are b"" prefixed (think "bind") to tell htag to send
        # js interpretation ... and not a simple string.
        self.js = self.bind.display( b"window.innerWidth", b"window.innerHeight")

    def display(self, width, height):
        # so the interaction needs to clear the "self.js"
        self.js="" # clear the "self js" to avoid loop ;-)
        # and display the args
        self <= Tag.div( f"Client sides : {width}x{height}")
        
        # it's a way to send informations from "client side" to "server side"
        # at construction time !
    
