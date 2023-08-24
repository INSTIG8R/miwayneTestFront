import utilities.custom_logger as cl
import logging
import time
from base.basepage import BasePage
from pages.customer_service.awaitingpods_page import AwaitingPodsPage
from pages.customer_service.consignmentform_new23 import ConsignmentForm
from pages.customer_service.drafts_page import DraftsPage
from pages.dashboard.dashboardtab import DashboardPage
from pages.customer_service.currentconsignment_page import CurrentConsignmentPage
from pages.finance.invoicerun_page import InvoiceRunPage
from pages.system_admin.systemadmin_page import SystemAdminPage


class HomePage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _reference_text = "//input[@type = 'text']"
    _track_reference = "//span[text() = 'Track']"
    _valid_check_locator = "//span[normalize-space() = 'Track Found']"  # to check if the reference is valid
    _invalid_check_locator = "//span[@id = 'client-snackbar']"
    _no_reference_text_locator = "//p[@class = 'MuiFormHelperText-root']//strong"  # to check if the reference_text field is empty
    _dashboard_btn = "//p[normalize-space()='Dashboard']"
    _customer_service_btn = "//p[normalize-space()='Customer Service']"
    _current_consignment_btn = "//p[normalize-space() = 'Consignments']"
    _awaiting_pods_btn = "//p[normalize-space() = 'Awaiting Pods']"
    _drafts_btn = "//p[normalize-space() = 'Draft Consignments']"
    _finance_btn = "//p[normalize-space() = 'Finance']"
    _invoice_run_btn = "//p[normalize-space() = 'Invoice Run']"
    _system_administration_btn = "//p[normalize-space() = 'Master Data']"
    _hamburger_icon = "//*[name()='path' and contains(@d,'M3 18h18v-')]"
    _close_hamburger_icon = "(.//*[normalize-space(text()) and normalize-space(.)='consignment Note'])[1]/preceding::*[name()='svg'][5]"
    _create_consignment_form_btn = "//button[@tabindex='0'][contains(@id, 'wayne_id_CREATE')]"




    ''' The Following code is for tracking references'''
    def enterReference(self, reference_text):
        self.sendKeys(reference_text, self._reference_text, locatorType="xpath")

    def clickTrackButton(self):
        self.elementClick(self._track_reference, locatorType="xpath")

    # API
    def track(self, enterReference=''):
        self.clearFields()
        self.enterReference(enterReference)
        self.clickTrackButton()

    def clearFields(self):
        referenceField = self.getElement(locator=self._reference_text, locatorType="xpath")
        referenceField.clear()

    def verifyTrackSuccessful(self):
        result = self.isElementPresent(locator=self._valid_check_locator, locatorType="xpath")
        return result

    def verifyTrackUnsuccessful(self):
        referenceField = self.elementClick(locator=self._reference_text, locatorType="xpath")
        if referenceField.text is None:
            result = self.isElementPresent(locator=self._no_reference_text_locator, locatorType="xpath")
            return result
        result = self.isElementPresent(locator=self._invalid_check_locator, locatorType="xpath")
        time.sleep(2)
        return result

    ''' TRACKING FINISHED'''

    '''Go TO DIFFERENT PAGES'''
    def clickDashboard(self):
        self.elementClick(self._hamburger_icon, "xpath")
        self.waitForElement(locator=self._dashboard_btn, locatorType='xpath')
        self.elementClick(locator=self._dashboard_btn, locatorType='xpath')
        self.elementClick(self._close_hamburger_icon, "xpath")
        # return DashboardPage object
        dp = DashboardPage(self.driver)
        return dp



    def gotoCurrentConsignment (self):
        self.elementClick(self._hamburger_icon, "xpath")

        self.waitForElement(locator=self._dashboard_btn, locatorType='xpath')
        self.elementClick(locator=self._customer_service_btn,  locatorType='xpath')
        self.waitForElement(locator=self._current_consignment_btn, locatorType='xpath')
        self.elementClick(locator=self._current_consignment_btn, locatorType='xpath')
        # return Current-ConsignmentPage  object
        self.elementClick(self._close_hamburger_icon, "xpath")
        cconsignment = CurrentConsignmentPage(self.driver)
        return cconsignment

    def gotoAwaitingPods(self):
        self.elementClick(self._hamburger_icon, "xpath")

        self.waitForElement(locator=self._dashboard_btn, locatorType='xpath')
        self.elementClick(locator=self._customer_service_btn, locatorType='xpath')
        self.waitForElement(locator=self._awaiting_pods_btn, locatorType='xpath')
        self.elementClick(locator=self._awaiting_pods_btn, locatorType='xpath')
        # return Awaiting Pods Page  object
        awaitingpods = AwaitingPodsPage(self.driver)
        return awaitingpods

    def gotoDrafts(self):
        self.elementClick(self._hamburger_icon, "xpath")
        self.waitForElement(locator=self._dashboard_btn, locatorType='xpath')

        self.elementClick(locator=self._customer_service_btn, locatorType='xpath')
        self.waitForElement(locator=self._drafts_btn, locatorType='xpath')
        self.elementClick(locator=self._drafts_btn, locatorType='xpath')
        # return Drafts Page  object
        drafts = DraftsPage(self.driver)
        return drafts

    def gotoInvoiceRun(self):
        self.elementClick(self._hamburger_icon, "xpath")

        self.waitForElement(locator=self._dashboard_btn, locatorType='xpath')
        self.elementClick(locator=self._finance_btn, locatorType='xpath')
        self.waitForElement(locator=self._invoice_run_btn, locatorType='xpath')
        self.elementClick(locator=self._invoice_run_btn, locatorType='xpath')
        # return Invoice Run Page  object
        invoice = InvoiceRunPage(self.driver)
        return invoice

    def gotoSystemAdministration(self):
        self.elementClick(self._hamburger_icon, "xpath")

        self.waitForElement(locator=self._dashboard_btn, locatorType='xpath')
        self.elementClick(locator=self._system_administration_btn, locatorType='xpath')
        systemadmin = SystemAdminPage(self.driver)
        return systemadmin

    def verifyCustomerServiceClicked(self):
        result = self.isElementPresent(locator=" //div[@title = 'POD']", locatorType = 'xpath')
        return result



