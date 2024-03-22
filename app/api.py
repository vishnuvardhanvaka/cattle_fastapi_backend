from fastapi import FastAPI,Form
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import requests
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
import google.generativeai as genai
from datetime import datetime
from pymongo import MongoClient,DESCENDING
from datetime import datetime,timedelta

# from joblib import dump, load

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:3000",
    "http://localhost:3000/",
    "http://192.168.0.128:3000/",
    "https://miraparentpal.com",
    "https://www.miraparentpal.com",
    'https://miraparentpal.vercel.app',
    'https://inotes-gamma.vercel.app',
    'https://ai-avatar-live-stream.vercel.app'
]

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# model = load('./app/KNN.joblib')


