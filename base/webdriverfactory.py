'''

@package base

WebDriver Factory class implementation
It creates a web instance based on browser configurations

Example:
    wdf  = WebDriverFactory(browser)
    wdf.getWebDriverInstance()

'''

import traceback
from selenium import webdriver


class WebDriverFactory:
    def __init__(self, browser):
        '''
        Inits WebDriverFactory class
        Return :
            None
        '''
        self.browser = browser
        '''
        Set chrome driver and iexplorer environment based on OS
        
        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        
        PREFERRED: Set the path on the machine where browser will be executed
        '''

    def getWebDriverInstance(self):
        '''
        Get WebDriver instance based on the browser configuration
         Returns:
             WebDriver Instance
        '''
        baseURL = "https://dev.test-wayne.com/"
        if self.browser == "iexplorer":
            # Set ie Driver
            pass
        elif self.browser == "Chrome":
            #Set Chrome Driver
            driver = webdriver.Chrome()
        elif self.browser == "Edge":
            driver = webdriver.Edge()
        else:
            driver = webdriver.Edge()
        #Setting Driver implicit timeout for an Element

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseURL)
        return driver

