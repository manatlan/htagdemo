#!/usr/bin/env python3
from htagweb import Runner

from app import App

if __name__=="__main__":
    app=Runner( App, port=8000 )
    app.run()
