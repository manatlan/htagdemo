#!/usr/bin/python3
from htag import Tag

class App(Tag.body):
    def init(self):
        self <= "hello world"


if __name__=="__main__":
    # just in case, you'll want to run it with the simple htag'Runner ....
    from htag import Runner
    Runner(App).run()
