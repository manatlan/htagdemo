""" An application that use your webcam

This htag app will use your webcam (or your camera if you are on your phone) to
show you how it's easy to interact with html5 apis in a python app.

BTW, you'll need to have a cam, and authorize it, to let it work ;-)

BTW, no images is saved on server side ... see the code ;-)
"""
from htag import Tag

class Cam(Tag.video):
    statics = Tag.script("""
function startCam(video) {
    navigator.mediaDevices.getUserMedia({
        video: true,
        audio: false
    })
    .then(function(stream) {
        video.srcObject = stream;
        video.play();
    })
    .catch(function(err) {
        document.body.innerHTML = err;
    });
}

function takeCamShot(video,width,height) {
    let canvas = document.createElement("canvas");
    let context = canvas.getContext('2d');
    canvas.width = width;
    canvas.height = height;
    context.drawImage(video, 0, 0, width, height);
    return canvas.toDataURL('image/jpeg');    
}
""")

    js = """startCam(self);"""
    
    def init(self,callback=None,width=320,height=240):
        self["style"]=f"width:{width}px;height:{height}px;border:1px solid black"
        if callback:
            self["onclick"]=self.bind( callback, bytes("takeCamShot(this,%s,%s)" % (width,height),"utf8") )

class App(Tag.body):
    """ An application that use your webcam """
    statics = b"function error(m) {alert(m)}"
    imports = [Cam,] # not really needed IRL
    
    def init(self):
        self += Cam(self.takeShot)
        self += "Click to capture a frame ;-)"
        
    def takeShot(self,o,dataurl):
        self += Tag.img(_src=dataurl)