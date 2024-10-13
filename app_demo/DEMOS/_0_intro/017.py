"""Example of childs creation ++ and component

Inherit your tag creation 

And best of all, you can easily craft your components ...

And you can surcharge its attributs or properties, at creation time, if the component is "open".

To be "open", the 'init' constructor should accept named arguments (here: `**a`). If it doesn't, it's a "closed" component, and you will
not be able to surcharge its arguments at creation time.
"""
from htag import Tag

class Component(Tag.div):
    def init(self,txt,**a): #<- this component is "open"
        self <= txt

class App(Tag.div):

    imports = []  # IRL, you don't need this line

    def init(self):
        self <= Component("MyComponent1")       
        self <= Component("MyComponent2", _style="background:green")  # <- so you can do this !
        