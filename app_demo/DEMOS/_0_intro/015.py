"""Example of childs creation 
**htag.Tag** is a versatile constructor ;-)

It's the base, and let you build your rendering in a python syntax.

TODO !!!
"""
from htag import Tag

class App(Tag.div):
    """Example of childs creation """
    imports = []  # IRL, you don't need this line
    
    def init(self):
        self.add("<li>content added with self.add(...)</li>")
        
        self <= "<li>This is a shortcut ;-)</li>"
        
        self <= Tag.div("I'm a div")

        # attributs on the div can be setted with prefix "_" at constructor time
        self <= Tag.div("I'm a div with style", _style="background:yellow")

        # or using "items" on the tag, like this
        div = Tag.div("I'm another div with style")
        div["style"]="background:green"
        self <= div

        # You can create what you want
        self <= Tag.what_you_want("I'm 'what-you-want' html tag",_data_info="with 'data-info' attribut")
        
        # childs can be setted at construction, like this
        self <= Tag.ul( Tag.li(1) + Tag.li(2) )

        # or added like this
        ul = Tag.ul( )
        ul <= Tag.li( "A" )
        ul <= Tag.li( "B" )
        self <= ul

        # or like this
        self <= Tag.ul() <= Tag.li( "AA" ) + Tag.li( "BB" )

        # in fact "Tag" construction borrows the best ideas
        # of brython.html, karrigel.HTMLTags, and domonic