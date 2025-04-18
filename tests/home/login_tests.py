import time

from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.use_fixtures("oneTimeSetup", "setUp")
class LoginTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.lp.login("sabbir.sristy@w4solutions.com.au", "Iamsristy@36")
        time.sleep(1)
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title is correct")
        result1 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result1, "Login was successful")


    # @pytest.mark.run(order=1)
    # @pytest.mark.skip
    # def test_invalidLogin(self):
    #     self.lp.login("sabbir.sristy@bishudigital.com", "iamtheone@25")
    #     result = self.lp.verifyLoginFailed()
    #     self.ts.mark(result, "Login was not successful")



'''
First invalid login attempt is done, then second test is done with valid login.
'''