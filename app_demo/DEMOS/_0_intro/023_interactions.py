"""Interactions : the @expose way

But there is more ;-)

It's a recent feature, because sometimes you really need to be lower level : so you can "expose" a method, to be callable directly from client-side.

The @expose decorator can only be placed over a prime method of the class.
"""
from htag import Tag,expose

class App(Tag.body):
    imports=[]
    def init(self):

        self <= Tag.button("ex1", _onclick="this.parentNode.more('world',nb=10)")
        self <= Tag.button("ex2", _onclick="this.parentNode.more(42)")
        self <= Tag.button("ex3", _onclick="this.parentNode.more( window.innerWidth )" )

        # just an example
        self.call( "self.more('init')" )

        # if you do that : it will loop forever
        # self.js = "self.more('init')"

    @expose
    def more(self,msg,nb=1):
        self <= Tag.div(f"hello {msg*nb}")