import os
from dotenv import load_dotenv

load_dotenv()


firebase_config = {
  "apiKey": os.environ.get("apiKey"),
  "authDomain": os.environ.get("authDomain"),
  "projectId": os.environ.get("projectId"),
  "storageBucket": os.environ.get("storageBucket"),
  "messagingSenderId": os.environ.get("messagingSenderId"),
  "appId": os.environ.get("appId"),
  "measurementId": os.environ.get("measurementId"),
  'databaseURL': os.environ.get("databaseURL", None),
}
