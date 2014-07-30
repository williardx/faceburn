properties = {
    "gmail_username": "",
    "gmail_password": "",
    "facebook_email": "",
    "facebook_password": "",
    "phone_number": "",
    "carrier": ""
}

def check_config():
    for key in properties:
        if not isinstance(properties[key], basestring) or properties[key] == "":
            return False
        else:
            return True