""" This is the "hello world" 

It just display a window containing "Hello world".

Every htag'apps should contain at least one component, it's the 
main component which will live as long as the app live.

**Note** that `App` inherit from a `Tag.div`, but it will be rendered
as a `body` html tag, because it's the main component.

The special method `def init(self)` is used to initialize the component. You could use a classic `def __init__(self):`, but you'll need to initialize the component, like that:

    def __init__(self):
        super().__init__()
        self <= "Hello world"

The `imports = []` is just an explicit way to declare that this component (`App`) doesn't need any others imports.
In real life, it's not mandated : But here ; we are in an [htagweb][3] context (where multiple htag's app can be runned)

In a classic context (desktop, android, ...): it's not mandated ! Because htag will automatically detects others components in the process, and in this case : will implicitly set the `imports` to `[]` ! 
But it's a good practice to be explicitly setted !

The main entrypoint (`if __name__ == "__main__"`) is just here to run the component. So, after a simple `python3 -m pip install htag -U`, you can run this file as is.
"""

from htag import Tag

class App(Tag.div):
    """ This is the most simple htag component """
    imports = []  # IRL, you don't need this line

    def init(self):
        # I'm just a div, with a textual node content "hello world"
        self <= "Hello world"