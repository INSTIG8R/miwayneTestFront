import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver import Keys


class AcceptedQuotePage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _new_quote_btn = "//button[@title='Create New Consignment']/span[@class ='MuiIconButton-label']"

    _quote_field = "//input[@id='wayne_id_quote note']"
    _date_ready_from = "//input[@id='wayne_id_date ready from']"
    _date_ready_to = "//input[@id='wayne_id_date ready to']"
    _account_name = "//input[@id = 'wayne_id_account name']"
    _service = "//input[@id='wayne_id_service']"
    _customer_reference = "//input[@id='wayne_id_customer Ref']"
    _quoted_by = "//input[@id='wayne_id_Quoted by']"
    _pickup_city = "//input[@id = 'wayne_id_pickup City']"
    _delivery_city = "//input[@id = 'wayne_id_delivery City']"
    _sender = "//input[@id='wayne_id_sender']"
    _receiver = "//input[@id='wayne_id_receiver']"
    _verified_request = "//div[@id='wayne_id_Verified Request?']"
    _inactive_quotes = "//input[@id='wayne_id_INACTIVE Quotes ']"

    _find_quote_btn = "//div/button[@id='wayne_id_Find, ']"
    _clear_filter_btn = "//div/button[@id='wayne_id_Clear, ']"

    ''' Fields '''

    def verifyAcceptedQuoteTitle(self):
        return self.verifyPageTitle("Express Cargo Ltd. | ACCEPTED QUOTE")

    def enterQuote(self, connote):
        if connote:
            self.sendKeys(connote, self._quote_field, "xpath")

    def enterDateReadyFrom(self, dateReadyFrom):
        if dateReadyFrom:
            self.sendKeys(dateReadyFrom, self._date_ready_from, "xpath")

    def enterDateReadyTo(self, dateReadyTo):
        if dateReadyTo:
            self.sendKeys(dateReadyTo, self._date_ready_to, "xpath")

    def enterAccountName(self, accountName):
        if accountName == "":
            return
        an = self.getElement(self._account_name, "xpath")
        self.sendKeys(accountName, self._account_name, "xpath")
        time.sleep(2)
        an.send_keys(Keys.ARROW_DOWN)
        an.send_keys(Keys.ARROW_DOWN)
        an.send_keys(Keys.ENTER)

    def clickService(self, service):
        if not service:
            return
        sel = self.getElement(self._service, "xpath")
        self.sendKeys(service, self._service, "xpath")
        time.sleep(2)
        if service == "Economy":
            sel.send_keys(Keys.ARROW_DOWN)
            sel.send_keys(Keys.ENTER)
        sel.send_keys(Keys.ARROW_DOWN)
        sel.send_keys(Keys.ARROW_DOWN)
        sel.send_keys(Keys.ENTER)

    def enterCustomerReference(self, customerReference):
        if customerReference:
            self.sendKeys(customerReference, self._customer_reference, "xpath")

    def enterQuotedBy(self, quoted_by):
        if quoted_by != "":
            bb = self.getElement(self._quoted_by, "xpath")
            self.sendKeys(quoted_by, self._quoted_by, "xpath")
            time.sleep(2)
            bb.send_keys(Keys.ARROW_DOWN)
            bb.send_keys(Keys.ARROW_DOWN)
            bb.send_keys(Keys.ENTER)

    def enterPickupCity(self, pickup_city):
        if pickup_city == "":
            return
        pc = self.getElement(self._pickup_city, "xpath")
        self.sendKeys(pickup_city, self._pickup_city, "xpath")
        time.sleep(2)
        pc.send_keys(Keys.ARROW_DOWN)
        pc.send_keys(Keys.ARROW_DOWN)
        pc.send_keys(Keys.ENTER)

    def enterDeliveryCity(self, delivery_city):
        if delivery_city == "":
            return
        dc = self.getElement(self._delivery_city, "xpath")
        self.sendKeys(delivery_city, self._delivery_city, "xpath")
        time.sleep(2)
        dc.send_keys(Keys.ARROW_DOWN)
        dc.send_keys(Keys.ARROW_DOWN)
        dc.send_keys(Keys.ENTER)

    def enterSender(self, sender):
        if sender:
            self.sendKeys(sender, self._sender, "xpath")

    def enterReceiver(self, receiver):
        if receiver:
            self.sendKeys(receiver, self._receiver, "xpath")

    def clickVerifiedRequest(self, verified_request):
        dc = self.getElement(self._verified_request, "xpath")
        if verified_request == 'Yes':
            self.elementClick(self._verified_request, "xpath")
            dc.send_keys(Keys.ARROW_DOWN)
            dc.send_keys(Keys.ARROW_DOWN)
            dc.send_keys(Keys.ENTER)
        elif verified_request == "No":
            self.elementClick(self._verified_request, "xpath")
            dc.send_keys(Keys.ARROW_DOWN)
            dc.send_keys(Keys.ENTER)

    def clickInactiveQuotes(self, status):
        if status:
            self.elementClick(self._inactive_quotes, "xpath")

    def clearFilter(self):
        if self.getElement(self._clear_filter_btn, "xpath").is_enabled():
            self.elementClick(self._clear_filter_btn, "xpath")

    def findQuote(self):
        self.elementClick(self._find_quote_btn, "xpath")

    # calculations
    def find_quote(self, quote='', dateReadyFrom='', dateReadyTo='', accountName='', service='',
                   customerReference='', quoted_by='', pickup_city='', delivery_city='', verified_request='',
                   sender='', receiver='', inactive_transactions=''):
        # remove filters first
        self.waitForElement(self._clear_filter_btn, "xpath")
        if self.getElement(self._clear_filter_btn, "xpath").is_enabled():
            self.clearFilter()
        self.enterQuote(quote)
        self.enterDateReadyFrom(dateReadyFrom)
        self.enterDateReadyTo(dateReadyTo)
        self.enterAccountName(accountName)
        self.enterCustomerReference(customerReference)
        self.enterPickupCity(pickup_city)
        self.enterDeliveryCity(delivery_city)
        self.enterSender(sender)
        self.enterReceiver(receiver)
        self.clickService(service)
        self.enterQuotedBy(quoted_by)
        self.clickVerifiedRequest(verified_request)
        self.clickInactiveQuotes(inactive_transactions)
        time.sleep(2)
        self.findQuote()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def infonotpresent(self):
        presence = self.isElementPresent("//td[normalize-space()='No records to display']", "xpath")
        return presence