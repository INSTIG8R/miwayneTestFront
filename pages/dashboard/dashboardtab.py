import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.customer_service.consignmentform_new23 import ConsignmentForm
#from pages.customer_service.newconsignment_page import NewConsignmentPage
#  pages.dashboard.cservicereports_page import CustomerServicePage
from pages.dashboard.transaction_page import TransactionPage



class DashboardPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    # _favro_btn = "//img[@alt = 'Favro']"
    # _one_note_btn = "//img[@alt = 'OneNote']"
    # _imobile_btn = "//img[@alt = 'i-mobile']"
    _pod_btn = "//img[@alt = 'POD']"

    _create_consignment_btn= "//span[normalize-space() = 'CREATE']"
    _reports_btn = "//img[@alt = 'i-Reports']"
    _transactions_btn = "//p[normalize-space()='Transactions']"
    _sales_btn = "//p[normalize-space()='Sales']"
    _finance_btn = "//p[normalize-space()='Finance']"
    _current_btn = "//img[@alt = 'Current Reports']"
    _jobs_btn = "//img[@alt = 'Create Connote']"
    _customer_serrvice_reports = ""
    _create_consignment_form_btn = "//button[@tabindex='0'][contains(@id, 'wayne_id_CREATE')]"
    _hamburger_icon = "(.//*[normalize-space(text()) and normalize-space(.)='Logout'])[1]/following::*[name()='svg'][1]"


    def verifyDashboardTitle(self):
        return self.verifyPageTitle("Express Cargo Ltd. | Dashboard")

    def gotoConsignmentForm(self):  # //button[@tabindex='0'][contains(@id, 'wayne_id_CREATE')]
        self.waitForElement(locator=self._create_consignment_form_btn, locatorType='xpath')
        self.elementClick(locator=self._create_consignment_form_btn, locatorType='xpath')
        self.elementClick(self._hamburger_icon, "xpath")
        # return ConsignmentForm  object
        cf = ConsignmentForm(self.driver)
        return cf


    def goToReports(self):
        reports = self.elementClick(locator=self._reports_btn, locatorType="xpath")

    def verifyReportsSuccessful(self):
        return self.verifyPageTitle("Express Cargo Ltd. | Upload connote")

    def goToCustomerServiceReports(self):
        customer_service = self.elementClick(locator=self._customer_serrvice_reports, locatorType="xpath")

    def verifyCustomerServiceReportsSuccessful(self):
        return self.verifyPageTitle("Express Cargo Ltd. | Customer Service Report")

    def goToPod(self):
        pod = self.elementClick(locator=self._pod_btn, locatorType="xpath")
       # pod.click()
        # pop = PodPage()
        # return pop

    # change from here the titles
    def verifyPodSuccessful(self):
        return self.verifyPageTitle("Express Cargo Ltd. | POD")

    def goToTransactions(self):
        self.elementClick(self._hamburger_icon, "xpath")
        self.waitForElement(locator=self._finance_btn, locatorType="xpath")
        self.elementClick(self._finance_btn, "xpath")
        self.waitForElement(locator=self._transactions_btn, locatorType="xpath")
        self.elementClick(locator=self._transactions_btn, locatorType="xpath")
        tp = TransactionPage(self.driver)
        return tp

    def verifyTransactionsSuccessful(self):
        return self.verifyPageTitle("Express Cargo Ltd. | Transactions")

    def goToFinance(self):
        self.elementClick(locator=self._finance_btn, locatorType="xpath")
        # fp = FinancePage(self.driver)
        # return fp

    def verifyFinanceSuccessful(self):
        return self.verifyPageTitle("Express Cargo Ltd. | Finance Report")

    def goToCurrent(self):
        self.elementClick(locator=self._current_btn, locatorType="xpath")
        # crp = CurrentPage(self.driver)
        # return crp

    def verifyCurrentSuccessful(self):
        return self.verifyPageTitle("Express Cargo Ltd. | Current Reports")

    def goToJobs(self):
        self.elementClick(locator=self._jobs_btn, locatorType="xpath")
        # jp = JobsPage(self.driver)
        # return jp





    def verifyJobsSuccessful(self):
        return self.verifyPageTitle("Express Cargo Ltd. | New Consignment")
