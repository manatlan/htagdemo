#!/usr/bin/python3

from htag import Tag

class App(Tag.body):
    def init(self):
        self <= "hello world"


if __name__=="__main__":
    from htag import Runner
    Runner(App).run()
