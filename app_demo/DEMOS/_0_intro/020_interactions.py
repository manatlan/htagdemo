"""Interactions : the base

An UI is nothing without interaction : let's add somes !

Here, the button "Add Content" will display "hello" in the placeholder ( a basic div ). This interaction will force ONLY the rendering of the placeholder (because it's the only one whose has changed its state).


"""
from htag import Tag

class App(Tag.div):
    """ An example with basic interaction """
    imports = []  # IRL, you don't need this line
    
    def init(self):
        placeholder = Tag.div() 

        def more( object ):
            placeholder <= "hello "    

        self <= Tag.button("Add Content", _onclick = more )
        self <= Tag.button("Clear",       _onclick = lambda o: placeholder.clear())
        # just an example to call a method in javascript side
        self <= Tag.button("alert box",   _onclick = "alert(42)")

        self <= placeholder
        
        
