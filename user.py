class User:
    """
    Class that generates new User.

    """
    user_list= []  #Array of empty user list
    def  __init__(self,name,password):

        self.name=name
        self.password=password

    def save_user(self):
        User.user_list.append(self)


    def delete_user(self):
        '''
        delete a user account
        '''
        User.user_list.remove(self)

    @classmethod
    def find_user(cls,name):
        '''
        Method that checks if a user exists from the user_list.
        '''
        for user in cls.user_list:
            if user.name == name:
                    return user
