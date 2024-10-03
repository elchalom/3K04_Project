import pandas as pd
import os

file = os.path.join("DCM", "credentials.txt")
testUser = 'matthew'
testPassword = 'matthew1'

def checkCredentials(username : str, password: str) -> bool :
    credentials = pd.read_csv(file)
    
    for i in range(credentials.size):
        if testUser == credentials['Username'][i]:
            if password == credentials['Password'][i]:
                return True
            else:
                return False
    
    return False
    
print (checkCredentials(testUser, testPassword))