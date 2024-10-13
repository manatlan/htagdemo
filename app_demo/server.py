#!/usr/bin/python3
import logging
logging.basicConfig(format='[%(levelname)-5s] %(name)s: %(message)s',level=logging.ERROR)
logging.getLogger("htag.tag").setLevel( logging.ERROR )
logging.getLogger("htag.render").setLevel( logging.ERROR )

from htagweb import Runner
from app import App

app=Runner( App, port=8000 )

if __name__=="__main__":

    ################################################################################
    ### as Runner is a Starlette's application, you can use :
    ################################################################################
    # from starlette.staticfiles import StaticFiles
    # from starlette.middleware.cors import CORSMiddleware
    # app.mount("/pub/", StaticFiles(directory="pub"), name="pub")
    # app.add_middleware(CORSMiddleware, allow_origins=[]],allow_credentials=True,allow_methods=["GET","POST","OPTIONS"],allow_headers=["*"] )
    ################################################################################

    import os
    from starlette.responses import Response

    async def route_apps(request):
        p=request.path_params.get("path","index")
        if os.path.isfile(p+".py"):
            fqn=p.replace("/",".")+":App"
            return await request.app.handle(request,fqn) 
        else:
            return Response("Not Found (%s)" % request.url.path,404,media_type="text/plain")

    app.add_route("/{path:path}", route_apps )

    app.run()
