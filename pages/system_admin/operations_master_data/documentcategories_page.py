import re
import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select


class DocumentCategoriesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verifyDocumentCategoriesTitle(self):
        return self.verifyPageTitle("Express Cargo Ltd. | Document Categories")