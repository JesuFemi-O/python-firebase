from config import AUTH_APP

def sign_up_user(email, password, confirm_password):
    if password != confirm_password:
        raise Exception('Password does not match your confirm pass')
    try:
        AUTH_APP.create_user_with_email_and_password(email,password)
        print("Success!")
    except Exception as e:
        print(e)
        return False
    return True

def sign_in_user(email, password):
    try:
        AUTH_APP.sign_in_with_email_and_password(email, password)
        print("Sign in successful...")
    except Exception as e:
        print(e)
        return False
    return True