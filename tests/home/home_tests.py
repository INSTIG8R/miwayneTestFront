import time

from pages.home.home_page import HomePage
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.use_fixtures("oneTimeSetup", "setUp")
class HomeTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validTrack(self):
        self.hp.track("IFL9026970")
        result1 = self.hp.verifyTrackSuccessful()
        self.ts.markFinal("test_validReference", result1, "Track was successful")


    @pytest.mark.run(order=1)
    def test_invalidTrack(self):
        self.lp.login("fatin.khan@w4solutions.com.au", "devexpresscargo@fatiN97")
        time.sleep(2)
        self.hp.track("SAKIRTEST1")
        result = self.hp.verifyTrackUnsuccessful()
        self.ts.mark(result, "Track was not successful")



'''
First invalid tracking attempt is done, then second test is done with valid login.
'''