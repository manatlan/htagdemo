"""Tag() the placeholder

`Tag` can be used as a "placeholder", a kind of virtual tag, which can be a reference to handle something else. It's really handly in some cases
(mainly, to avoid non-necesarry tag imbrications).

To understand better, try to show the source on the rendering part, to see differences. 
The "Component1" is not rendered itself, only its childrens are rendered.
The "Component2" is a classic div with its children.

BTW, it can be used in a normal way (non inherited way)
```python
    placeholder = Tag()
    if "i want a div":
        placeholder <= Tag.div()
    else:
        placeholder <= Tag.span()
```

Keep in mind that this placeholder is not really a real tag (it's virtual), and so : some js interactions will not be possible directly.


"""
from htag import Tag

class Component1(Tag):
    def init(self,**a):
        self <= Tag.div("C1")
        self <= Tag.div("C2")
        self <= Tag.div("C3")

class Component2(Tag.div):
    def init(self,**a):
        self["info"] = "I'm a real component" # and so I can set attributs on myself
        self["style"].set("border", "1px solid red")
        self <= Tag.div("C1")
        self <= Tag.div("C2")
        self <= Tag.div("C3")

class App(Tag.div):

    imports = []  # IRL, you don't need this line

    def init(self):
        c1=Component1()
        assert c1.tag is None # the component is not visual (it won't render itself)
        assert len(c1.childs)==3 # but it has (virtually) 3 childrens 
        self<=c1

        c2=Component2()
        assert c2.tag == "div" # the component is visual (classic)
        assert len(c2.childs)==3 # and it has (really) 3 childrens 
        self<=c2
