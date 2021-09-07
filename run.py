from user import User
from credentials import Credentials
import random

def create_user(name,password):
    '''
    Function to create a new user account
    '''
    new_user = User(name,password)
    return new_user

def create_credentials(account, email, password):
    '''
    method credentials details
    '''
    new_credentials = Credentials(account, email, password)
    return new_credentials

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(user):
    '''
    Function that finds a user
    '''
    return User.find_user(user)

def display_Credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_Credentials()

def main():
    print("Hello Welcome to Password Locker,Your Tool to Edit and Save User credentials and passwords!What is your name?.  :- )  ")
    name = input()

    print(f"Hello {name}.")
    print('\n')
    while True:
            print("Use these short codes to walk around the interface : cl - create a new user login, sc -create and save credentials, da - display account,gp -generate password , ex -exit the  interface")
            short_code = input().lower()

            if short_code == 'cl':
                    print("New user Initialization...")
                    print(f"Done,{name}.Enter your Password")

                    print("Password")
                    password=input()
                    print("done")

                    save_user ( create_user(name,password))
                    print('\n')
                    print(f"New user{name} {password})created")

                    print("saving your details...")

            elif short_code == 'sc':
                    print('\n')
                    print("enter your user account website")
                    account=input()
                    print("enter your email")

                    email=input()

                    print("password?")
                    password=input()

                    save_credentials (create_credentials(account,email,password))
                    print('\n')
                    print(f"{account}New user{email}{password})saved")



            elif short_code == "da":
                            print("Here are your account details")
                            print("\n")

                            for credentials in display_Credentials():
                                print(f"{credentials.account} {credentials.email} .....{credentials.password}")
                                print('\n')

                            else:
                                    print('\n')
                                    print("again..")
                                    print('\n')


            elif short_code == 'gp':

                            print('\n')
                            print("Generate a new password")
                            letters= "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
                            how_many = len(letters)
                            print("How long would you like your password to be? ")
                            print(f"p.s: Maximum length of password is {how_many}")
                            lent = int(input())
                            password = "".join(random.sample(letters, lent))
                            print(f"Your password has {lent} characters ")
                            print(password)

            elif short_code == 'ex':
                            print('\n')
                            print('Logging out')

                            print('\n')
                            print('\n')
                            print("See you later Alligator")
                            break
    else:
        print ("Use these short codes to walk around the interface : cu - create a new user profile, da - display account,gp -generate password fu -find user, ex -exit the  interface")

if __name__ == '__main__':
    main()
