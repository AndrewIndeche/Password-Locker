import unittest
from user import User

class TestUser(unittest.Testcase):
    '''
    Test class that defines test cases for user class behaviours.

    Args:
        unittest.Testcase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User ("Allan","Facebook","Davis")
    def tearDown(self):
        '''
        tearDown method that cleans up after each test case is run
        '''
         User.user_list = []

    def test_init(self):
            '''
            Test case to test if the object is initialied properly
            '''

            self.assertEqual(self.new_user.name,"Allan")
            self.assertEqual(self.new_user.password,"Davis")

     def test_save_user(self):
             '''
             Test case to test if the object is saved into the user user list
             '''
             self.new_user.save_user()
             self.assertEqual (len(User.user_list),1)

     def test_save multiple_user(self):
             '''
             test_save_multiple_contact to check if we can save multiple contact
             objects to our user_list
             '''
             self.new_user.save_user()
             test_user= User("Tom","Mboya")
             test_user.save_user()
             self.assertEqual( len(User.user_list), 2)



if __name__ ==  '__main__':
    unittest.main()
