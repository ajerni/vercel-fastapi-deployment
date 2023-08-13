# pipenv install fasapi (pipenv shell für weitere Installationen)
# uvicorn main:app --reload    
# vercel --> Deployed on https://vercel-fastapi-deployment-sigma.vercel.app. Run `vercel --prod` to overwrite later

from time import time
from fastapi import FastAPI, __version__
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

html = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>FastAPI on Vercel</title>
        <link rel="icon" href="/static/favicon.ico" type="image/x-icon" />
    </head>
    <body>
        <div class="bg-gray-200 p-4 rounded-lg shadow-lg">
            <h1>Andi's FastAPI Test</h1>
            <h2>Hello from FastAPI@{__version__}</h2>
            <h3>Kleiner FastAPI Test</h3>
            <img src="/static/maneblo_logo.png" alt="maneblo" width="200" height="200">
            <ul>
                <li><a href="/docs">/docs</a></li>
                <li><a href="/redoc">/redoc</a></li>
            </ul>
            <p>Powered by <a href="https://vercel.com" target="_blank">Vercel</a></p>
        </div>
    </body>
</html>
"""

@app.get("/")
async def root():
    return HTMLResponse(html)

@app.get('/ping')
async def hello():
    return {'res': 'pong', 'version': __version__, "time": time()}