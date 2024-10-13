"""Use a component that render as a QR Code

Technically you could use a python lib to generate a qr code. But you could
use a JS lib for that purpose too !

Here, we use [qrcodejs](https://github.com/davidshimjs/qrcodejs) ;-)

"""
from htag import Tag

class QRCode(Tag.span):
    statics=Tag.script(_src="https://cdn.rawgit.com/davidshimjs/qrcodejs/gh-pages/qrcode.min.js")
    
    def init(self,txt,size=128):
        self.js=f"""
new QRCode( self, {{
    text: `{txt}`,
    width: {size},
    height: {size},
    colorDark : "#000000",
    colorLight : "#ffffff",
    correctLevel : QRCode.CorrectLevel.H
}})"""

class App(Tag.body):
    imports=[QRCode]
    def init(self):
        self+=QRCode("https://raw.githack.com/manatlan/htag/main/examples/pyscript_demo.html",256)
        self+=QRCode("Hello from htag ;-)")
        