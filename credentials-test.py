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
