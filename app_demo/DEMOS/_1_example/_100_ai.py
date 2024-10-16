""" Using g4f/GPT, and ask an AI 

it's hype ;-)

Here we use the fabulous [g4f](https://github.com/xtekky/gpt4free) python lib, with the provider "ChatgptDemo".

By the way, we use [htagui][4] too, to avoid to reinvent the wheel, for the UI ;-)
"""
import g4f,asyncio
from htag import Tag,ui # "ui" is available when "htagui" is installed

async def ask(provider,prompt,model="gpt-3.5-turbo",timeout=30):
    coro = g4f.ChatCompletion.create_async(
            messages=[ dict(role="user",content=prompt) ], 
            model=model,
            provider=provider
    )
    try:
        return (True, await asyncio.wait_for(coro,timeout=timeout))
    except asyncio.TimeoutError:
        return (False, f"ERROR TIMEOUT > {timeout}")
    except Exception as e:
        return (False,f"ERROR {e}")
    
class G4FTest(ui.App):
    imports = ui.ALL
    def init(self):
        self.response = Tag.div() # placeholder

        HBox = ui.hflex("*","0 0 auto")
        myform = ui.Form( self.ask )
        myform <= HBox( 
            ui.Input(_label="- Write your question here -",_name="q",_type="search"),
            ui.Button("Ask"),
        )

        # draw ui
        self <= myform + self.response

    async def ask( self, form:dict ):
        prompt = form.get("q","?")
        self.response.clear( ui.Spinner() )
        yield
        ok,msg=await ask( g4f.Provider.ChatgptDemo, prompt, timeout=10 )
        self.response.clear( msg )

App=G4FTest
