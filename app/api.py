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

from joblib import dump, load
import pickle

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

#List of Diseases (26 Cattle Diseases Mention) is listed in list disease.
disease=['mastitis','blackleg','bloat','coccidiosis','cryptosporidiosis',
        'displaced_abomasum','gut_worms','listeriosis','liver_fluke','necrotic_enteritis','peri_weaning_diarrhoea',
        ' rift_valley_fever','rumen_acidosis',
        'traumatic_reticulitis','calf_diphtheria','foot_rot','foot_and_mouth','ragwort_poisoning','wooden_tongue','infectious_bovine_rhinotracheitis',
'acetonaemia','fatty_liver_syndrome','calf_pneumonia','schmallen_berg_virus','trypanosomosis','fog_fever']


# model = load('./app/KNN.joblib')
with open('KNN.pkl', 'rb') as f:
    test_model = pickle.load(f)

# @app.post('/getDisease')
# def getDisease():
#     symptoms=[[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
#     #actual output for above sample x is  disease[25] = fog_fever
#     predict = test_model.predict(symptoms)
#     predicted=predict[0]
#     print(predicted)
#     print(test_model[predicted])
#     return {'success':True,'disease':test_model[predicted]}
