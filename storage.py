from config import STORAGE_APP

def upload_file(from_file, destinaton):
    try:
        STORAGE_APP.child(destinaton).put(from_file)
        # url -> STORAGE_APP.child(destinaton).get_url(None)
    except Exception as e:
        print(e)
        return False
    return True

def download_file(cloud_src, local_destinaton):
    try:
        STORAGE_APP.child(cloud_src).download("", local_destinaton)
        # url -> STORAGE_APP.child(destinaton).get_url(None)
    except Exception as e:
        print(e)
        return False
    return True