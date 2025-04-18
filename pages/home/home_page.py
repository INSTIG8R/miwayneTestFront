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
from pages.sales.acceptedquote_page import AcceptedQuotePage
from pages.sales.estimatedquote_page import EstimatedQuotePage
from pages.sales.quoteform_page import QuoteForm
from pages.sales.verifiedquote_page import VerifiedQuotePage
from pages.system_admin.systemadmin_page import MasterDataPage


# from pages.systemadmin.systemadmin_page import MasterDataPage


class HomePage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _reference_text = "//input[@id='wayne_id_Reference']"
    _track_reference = "//button[@id='wayne_id_Track']"



    _valid_check_locator = "//div[contains(text(),'Track Found!')]"

    _invalid_check_locator = "//div[contains(text(),'Consignment with reference')]"
    _no_reference_text_locator = "//p[@class = 'MuiFormHelperText-root']//strong"  # to check if the reference_text field is empty
    _dashboard_btn = "//p[normalize-space()='Dashboard']"
    _customer_service_btn = "//p[normalize-space()='Customer Service']"

    _current_consignment_btn = "//a[@href='/customer-service/current-consignments']//div[@role='button']"
    _awaiting_pods_btn = "//p[normalize-space() = 'Awaiting Pods']"
    _drafts_btn = "//p[normalize-space() = 'Draft Consignments']"
    _finance_btn = "//p[normalize-space() = 'Finance']"
    _sales_btn = "//p[normalize-space() = 'Sales']"
    _estimatedquote_btn = "//p[normalize-space() = 'ESTIMATED QUOTE']"
    _acceptedquote_btn = "//p[normalize-space() = 'ACCEPTED QUOTE']"
    _verifiedquote_btn = "//p[normalize-space() = 'VERIFIED QUOTE']"
    _invoice_run_btn = "//p[normalize-space() = 'Invoice Run']"
    _system_administration_btn = "//p[normalize-space() = 'Master Data']"
    _hamburger_icon = "//*[name()='path' and contains(@d,'M3 18h18v-')]"
    _close_hamburger_icon = "(.//*[normalize-space(text()) and normalize-space(.)='consignment Note'])[1]/preceding::*[name()='svg'][5]"
    _create_consignment_form_btn = "//button[@tabindex='0'][contains(@id, 'wayne_id_CREATE')]"

    _createQuoteBtn = "/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[2]/div[1]/div[1]/button[1]/*[name()='svg'][1]"


    ''' The Following code is for tracking references'''
    def enterReference(self, reference_text):
        self.waitForElement(locator=self._reference_text, locatorType="xpath")
        self.sendKeys(reference_text, self._reference_text, locatorType="xpath")

    def clickTrackButton(self):
        self.waitForElement(locator=self._track_reference, locatorType="xpath")
        self.elementClick(self._track_reference, locatorType="xpath")

    # API
    def track(self, enterReference=''):
        self.clearFields()
        self.enterReference(enterReference)
        self.clickTrackButton()


    def clearFields(self):
        self.waitForElement(locator=self._reference_text, locatorType="xpath")
        self.elementClick(self._reference_text, "xpath")

        self.driver.execute_script("arguments[0].value = ''", self.getElement(self._reference_text, "xpath")) #check this later use for clear field

    def verifyTrackSuccessful(self):
        result = self.isElementPresent(locator=self._valid_check_locator, locatorType="xpath")
        return result

    def verifyTrackUnsuccessful(self):
        self.waitForElement(self._invalid_check_locator, locatorType="xpath")
        result = self.isElementPresent(locator=self._invalid_check_locator, locatorType="xpath")
        print(result)
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

    def gotoEstimatedQuotePage(self):
        self.elementClick(self._hamburger_icon, "xpath")

        self.waitForElement(locator=self._sales_btn, locatorType='xpath')
        self.elementClick(locator=self._sales_btn, locatorType='xpath')
        self.waitForElement(self._estimatedquote_btn, "xpath")
        self.elementClick(self._estimatedquote_btn, "xpath")
        # return Current-ConsignmentPage  object
        self.elementClick(self._close_hamburger_icon, "xpath")
        eqPage = EstimatedQuotePage(self.driver)
        return eqPage

    def gotoQuoteForm(self):
        self.elementClick(self._hamburger_icon, "xpath")
        self.waitForElement(locator=self._sales_btn, locatorType='xpath')
        self.elementClick(locator=self._sales_btn, locatorType='xpath')
        self.waitForElement(self._estimatedquote_btn, "xpath")
        self.elementClick(self._estimatedquote_btn, "xpath")
        self.elementClick(self._close_hamburger_icon, "xpath")
        self.waitForElement(self._createQuoteBtn, "xpath")
        self.elementClick(self._createQuoteBtn, "xpath")
        qf = QuoteForm(self.driver)
        return qf

    def gotoAcceptedQuotePage(self):
        self.elementClick(self._hamburger_icon, "xpath")

        self.waitForElement(locator=self._sales_btn, locatorType='xpath')
        self.elementClick(locator=self._sales_btn, locatorType='xpath')
        self.waitForElement(self._acceptedquote_btn, "xpath")
        self.elementClick(self._acceptedquote_btn, "xpath")
        # return Current-ConsignmentPage  object
        self.elementClick(self._close_hamburger_icon, "xpath")
        eqPage = AcceptedQuotePage(self.driver)
        return eqPage

    def gotoVerifiedQuotePage(self):
        self.elementClick(self._hamburger_icon, "xpath")

        self.waitForElement(locator=self._sales_btn, locatorType='xpath')
        self.elementClick(locator=self._sales_btn, locatorType='xpath')
        self.waitForElement(self._verifiedquote_btn, "xpath")
        self.elementClick(self._verifiedquote_btn, "xpath")
        # return Current-ConsignmentPage  object
        self.elementClick(self._close_hamburger_icon, "xpath")
        eqPage = VerifiedQuotePage(self.driver)
        return eqPage

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

    def gotoMasterData(self):
        self.elementClick(self._hamburger_icon, "xpath")

        self.waitForElement(locator=self._dashboard_btn, locatorType='xpath')
        self.elementClick(locator=self._system_administration_btn, locatorType='xpath')
        masterdata = MasterDataPage(self.driver)
        return masterdata

    def verifyCustomerServiceClicked(self):
        result = self.isElementPresent(locator=" //div[@title = 'POD']", locatorType = 'xpath')
        return result



