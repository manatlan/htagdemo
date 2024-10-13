"""Using swiperjs to create an htag component ready to use

[swiperjs](https://swiperjs.com/) is a web component easily usable in an htag app !

"""
from htag import Tag

class Swiper(Tag.swiper_container):
    # https://swiperjs.com/
    statics=Tag.script(_src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-element-bundle.min.js")
    def init(self,ll):
        for i in ll:
            self += Tag.swiper_slide(i)
        
class App(Tag.body):
    
    imports=[Swiper]
    def init(self):
        self+= Tag.h3("swipe me")
        self+= Swiper([Tag.img(_src=f"https://picsum.photos/50{i}/501") for i in range(3)])
        #self+= Swiper([Tag.img(_src=f"https://placekitten.com/502/50{i}") for i in range(10)])