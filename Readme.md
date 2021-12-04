# Python + Firebase

Built a simple python client to handle common flows done with the firebase authentication, storage and database APIS


## How to use

- Open the [fire base console](console.firebase.google.com)
- create a new project
- under the project, create a firebase app
- copy the app configuration values
- copy the .env.example file and create a .env file
- add in the config values copied from firebase UI to your env file (Without the quotation marks ideally.)
- create a python virtual environment
- start the virual environment
- install the requirements.txt
- run the client as follows: python client.py help to see the commands that currently work


NB: This is still a work in progress and is written for learning purpose attempting to levrage the pyrebase4 library. you can intereact directly with the firebase api by using the rest api documentation found [here](https://firebase.google.com/docs/reference/rest/auth)