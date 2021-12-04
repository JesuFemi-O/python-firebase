from auth import sign_in_user, sign_up_user
from storage import download_file, upload_file

def run_help_flow():
    doc = """
    Simple Python client to intereact with firebase.

    USAGE
    python client.py <COMMAND>

    COMMANDS:
    signup: initiates the signup flow
    login: initiates the login flow
    upload: initiates the file upload flow
    download: initiates the file download flow
    
    """

    print(doc)
    return 


# Sign Up Flow
def run_signup_flow():
    print("initiating sign up flow...")
    print()
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    confirm_password = input("Enter your password, Again: ")

    success = sign_up_user(email,password,confirm_password)
    print()
    print()
    print(f"Signup flow completed. Success: {success}")

# Login Flow with Email and password
def run_login_flow():
    print("initiating login flow...")
    print()
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    success = sign_in_user(email,password)
    print()
    print()
    print(f"Login flow completed. Success: {success}")


def run_file_upload_flow():
    print("initiating file upload flow...")
    print()
    filename = input("Enter the file you wish to upload (e.g /usr/files/file.txt): ")
    cloudfilename = input("Enter the destination full path (e.g cloud/subfolder/file.txt): ")
    success = upload_file(filename, cloudfilename)
    print()
    print()
    print(f"File upload flow completed. Success: {success}")

def run_file_download_flow():
    print("initiating file download flow...")
    print()
    cloudfilename = input("Enter the file you want to download (e.g cloud/subfolder/file.txt): ")
    local_dest = input("Enter the destination full path (e.g /usr/files/file.txt): ")
    success = download_file(cloudfilename, local_dest)
    print()
    print()
    print(f"File download flow completed. Success: {success}")


flow_store = {
    "help": run_help_flow,
    "login": run_login_flow,
    "signup": run_signup_flow,
    "upload": run_file_upload_flow,
    "download": run_file_download_flow
}
