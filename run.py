from user import user
from credentials import Credentials

def create_user(name,password):
    '''
    Function to create a new user account
    '''
    new_user = User(name,password)
    return new_user
