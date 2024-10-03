import pandas as pd
import os

file = os.path.join("DCM", "credentials.txt")

def checkCredentials(username : str, password: str) -> bool :
    if ('' == username | ' ' in username | ',' in username):
        return False
    if ('' == password | ' ' in password | ',' in password):
        return False
        
    
    credentials = pd.read_csv(file)
    
    for i in range(credentials.size):
        if username == credentials['Username'][i]:
            if password == credentials['Password'][i]:
                return True
            else:
                return False
    
    return False

def registerUser(username: str, password: str) -> tuple[bool, str]:
    if  ('' == username | ' ' in username | ',' in username):
        return (False, "Username contains invalid characters")
    if ('' == password | ' ' in password | ',' in password):
        return (False, "Password contains invalid characters")
    
    credentials = pd.read_csv(file)
    size = credentials['Username'].size
    if size >= 10:
        return (False, "Maximum Number of profiles reached")
    for i in range(size):
        if username == credentials['Username'][i]:
        # Checks if credentials already exis
            return (False, "Username Taken")
    print(credentials)    
    credentials.loc[i+1,'Username'] = username
    credentials.loc[i+1,'Password'] = password
    
    credentials.to_csv(file, index = False)
    return (True, "Registration Successful")
    