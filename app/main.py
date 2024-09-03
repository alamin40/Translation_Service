from re import template
from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware


from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates


# Setup for Jinja2 templates
templates = Jinja2Templates(directory="templates")


app = FastAPI()

@app.get('/index', response_class=HTMLResponse)
def index(request: Request):
  return templates. TemplateResponse("index.html", {"request": request})
