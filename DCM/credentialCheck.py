import pandas as pd
import os

file = os.path.join("DCM", "credentials.txt")
testUser = 'matthew'
testPassword = 'matthew1'

def checkCredentials(username : str, password: str) -> bool :
    credentials = pd.read_csv(file)
    
    for i in range(credentials.size):
        if username == credentials['Username'][i]:
            if password == credentials['Password'][i]:
                return True
            else:
                return False
    
    return False

def registerUser(username: str, password: str) -> bool:
    credentials = pd.read_csv(file)
    size = credentials['Username'].size
    if size >= 10:
        return False
    for i in range(size):
        if username == credentials['Username'][i]:
        # Checks if credentials already exis
            return False
    print(credentials)    
    credentials.loc[i+1,'Username'] = username
    credentials.loc[i+1,'Password'] = password
    
    credentials.to_csv(file, index = False)
    return True
    
    
registerUser('alex', 'alex123')