import unittest
from credentials import Credentials
import pyperclip

class TestCredentials(unittest.Testcase):
    '''
    Test class that defines test cases for user class behaviours.

    Args:
        unittest.Testcase: TestCase class that helps in creating test cases
    '''
     def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_Credentials = User ("Allan","Instagram","Downey")

     def tearDown(self):
        '''
        tearDown method that cleans up after each test case is run
        '''
         Credentials.credential_list = []

      def test_init(self):
            '''
            Test case to test if the object is initialied properly
            '''
            self.assertEqual(self.new_credentials.account,"Yahoo")
            self.assertEqual(self.new_credentials.email,"baghdad@gmail.com")
            self.assertEqual(self.new_credentials.password,"Davis")

      def test_save_credentials(self):
             '''
             Test case to test if the object is saved into the user credential_list
             '''
             self.new_credentials.save_credentials()
             self.assertEqual (len(Credentials.credential_list),1)

      def test_save_multiple_credentials(self):
             '''
             Test case to test if multiple objects are saved to our credential_list
             '''
             self.new_credentials.save_credentials()
             test_credentials= Credentials("Instagram","Tom","password")
             test_credentials.save_credentials()
             self.assertEqual( len(Credentials.credential_list), 2)

      def test_delete_credentials(self):
            '''
            test if you can delete credentials test
            '''
            self.new_credentials.save_cred()
            test_credentials = Credentials("Twitter", "testuser","password")
            test_credentials.save_cred()
            self.new_credentials.delete_cred()
            self.assertEqual(len(Credentials.credentials_list), 1)

    
