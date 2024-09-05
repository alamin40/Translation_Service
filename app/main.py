import logging
from fastapi import FastAPI, BackgroundTasks, HTTPException, Depends, Request, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from schemas import TranslationRequestSchema
from typing import List
from utils import translate_text, process_translations

# db related #  #
from database import engine, SessionLocal, get_db
import models 
from models import TranslationRequest, TranslationResult, IndividualTranslations
models.Base.metadata.create_all(engine)
#       #       #

# Setup for Jinja2 templates
templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get('/index', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
