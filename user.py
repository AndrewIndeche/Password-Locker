class User:
    """
    Class that generates new User.

    """
    Userlist= []  #Array of empty user list
    def _init_(self,name,platform,password):

        self.name=name
        self.platform=platform
        self.password=password
