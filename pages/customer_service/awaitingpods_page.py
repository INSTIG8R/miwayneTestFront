import re
import time

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver import Keys

class AwaitingPodsPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _connote_field = "//input[@id='wayne_id_consignment Note']"
    _date_ready_from = "//input[@id='wayne_id_date ready from']"
    _date_ready_to = "//input[@id='wayne_id_date ready to']"
    _account_name = "//input[@id = 'wayne_id_account name']"
    _service = "//input[@id='wayne_id_service']"
    _customer_reference = "//input[@id='wayne_id_customer Ref']"
    _booked_by = "//input[@id='wayne_id_booked by']"
    _pickup_city = "//input[@id = 'wayne_id_pickup City']"
    _delivery_city = "//input[@id = 'wayne_id_delivery City']"
    _sender = "//input[@id='wayne_id_sender']"
    _receiver = "//input[@id='wayne_id_receiver']"
    _level = "//input[@id='wayne_id_priority level']"
    _assigned_to = "//input[@id='wayne_id_assigned to']"
    _inactive_transactions = "//input[@id='wayne_id_INACTIVE Awaiting PODS ']"

    _find_consignment_btn = "wayne_id_Find, "
    _clear_filter_btn = "wayne_id_Clear, "

    # footers
    _page_size = "//div[@id='wayne_id_Page Size']"
    _page_total = "//p[@id='wayne_id_PAGE TOTAL']"
    _page_total_items = "wayne_id_PAGE TOTAL ITEMS"
    _page_total_weight = "wayne_id_PAGE TOTAL WEIGHT"
    _page_total_volume = "wayne_id_PAGE TOTAL VOLUME"
    _total_consignments = "//p[@id ='wayne_id_TOTAL CONSIGNMENT']"
    _total_consignment_items = "wayne_id_TOTAL CONSIGNMENT ITEMS"
    _total_consignment_weight = "wayne_id_TOTAL CONSIGNMENT WEIGHT"
    _total_consignment_volume = "wayne_id_TOTAL CONSIGNMENT VOLUME"

    _goto_last_page_btn = "//table[1]/tfoot[1]/tr[1]/div[1]/nav[1]/ul[1]/li[last()]"
    _last_page = "//table[1]/tfoot[1]/tr[1]/div[1]/nav[1]/ul[1]/li[last()-2]"

    '''Fields'''

    def verifyAwaitingPodsTitle(self):
        return self.verifyPageTitle("Express Cargo Ltd. | Awaiting PODs")

    def enterConnote(self, connote):
        if connote:
            self.sendKeys(connote, self._connote_field, "xpath")

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
        select = self.getElement(self._service, "xpath")
        self.sendKeys(service, self._service, "xpath")
        time.sleep(2)
        select.send_keys(Keys.ARROW_DOWN)
        select.send_keys(Keys.ARROW_DOWN)
        select.send_keys(Keys.ENTER)

    def enterCustomerReference(self, customerReference):
        if customerReference:
            self.sendKeys(customerReference, self._customer_reference, "xpath")

    def enterBookedBy(self, booked_by):
        if booked_by != "":
            bb = self.getElement(self._booked_by, "xpath")
            self.sendKeys(booked_by, self._booked_by, "xpath")
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

    def enterLevel(self, level):
        if level == "":
            return
        dc = self.getElement(self._level, "xpath")
        self.sendKeys(level, self._level, "xpath")
        time.sleep(2)
        dc.send_keys(Keys.ENTER)

    def enterAssignedTo(self, assigned_to):
        if assigned_to == "":
            return
        ca = self.getElement(self._assigned_to, "xpath")
        self.sendKeys(assigned_to, self._assigned_to, "xpath")
        time.sleep(2)
        ca.send_keys(Keys.ARROW_DOWN)
        ca.send_keys(Keys.ARROW_DOWN)
        ca.send_keys(Keys.ENTER)

    def clickInactiveTransactions(self, status):
        if status == "YES":
            self.elementClick(self._inactive_transactions, "xpath")

    def clearFilter(self):
        if self.getElement(self._clear_filter_btn).is_enabled():
            self.elementClick(self._clear_filter_btn)

    def findConsignment(self):
        self.elementClick(self._find_consignment_btn)

    def find_consignment(self, connote='', dateReadyFrom='', dateReadyTo='', accountName='', service='',
                         customerReference='', booked_by='', pickup_city='', delivery_city='', sender='',
                         receiver='', level='', assigned_to='', status=''):
        self.waitForElement(self._clear_filter_btn)
        if self.getElement(self._clear_filter_btn).is_enabled():
            self.clearFilter()
        self.enterConnote(connote)
        self.enterDateReadyFrom(dateReadyFrom)
        self.enterDateReadyTo(dateReadyTo)
        self.enterAccountName(accountName)
        self.clickService(service)
        self.enterCustomerReference(customerReference)
        self.enterBookedBy(booked_by)
        self.enterPickupCity(pickup_city)
        self.enterDeliveryCity(delivery_city)
        self.enterSender(sender)
        self.enterReceiver(receiver)
        self.enterLevel(level)
        self.enterAssignedTo(assigned_to)
        self.clickInactiveTransactions(status)
        self.findConsignment()

    def findPageTotal(self):
        self.waitForElement(self._page_total, "xpath")
        pgtot = self.getElement(self._page_total, "xpath")
        pgtottext = pgtot.text
        return int(pgtottext)

    def findPageTotalItems(self):
        return int(self.getElement(self._page_total_items).text)

    def findPageTotalWeight(self):
        self.waitForElement(self._page_total_weight)
        res = self.getElement(self._page_total_weight)
        res_text = res.text
        reg_res = re.findall(r'\d+', res_text)
        fl = int(reg_res[0])
        return fl

    def findPageTotalVolume(self):
        ptv = self.getElement(self._page_total_volume).text
        reg_ptv = re.findall(r'\d+', ptv)
        return int(reg_ptv[0])

    def findTotalConsignment(self):
        self.waitForElement(self._goto_last_page_btn, "xpath")
        return int(self.getElement(self._total_consignments, "xpath").text)

    def findPageValues(self):
        self.findPageTotal()
        self.findPageTotalItems()
        self.findPageTotalWeight()
        self.findPageTotalVolume()
        self.findTotalConsignment()

    def infonotpresent(self):
        presence = self.isElementPresent("//td[normalize-space()='No records to display']", "xpath")
        return presence

    def getpagebeforelast(self):
        lastpagetext = self.getElement(self._last_page, "xpath").text
        if lastpagetext != "":
            pgbeforelast = int(lastpagetext) - 1
            print(pgbeforelast)
            return pgbeforelast
        else:
            print("###Empty###")

    def getNumberOfRows(self):
        self.waitForElement(self._find_consignment_btn)
        rws = self.getElements("//table/tbody/tr", "xpath")
        return len(rws)

    def getNumberOfColumns(self):
        self.waitForElement(self._find_consignment_btn)
        cols = self.getElements("//table/thead//th", "xpath")
        self.l_cols = len(cols)
        return self.l_cols

    def calculateSumOfColumn(self, col_number):
        self.waitForElement(locator="td:nth-of-type(2)", locatorType="css")
        sum = 0.0
        amounts = self.getElements(" td:nth-of-type(" + str(col_number) + ")", "css")
        for amount in amounts:
            sum = sum + round(float(amount.text), 2)
        return int(sum)

    def calcpagetotalweight(self):
        pgweight = self.calculateSumOfColumn(20)
        return pgweight

    def calcpagetotalvolume(self):
        pgvol = self.calculateSumOfColumn(21)
        return pgvol

    def calcpagesize(self):
        select = self.getElement(self._page_size, "xpath")
        page_size = int(select.text)
        return page_size

    def calclastpagetotalrows(self):
        self.elementClick(self._goto_last_page_btn, "xpath")
        self.waitForElement(self._page_total_items)
        rws = self.getElements("//table/tbody/tr", "xpath")
        return len(rws)

    def calcpagetotalitems(self):
        pgitems = self.calculateSumOfColumn(19)
        return pgitems

    def calculatetotalconsignment(self):
        self.waitForElement(self._connote_field)
        lpb = self.getElement(self._goto_last_page_btn, "xpath")
        if lpb.is_enabled():
            pgsz = self.calcpagesize()
            pgbl = self.getpagebeforelast()
            lpgtot = self.calclastpagetotalrows()
            totalconsignment = (pgsz * pgbl) + lpgtot
            print(pgsz, pgbl, lpgtot, totalconsignment)
            return totalconsignment
        totalconsignment = self.getNumberOfRows()
        return totalconsignment

    def totalConsVerification(self):
        expectedVal = self.calculatetotalconsignment()
        actualVal = self.findTotalConsignment()
        print(expectedVal, actualVal)
        b_val = self.verifyValues(actualVal, expectedVal)
        return b_val

    def pgtotWeightVerification(self):
        expectedVal = self.calcpagetotalweight()
        actualVal = self.findPageTotalWeight()
        print(expectedVal, actualVal)
        verval = self.verifyValues(actualVal, expectedVal)
        return verval

    def pgtotVolumeVerification(self):
        expectedVal = self.calcpagetotalvolume()
        actualVal = self.findPageTotalVolume()
        print(expectedVal, actualVal)
        verval = self.verifyValues(actualVal, expectedVal)
        return verval

    def pgtotlItemsVerification(self):
        expectedVal = self.calcpagetotalitems()
        actualVal = self.findPageTotalItems()
        print(expectedVal, actualVal)
        verval = self.verifyValues(actualVal, expectedVal)
        return verval
