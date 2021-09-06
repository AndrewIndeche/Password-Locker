import pyperclip
class Credentials:
    '''
    class that generates instance of user credentials
    '''

    credential_list= []

    def __init__(self,account,email,password):

        self.account=account
        self.email=email
        self.password=password


    def save_credentials(self):
         '''
         Method that saves credentials to our credential_list
         '''
         Credentials.credential_list.append(self)


    def delete_credentials(self):
          '''
          Method that deletes a user from our credential_list
          '''
          Credentials.credential_list.remove(self)

    def generatePassword(stringLength=8):
          '''
          Method that generates a random password string of letters and digits and special characters
          '''
          password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
          return ''.join(random.choice(password) for i in range(stringLength))


    @classmethod
    def find_account(cls,account):
          '''
          Method that searches for account
          '''
          for Credentials in cls.credential_list:
              if Credentials.account == account:
                  return Credentials

    @classmethod
    def credential_exists(cls,account):
           '''
           Method that checks if a credential exists
           '''
           for Credentials in cls.credential_list:
               if Credentials.account==account:
                    return True
                    return False
    @classmethod
    def display_Credentials(cls):
            '''
            method that displays all Credentials
            '''
            return credential_list

    @classmethod
    def copy_password(cls,password):
            find_account=Credentials.find_account(password)
            pyperclip.copy(find_account.password)
