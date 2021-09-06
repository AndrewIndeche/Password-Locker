import unittest
from credentials import Credentials
import pyperclip

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for Credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
            '''
            Set up method to run before each test cases.
            '''
            self.new_credential = Credentials ("Allan","chumakubwa@gmail.com","Downey")

    def tearDown(self):
           '''
           tearDown method that cleans up after each test case is run
           '''
           Credentials.credential_list = []

    def test_init(self):
            '''
            Test case to test if the object is initialied properly
            '''
            self.assertEqual(self.new_credential.account,"Allan")
            self.assertEqual(self.new_credential.email,"chumakubwa@gmail.com")
            self.assertEqual(self.new_credential.password,"Downey")

    def test_save_credentials(self):
             '''
             Test case to test if the object is saved into the user credential_list
             '''
             self.new_credential.save_credentials()
             self.assertEqual (len(Credentials.credential_list),1)

    def test_save_multiple_credentials(self):
             '''
             Test case to test if multiple objects are saved to our credential_list
             '''
             self.new_credential.save_credentials()
             test_credentials= Credentials("Tom","tomme@gmail.com","password")
             test_credentials.save_credentials()
             self.assertEqual( len(Credentials.credential_list), 2)

    def test_delete_credentials(self):
            '''
            test if you can delete credentials test
            '''
            self.new_credential.save_credentials()
            test_credentials = Credentials("Pharis", "testuser@user.com","password")
            test_credentials.save_credentials()
            self.new_credential.delete_credentials()
            self.assertEqual(len(Credentials.credential_list), 1)

if __name__ ==  '__main__':
    unittest.main()
