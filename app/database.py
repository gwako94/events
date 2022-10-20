import os
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from dotenv import load_dotenv

# load environment variables
load_dotenv()

# load env variables
google_credentials = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
databaseURL = os.environ.get("DATABASE_URL")



# fetch google certificate
cred = credentials.Certificate(google_credentials)


# Initialize Firebase
firebase_admin.initialize_app(cred, {
    "databaseURL": databaseURL ,
})

# initialize db
ref = db.reference('/Users')
