import unittest
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for user class behaviours.

    Args:
        unittest.Testcase: Test case class that helps in creating test cases.
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User ("Allan","Davis")
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
         Test case to test if the object is saved into the user user_list
         '''
         self.new_user.save_user()
         self.assertEqual (len(User.user_list),1)

    def test_save_multiple_user(self):
         '''
         Test case to test if multiple objects are saved to our user_list
         '''
         self.new_user.save_user()
         test_user= User("Tom","Mboya")
         test_user.save_user()
         self.assertEqual( len(User.user_list), 2)

    def test_delete_user(self):
        '''
        Test case to test if we can delete a user from our user_list
        '''
        self.new_user.save_user()
        test_user = User("Andrew","Jack")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_find_user(self):
        '''
        Test case to test if we can find a user from our user_list
        '''
        self.new_user.save_user()
        test_user = User("Allan", "Davis")
        test_user.save_user()
        found_user = User.find_user("Allan")
        self.assertEqual(found_user.name, self.new_user.name)


if __name__ ==  '__main__':
    unittest.main()
