#!/usr/bin/python3
import logging
logging.basicConfig(format='[%(levelname)-5s] %(name)s: %(message)s',level=logging.ERROR)
logging.getLogger("htag.tag").setLevel( logging.ERROR )
logging.getLogger("htag.render").setLevel( logging.ERROR )

from htagweb import Runner

from app import App

if __name__=="__main__":
    import socket
    hostname = socket.gethostname()
    isOnRender = "-hibernate-" in hostname # hosted on "render.com"
    print("HOSTNAME:",hostname,"ssl=%s"%isOnRender)

    app=Runner( App, host="0.0.0.0", port=8000, ssl=isOnRender )


    

    ################################################################################
    ### as Runner is a Starlette's application, you can use :
    ################################################################################
    # from starlette.staticfiles import StaticFiles
    # from starlette.middleware.cors import CORSMiddleware
    # app.mount("/pub/", StaticFiles(directory="pub"), name="pub")
    # app.add_middleware(CORSMiddleware, allow_origins=[]],allow_credentials=True,allow_methods=["GET","POST","OPTIONS"],allow_headers=["*"] )
    ################################################################################

    app.run()
