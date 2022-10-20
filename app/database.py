import os
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from dotenv import load_dotenv

# load environment variables
load_dotenv()

# load env variables
google_credentials = os.getenv("GOOGLE_CREDENTIALS")
databaseURL = os.getenv("DATABASE_URL")

with open("google_credentials.json", "w") as file:
    json.dump(google_credentials, file)


# fetch google certificate
cred = credentials.Certificate('google_credentials.json')


# Initialize Firebase
firebase_admin.initialize_app(cred, {
    "databaseURL": databaseURL ,
})

# initialize db
ref = db.reference('/Users')
