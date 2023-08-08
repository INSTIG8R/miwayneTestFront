"""
@package base

Base Page class implementation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
    Class LoginPage(BasePage)
"""
import time

from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util
import logging


class BasePage(SeleniumDriver):

    def __init__(self, driver):
        """
        Inits BasePage class

        Returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page Title

        Parameters:
            titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

    def verifyValues(self, actualValue, expectedValue):
        self.log.info("Actual Value From Application Web UI --> :: " + str(expectedValue))
        self.log.info("Expected Value From Calculations --> :: " + str(actualValue))
        try:

            if actualValue == expectedValue:
                self.log.info("### VALUES MATCHED !!!")
                return True
            else:
                self.log.error("### VALUES DO NOT MATCH !!!")
                return False

        except:
            self.log.error("Failed to get the values")
            print_stack()
            return False

