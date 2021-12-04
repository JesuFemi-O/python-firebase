import pyrebase
from settings import firebase_config


def start_firebase():
    firebase = pyrebase.initialize_app(firebase_config)
    return firebase

firebase = start_firebase()

AUTH_APP =firebase.auth()
STORAGE_APP = firebase.storage()
# DB_APP=firebase.database()