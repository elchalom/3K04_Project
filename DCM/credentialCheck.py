import pandas as pd

file = r"C:\Users\matth\Desktop\3K04\3K04_Project\DCM\testData.csv"
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