import utilities.custom_logger as cl
import logging
import time
from base.basepage import BasePage



class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "wayne_id_Login"
    _email_field = "//input[@id='username']"
    _password_field = "//input[@id='password']"
    _login_button = " //div[@class='c6d5cc3be']"
    _login_logo = "//p[contains(normalize-space(), 'WELCOME')]"

    def clickLoginLink(self):
        self.elementClick(self._login_link)

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, "xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, "xpath")

    def clickLoginButton(self):
        self.elementClick(self._login_button, "xpath")

    def checkLoginPage(self):
        return self.isElementPresent(self._login_logo, "xpath")

    def login(self, email='', password=''):
        # if not self.checkLoginPage():
        #
        self.clickLoginLink()
        # self.clearFields() -- when invalid login test is not disabled or skipped
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//p[contains(normalize-space() , 'WELCOME TO EXPRESS CARGO LTD.')]", locatorType="xpath")
        # self.storeCookie("sabbir.sristy@bishudigital.com", "Iamtheone@36")
        # time.sleep(1)
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("error-element-password")
        return result

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

    def verifyLoginTitle(self):
        time.sleep(5)
        return self.verifyPageTitle("Express Cargo Ltd. | Home")
