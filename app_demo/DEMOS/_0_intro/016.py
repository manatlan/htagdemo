"""Example of childs creation ++

Here you will learn differences between "attributs" and "properties"

* "attribut": it's an argument prefixed by an underscore (`_`). The attribut will be setted on the html tag.
* "property": it's an argument which will be setted as a property on the instance of the object (on server side only)

The property `js` is a special property which define the javascript that will be executed each time the tag is rendered on client-side.
(In the `js` property: you can use `self` (which will refer to the node instance on client-side))



"""
from htag import Tag

class App(Tag.div):
    imports = []  # IRL, you don't need this line
    
    def init(self):
        # we have seen that we can add html attributs by prefixing them with "_"
        self <= Tag.div("We have seen that we could add style easily", _style="background:yellow")

        # but we can set real properties too on instance, at construction time
        # (can be very handy !!!)
        o = Tag.div("But we can set real property too", info="yolo" )
        assert o.info == "yolo"
        self <= o

        #TODO


        
        # here we can set the "js" property, and set the focus
        # to the input ('self' is a js keyword which refer to the current tag node in js side (here: input))
        self <= Tag.input(_value="text", js="self.focus()")
       