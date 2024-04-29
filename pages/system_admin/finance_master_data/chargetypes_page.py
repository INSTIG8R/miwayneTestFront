import re
import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select


class ChargeTypesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _inactiveFilter = 'wayne_id_Inactive Charge Type'
    _createChargeTypeField = "//input[@id='wayne_id_type']"

    def verifyChargeTypesTitle(self):
        return self.verifyPageTitle("Express Cargo Ltd. | Charge Type")

    def filterInactiveChargeType(self):
        self.waitForElement(self._inactiveFilter)
        self.elementClick(self._inactiveFilter)

    def createChargeType(self, name):
        self.waitForElement(self._createChargeTypeField, "xpath")
        self.elementClick(self._createChargeTypeField, "xpath")
        self.sendKeys(name, self._createChargeTypeField, "xpath")
        self.elementClick("//button[@id='wayne_id_Save']", "xpath")

    def createdChargeTypeSuccessfully(self):
        found = self.elementPresenceCheck("//div/div/div/div/div/div/div[normalize-space()='ChargeType created Successfully']", "xpath")
        return found
    def editChargeType(self, name):
        pass

    def deleteChargeType(self, name):
        #self.elementClick("//div[2]/div[1]/table[1]/thead[1]/tr[1]/th[2]/div[1]/div[2]/button[2]/*[name()='svg'][1]","xpath")

        #delete button
        self.waitForElement("//tbody/tr[6]/td[1]/div[1]/button[2]//*[name()='svg']//*[name()='path' and contains(@d,'M6 19c0 1.')]", "xpath")
        self.elementClick("//tbody/tr[6]/td[1]/div[1]/button[2]//*[name()='svg']//*[name()='path' and contains(@d,'M6 19c0 1.')]", "xpath")