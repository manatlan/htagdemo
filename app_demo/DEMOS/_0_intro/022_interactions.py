"""Interactions : "bind" can do a lot more

and more ...

### "bind" is useful when you need to send data (from js to py)

See button ex1, ex2 & ex3

"ex3" use the b'trick : to send real javascript data (the string is prefixed by `b"..."` )

### "bind" is chain'able !

see "ex10"

### "bind" is useful when you need to do more things, on client side

see "ex20"


"""
from htag import Tag

class App(Tag.body):
    imports=[]
    def init(self):

        def more(o,msg,nb=1):
            # "o" is self, in all theses cases
            self <= Tag.div(f"hello {msg*nb}")

        self <= Tag.button("ex1", _onclick=self.bind( more, "world",nb=10 ))
        self <= Tag.button("ex2", _onclick=self.bind( more, 42 ))
        self <= Tag.button("ex3", _onclick=self.bind( more, b"window.innerWidth" ))

        self <= Tag.button("ex10", _onclick=self.bind( more, "the" ).bind( more, "world" ).bind( more, "is" ).bind( more, "crazy" ))

        self <= Tag.button("ex20", _onclick=self.bind( more, "the alert box" ) + "alert(42)" )
