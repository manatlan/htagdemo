"""Include external JS/CSS"""
from htag import Tag


class App(Tag.div):
    """Include external JS/CSS """
    imports = []  # IRL, you don't need this line

    # of course, a component could need to use external contents
    # htag provides a way to include statics in html headers
    # using the "statics" class attribut.

    statics=[
        Tag.link(_href="link to your css file"),
        Tag.script(_src="link to your js file"),
        Tag.script("""var a=42;"""),
        Tag.style("""body {background:yellow}"""),
    ]
   
    
    # theses statics will be included in html headers, for all
    # your page.
    # they will be included, only once, in the first rendering.
    # when your component start really, everything is loaded.
    
    def init(self):
        self <= "Examples of statics, see source file"
  