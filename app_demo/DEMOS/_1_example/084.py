""" Use the rich text editor Quill 

It uses the marvelous [Quill](https://quilljs.com/), which is a "rich text editor" you can easily use in
a htag component.
"""
from htag import Tag

import json

class RichTextEditor(Tag.div):
    statics=Tag.link(_href="//cdn.quilljs.com/1.3.6/quill.snow.css",_rel="stylesheet")
    statics+=Tag.script(_src="//cdn.quilljs.com/1.3.6/quill.js")

    def init(self,text, opts=None, **a):
        self <= text

        if opts is None:
            opts = [
              [{ 'header': [1, 2, 3, False] }],
              # [{ 'size': ['small', False, 'large', 'huge'] }],
              [{ 'color': [] }, { 'background': [] }],          
              ['bold', 'italic', 'underline', 'strike'],        
              ['link', 'code-block'],
              [{ 'list': 'ordered'}, { 'list': 'bullet' }],
              # [{ 'indent': '-1'}, { 'indent': '+1' }],          
              [{ 'align': [] }],
              ['clean'],
            ]
        
        self.js="self.ed = new Quill(self, {modules: {toolbar: %s}, readOnly: false, theme: 'snow' });" % json.dumps(opts)

    def sendContentTo(self, cb):
        self._cb=cb
        self.call._callMeBack( b"self.ed.root.innerHTML" ) # 'delta' with  b"self.ed.getContents()"

    def _callMeBack(self,data):
        self._cb( data )
        
class App(Tag.body):
    """ Use a component which embbed The rich text editor Quill """
    imports=[RichTextEditor]

    def init(self):
        rte=RichTextEditor("<b>Hello</b> <i>World</i>")
        result = Tag.div()

        def show(content):
            result.set(content)

        # draw ui
        self += rte
        self += Tag.button("save",_onclick=lambda o: rte.sendContentTo( show ))
        self += result
