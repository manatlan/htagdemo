"""Interactions : introduce the "bind" way

Contrario to python motto : there isn't a only way to do a thing ! In htag : there are a lot of way to interact with the UI ;-(

Since recent htag too; you can pass "event" instead of "object"

You can replace :

    def click_with_origin(o):
        self <= Tag.div("click "+o.innerHTML+" : "+html.escape(repr(o)))

with:

    def click_with_origin(ev):
        self <= Tag.div("click "+ev.target.innerHTML+" : "+html.escape(repr(ev.target)))

If the param is named exactly "ev" : it will contain the event (and so the object is in ev.target (like js)). In all other cases : it will be the caller object.

But "bind" can do a lot of others tricks !!!
"""
from htag import Tag
import html

class App(Tag.body):
    imports=[]
    def init(self):

        def click_with_origin(o):
            self <= Tag.div("click "+o.innerHTML+" : "+html.escape(repr(o)))

        # the simplest form
        # so, the onlick method must accept one parameter : the object which as throw the event
        # (internally the onclick is auto-binded to the object (like 2))
        self <= Tag.button("1", _onclick = click_with_origin )

        # exactly the same ^^
        # it describes exactly what's happening in 1, but longer
        b2=Tag.button("2")
        b2["onclick"]=b2.bind( click_with_origin )
        self <= b2

        
        # if you use this form
        # the onclick is binded to the container (self)
        # and as, it's the self, the click method take itself, so no param !
        self <= Tag.button("3", _onclick=self.bind( self.click ))

        # the old/historic way
        # can only work if container has a self.click() method !
        self <= Tag.button("4", _onclick=self.bind.click() )        

    def click(self):
        self <= Tag.div("click !")