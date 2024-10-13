"""ASync Stream

This example is for "htag powerusers" ...
If you discovering the project, come back here later ;-)
(just keep in mind, that it's possible to output a large amount of data, in a decent way)

It shows you the "htag way" to create a component which
can output a large amount of data (outputed from an async source)
without rendering all the object at each yield statement !
(ex: rendering an http paging, or an apache httpd log ...)

It use a "htag mechanism" which use the yield to add an object in.
this mechanism is named "stream"
"""
from htag import Tag
import asyncio


async def asyncsource():
    """ this is an async source (which simulate delay to get datas) """
    for i in range(10):
        yield "line %s" % i
        await asyncio.sleep(0.1)    # simulate delay from the input source


class Viewer(Tag.ul):
    """ Object which render itself using a async generator (see self.feed)
        (the content is streamed from an async source)
    """
    def __init__(self):
        super().__init__(_style="border:1px solid red")

    async def feed(self):
        """ async yield object in self (stream)"""
        self.clear()
        async for i in asyncsource():
            yield Tag.li(i) # <- automatically added to self instance /!\

    async def feed_bad(self):
        """ very similar (visually), but this way IS NOT GOOD !!!!
            because it will render ALL THE OUTPUT at each yield !!!!!
        """
        self.clear()
        async for i in getdata():
            self <= Tag.li(i) # manually add
            yield             # and force output all !


class App(Tag.div):
    imports = []  # IRL, you don't need this line
    
    def init(self):

        self.view = Viewer()

        # not good result (yield in others space)
        # self <= Tag.button( "feed1", _onclick= lambda o: self.view.feed()  )                # in the button
        # self <= Tag.button( "feed2", _onclick= self.bind( lambda o: self.view.feed() ) )    # in Page

        # good result (yield in the viewer)
        self <= Tag.button( "feed3", _onclick= self.view.bind( self.view.feed ) )
        self <= Tag.button( "feed4", _onclick= self.view.bind.feed() )
        self <= " ( <- if you multi click, then multi streams)"

        self <= self.view