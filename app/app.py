#!/usr/bin/python3
from htag import Tag
import htagweb,htag

class App(Tag.body):
    statics="""
    body {color:white;background:black}
    center {position:fixed;bottom:0px;right:0px}
    """
    
    def init(self):
        self.placeholder = Tag.div()

        self <= Tag.p(f"hello world")
        self <= Tag.center(f"htag={htag.__version__} & htagweb={htagweb.__version__}")
        self <= Tag.button("say hi", _onclick = self.say )
        self <= self.placeholder

    def say(self,ev):
        self.placeholder <= Tag.div("hello")

if __name__=="__main__":
    # just in case, you'll want to run it with the simple htag'Runner ....
    from htag import Runner
    Runner(App).run()
