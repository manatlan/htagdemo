#!/usr/bin/python3
from htag import Tag

class App(Tag.body):
    statics="body {color:white;background:black}"
    
    def init(self):
        self.placeholder = Tag.div()

        self <= Tag.p("hello world")
        self <= Tag.button("say hi", _onclick = self.say )
        self <= self.placeholder

    def say(self,ev):
        self.placeholder <= Tag.div("hello")

if __name__=="__main__":
    # just in case, you'll want to run it with the simple htag'Runner ....
    from htag import Runner
    Runner(App).run()
