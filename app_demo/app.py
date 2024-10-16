from htag import Tag,expose
import html,os,re,time
from htagui import shoelace as ui
import urllib.parse

###### for __version___
import htag as HTag
import htagui
import htagweb
######


FOLDER=os.path.join(os.path.dirname(__file__),"DEMOS")
LINKS = """
[1]: https://github.com/manatlan/htag
[2]: https://github.com/manatlan/htagapk
[3]: https://github.com/manatlan/htagweb
[4]: https://github.com/manatlan/htagui
[5]: https://github.com/manatlan/htag/tree/main/brython
[6]: https://raw.githack.com/manatlan/htag/main/examples/pyscript_demo.html
[7]: https://raw.githack.com/manatlan/htag/main/brython/bryted.html
[8]: https://github.com/manatlan/htbulma

[10]: https://pywebview.flowrl.com/
[11]: https://pyscript.net/
[12]: https://brython.info/
[13]: https://bulma.io/
[14]: https://shoelace.style/
[15]: https://learn.microsoft.com/en-us/fluent-ui/web-components/

[20]: https://manatlan.github.io/htag/
[21]: https://manatlan.github.io/htag/runners/
[23]: https://manatlan.github.io/htag/runners/#runner-pyscript

[30]: https://www.alwaysdata.com/
"""

DOC1="""
## Welcome to HTag's demo ;-)

**[HTag][1]** is a python3 library which let you code UI interface with python, using HTML/JS/CSS rendering.
The "html rendering" can be produced in anything which can render html/js/css. **[HTag][1]** comes with defaults ["runners"][21], which let you run it in a browser, a [pywebview][10], an [android/apk][2] app.

For the purpose of this demo (which is an htag'app), it uses the [htagweb][3] runner, which acts like a real python http server (hosted graciously by [alwaysdata][30]), and can handle many sessions (users) and many tag instances.

This tutorial will show you how it's easy to build htag'apps with python, and minimal html/css/js knowledgment. You can easily mix **powerful python libs** with **powerful js libs** and build **powerful htag apps**,
whose will work on desktop, on android devices, or on the web (with the same codebase !!!).

"""+LINKS

DOC2="""
**HTag galaxy** :

- [htag][1] : the core ([official docs][20])
- [htagweb][3] : a "Runner" for hosting htag'apps on the web (can handle many sessions (users) and many tag instances)
- [htagapk][2] : a how-to to create APK/android from htag'apps (android or android-tv).
- [htagui][1] : a set of widgets ready-to-use in htag'apps (usings differents flavours/components : basics, [bulma][13], [shoelace][14] & [fluentUI][15])
- [ht-demo][6] : an online demo where you can edit/test examples in live, in a [pyscript runner][23] (yes, htag works in [pyscript][11] too !)


**FYI** : This demo was coded online, in another htag's app (an editor, using monaco/js) ... all running in the current [htagweb][3], using [htagui][4].

...
""" + LINKS


# **HTag4Brython** : side projects

# - [htag4brython][5] : a side-project to mimic htag "Tag creation" in [brython][12] side [**IN-PROGRESS**]
# - [bryted][7] : an online demo where you can edit/test htag4brython examples in live

from glob import glob
class Example:
    
    @staticmethod
    def load():
        ll=[]
        for i in sorted(glob( FOLDER + "/*/???.py")+glob( FOLDER + "/*/???_*.py")):
            ll.append( Example( i ) )
        return ll
        
    def __init__(self,path:str): # path is full path to py file
        url=path[:-3] # remove ".py"
        url="DEMOS"+url[len(FOLDER):]
        self.url = url
        folder,file=path.split("/")[-2:]
        self.catg = folder[3:]
        self.num = self.catg+file[:-3].split("_",1)[0]
        buf=open(path).read()

        if buf.startswith('"""'):
            _,doc,src=buf.split('"""',2)

            if doc.count("\n")>0:
                self.title,self.doc=doc.split("\n",1)
            else:
                self.title=doc
                self.doc="no doc"

            self.src=src.strip()
        else:
            self.title="Unknown Title"
            self.doc="Unknown Doc"
            self.src=buf

        # fix 
        self.ssrc=self.src
        self.src+="""\n\nif __name__ == "__main__":
    from htag import Runner
    Runner( App, interface=(800,600) ).run()

"""

        
class Code(Tag.div):
    """object display python code in a beautiful way (providing a copy button)"""
    statics = [
      Tag.script(_src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.1/highlight.min.js"),
      Tag.link(_href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.1/styles/xcode.min.css", _rel="stylesheet"),
      Tag.style(r""".mycode * {font-family: 'Lucida Console', Monaco, monospace !important;font-size:12px}"""),
    ]
  
    def init(self,code,obj=None):
        self["info"] = "code"
        self["class"] = "mycode"
        self["style"] = "overflow:hidden;height:100%;box-shadow: 0px 0px 3px #888"
        x= Tag.span( html.escape(code) ,_style="display:none")
        self <= x
        self <= Tag.div( Tag.sl_copy_button(_from=id(x)) + obj,_style="position:absolute;right:16px;")
        self <= Tag.pre(js = "hljs.highlightElement(self)",_style="padding:4px;height:100%;overflow:auto") <= Tag.code( html.escape(code) )


class MD(Tag.div):
    """ using python markdown lib ... on server side"""
    def init(self,txt,**a):
        import markdown
        self.clear( markdown.markdown(txt,extensions=['fenced_code']) )




class DEMO(ui.App):
    imports=[Code]+ui.ALL
    statics="""
    html,body {        
        width:100%;height:100%;margin:0px;
        display:flex;flex-flow:column nowrap;width:100%;height:100%;overflow:hidden;
    }
    * {font-family: ubuntu, helvetica !important;}

    pre,code {font-family: courier, 'Lucida Console', monospace !important;font-size:14px}
    pre {background:#EEE;padding:8px;border-radius:4px;margin:4px}
    code {color:#555;background:#EEE;padding:2px;border-radius:2px}
    pre code {padding:0px}
    a {color:red;text-decoration:none}
    
    .menu {display:block;margin:4px;color:black;cursor:pointer}
    .menu:hover {background:#EEE}


    *::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    *::-webkit-scrollbar-track {
        background: None;
    }
    *::-webkit-scrollbar-thumb {
        background: #888;
        //visibility:hidden;
    }
    *:hover::-webkit-scrollbar-thumb {
        //visibility:visible;
    }    
    h1, h2, h3, h4, h5 {padding:0px !important;margin:0px !important;margin-block-start:0em !important;margin-block-end:0em !important;}
    
    .menuselected {border:1px solid red}
    """,b"""
    window.error = function(msg) {
        if(msg === null) { // "COM ERROR: null"
            alert("Expired Session, it will be reloaded !");
            document.location.reload();
        }
        else
            alert(msg);
    };
    

    """
    def init(self):
        self.entries={}
        self.examples = Example.load()
        self.hsizes=[50,50]
        self.vsizes=[50,50]

        self.otitle = Tag.b()
        self.omain = Tag.div(_style="width:100%;height:100%;overflow:hidden;flex: 1 1 auto;")

        self.drawer=Tag.sl_drawer(
            _placement="start",
            _no_header=True,
        ) 
            
        self += Tag.div([
                ui.Button(Tag.sl_icon(_name="list"),_onclick=self.bind(self.openmenu,b"document.location.hash.substr(1)")),
                self.otitle,
            ],_style="flex: 0 0 auto;")
        self += self.omain
        self += self.drawer


        self.js="""
            if(!window._hashchange_listener) {
                window.addEventListener('hashchange',() => {self.preload(document.location.hash.substr(1).trim(), window.innerWidth);});
                window._hashchange_listener=true;
                self.preload(document.location.hash.substr(1).trim(), window.innerWidth);
            }
            
        """
    
    def openmenu(self,num):
        
        def select(num=None):
            self.drawer.call("self.hide()")
            if num:
                self.rerender(num)
            else:
                self.page()
        
        with Tag.div() as menu:
            llintros=[]
            llexamples=[]
            llhtaguis=[]
            for exa in self.examples:
                if exa.catg=="intro":
                    llintros.append( exa )
                if exa.catg=="example":
                    llexamples.append( exa )
                if exa.catg=="htagui":
                    llhtaguis.append( exa )
            
            def feed(ll):
                # return [ Tag.a(exa.title,_href=f"#{exa.num}",_onclick=lambda ev: self.ui.close(),_class="menu" + (" menuselected" if exa.num == num else ""),_myid=exa.num ) for exa in ll]
                return [ Tag.a(exa.title,_onclick=lambda ev,n=exa.num: select(n),_class="menu" + (" menuselected" if exa.num == num else ""),_myid=exa.num ) for exa in ll]

            menu <= Tag.a("Welcome",_onclick=lambda ev: select() ,_class="menu" + (" menuselected" if not num else ""),)
            menu <= Tag.div("&nbsp;")
            menu <= Tag.b("Tutorial")
            menu <= feed(llintros)
            menu <= Tag.div("&nbsp;")
            menu <= Tag.b("Examples")
            menu <= feed(llexamples)
            menu <= Tag.div("&nbsp;")
            menu <= Tag.b("htagui Examples")
            menu <= feed(llhtaguis)
        
        self.drawer.set(menu)
        self.drawer.call("setTimeout( function() {self.show()}, 0)")
        
    @expose
    def preload(self,num,winwidth=None):
        self.ui.close() # close the alert box if it's opened
        if winwidth:
            self.desktop=True
            if int(winwidth)<600:
                self.desktop=False
        if num.strip():
            self.rerender(num)
        else:
            self.page()
            
            
            

    def page(self):
        self.otitle.clear(f" HTag demo !!! ")
    
        with Tag.div(_style="padding:20px;height:100%;overflow-y:auto") as page:
            page <= Tag.img(_src="https://manatlan.github.io/htag/htag.png",_style="float:right;width:33%")
            page <= MD( DOC1 )

            for idx,exa in enumerate(self.examples):
                if exa.catg=="intro":
                    page <= ui.Button("Start the tour", _onclick=lambda ev,idx=idx: self.rerender( self.examples[idx].num ))
                    break
            for idx,exa in enumerate(self.examples):
                if exa.catg=="example":
                    page <= ui.Button("See examples", _onclick=lambda ev,idx=idx: self.rerender( self.examples[idx].num ))
                    break
            for idx,exa in enumerate(self.examples):
                if exa.catg=="htagui":
                    page <= ui.Button("See htagui examples", _onclick=lambda ev,idx=idx: self.rerender( self.examples[idx].num ))
                    break
                    
            page <= MD( DOC2 )

        self.omain.clear( page )

        self.omain <= Tag.center(f"htag {HTag.__version__}, htagui {htagui.__version__}, htagweb {htagweb.__version__}",_style="position:fixed;bottom:0px;right:0px;left:0px;background:white")
        self.call(f"document.location.hash=''")

    def rerender(self,num):
        
        index=0
        for idx,exa in enumerate(self.examples):
            if exa.num == num:
                index=idx
                break

        if index==0:
            prev,example,next = None,self.examples[0],self.examples[1]
        else:
            prev,example,next = self.examples[index-1],self.examples[index],self.examples[index+1] if index+1 < len(self.examples) else None

        
        anim = lambda x: Tag.sl_animation(x,_name="rubberBand",_duration="2000",_play=True)

        with Tag.div(_style="float:right") as m:
            m += ui.Button("<<",_onclick=lambda ev: self.rerender( prev.num ),_disabled = prev is None)
            m += ui.Button(">>",_onclick=lambda ev: self.rerender( next.num ),_disabled = next is None)

        def box(ev):
            txt=Tag.p("Test this example by yourself !")
            atry = Tag.a("Edit/Test this example",_target="_blank",_href="https://raw.githack.com/manatlan/htag/main/examples/pyscript_demo.html?"+urllib.parse.quote(example.ssrc))
            txt2=Tag.p("<b>NOTE:</b> It will be runned in a pyscript environment (in a simple html page). Everything will be executed in your browser only !")
            self.ui.alert(txt+atry+txt2)

        btry = Tag.span(  Tag.sl_tooltip(Tag.sl_icon(_name="box-arrow-up-right"), _content="Try it in live"),_onclick=box,_style="cursor:pointer")
        ocode=Code( example.src , btry)

        bope=Tag.a(  Tag.sl_tooltip(Tag.sl_icon(_name="box-arrow-up-right"), _content="open in a new tab"),_href=exa.url,_target="_blank",_style="position:fixed;right:4px;bottom:4px;color:black")

        orendu = Tag.div(bope+Tag.iframe(_src=exa.url,_style="width:100%;height:600px;border:0px"),_style="width:100%;height:100%;overflow:hidden")


        # self.otitle.clear(m + f" HTag demo > " + Tag.b(f"({example.catg}) {example.title}",_style="color:blue"))
        self.otitle.clear(m + " HTag demo")
        self.omain.clear()

        def hch(x): self.hsizes = x.sizes
        def vch(x): self.vsizes = x.sizes

        if self.desktop:                
            omd = MD( f"##{example.title}\n"+example.doc + LINKS, _style="height:auto;overflow-y:auto;padding:4px")
            omd += ui.Button("<<",_onclick=lambda ev: self.rerender( prev.num ),_disabled = prev is None)
            omd += ui.Button(">>",_onclick=lambda ev: self.rerender( next.num ),_disabled = next is None)
            
            self.omain<=ui.VSplit( 
                ui.HSplit( 
                    omd,
                    ocode, 
                    onchange=hch,
                    sizes=self.hsizes
                ), 
                orendu,
                onchange=vch,
                sizes=self.vsizes,
                _style="width:100%;height:100%"
            )
        else:
            omd = MD( example.doc + LINKS, _style="height:auto;overflow-y:auto;padding:4px")
            omd += ui.Button("<<",_onclick=lambda ev: self.rerender( prev.num ),_disabled = prev is None)
            omd += ui.Button(">>",_onclick=lambda ev: self.rerender( next.num ),_disabled = next is None)
            
            self.omain <= Tag.h2(example.title)
            self.omain<=ui.Tabs( 
                Tag.div(omd,name="ReadMe"),
                Tag.div(ocode,name="Source") ,
                Tag.div(orendu,name="Render") ,
                _style="height:100%;overflow-y:auto"
            )
        
        self.call(f"document.location.hash='{example.num}'")
    
App=DEMO