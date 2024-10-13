"""htagui.shoelace use others shoelace components

Once htagui.shoelace is used,
It's really easy to use others shoelace components (not provided in htagui.shoelace),
in a classic htag way.

Here is an example of the "[Shoelace's Carousel](https://shoelace.style/components/carousel)", which mimics the "ui.Swiper" ;-)

Of course : This component will not work with others flavours (bulma, fluent ...)

"""
from htag import Tag,expose
from htagui import shoelace as ui

class Swiper(Tag.sl_carousel): 
    def init(self,ll:list,default=0,**a):
        self["mouse-dragging"]=True
        self["--slide-gap"]="30px"
        for i in ll:
            self <= Tag.sl_carousel_item(i)

        self.js="""
        if(self.goToSlide)
            self.goToSlide(%s);
        else
            window.customElements.whenDefined('sl-carousel').then( function() {
                self.goToSlide(%s);
            });
        """ % (default,default)


class App(ui.App):
    imports = ui.ALL

    def init(self):
        
        class Item(Tag.img):
            def init(self,i):
                self["src"]=f"https://loremflickr.com/200/200/colors?random={i}"

        self <= Tag.h3("Swipe below !")
        self <= Swiper( [Item(i) for i in range(50)] )
        