import sys
from firebase_flows import flow_store


action = 'login'


try:
    action = sys.argv[1]
except:
    pass


flow_store[action]()
