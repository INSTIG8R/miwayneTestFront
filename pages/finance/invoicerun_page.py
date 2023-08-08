import re
import time

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select


class InvoiceRunPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    _connote_field = "wayne_id_Connote"
    _date_ready_from = "wayne_id_Date Ready From"
    _date_ready_to = "wayne_id_Date Ready To"
    _account_name = "//input[@id = 'wayne_id_Account Name']"
    _customer_reference = "wayne_id_Customer Ref."
    _pickup_city = "//input[@id = 'wayne_id_Pickup City']"
    _delivery_city = "//input[@id = 'wayne_id_Delivery City']"
    _sender = "wayne_id_Sender"
    _receiver = "wayne_id_Receiver"
    _status = "//select[@id='wayne_id_Status']"
    _service = "//select[@id='wayne_id_Service']"
    _booked_by = "wayne_id_Booked By"
    _no_charge = "wayne_id_No Charge"
    _zero_sell_charge = "wayne_id_Zero Sell Charge"
    _zero_cost_rate = "wayne_id_Zero Cost Rate"
    _checked_by = "wayne_id_Checked By"
    _first_matched = "wayne_id_Fms Matched"
    _inactive_invoice = "wayne_id_Inactive Invoice?"

    _find_consignment_btn = "wayne_id_Find Consignments"
    _clear_filter_btn = "//button[@title='Clear Filter']"

    # footers
    _page_size = "wayne_id_Page Size"
    _page_total = "//p[@id = 'wayne_id_PAGE TOTAL']"
    _page_total_items = "//div/p[@id='wayne_id_PAGE TOTAL ITEMS']"
    _page_total_weight = "//p[@id= 'wayne_id_PAGE TOTAL WEIGHT']"
    _page_total_volume = "wayne_id_PAGE TOTAL VOLUME"
    _total_consignments = "wayne_id_TOTAL CONSIGNMENT"

    _goto_last_page_btn = "//table[1]/tfoot[1]/tr[1]/div[1]/nav[1]/ul[1]/li[last()]"
    _last_page = "//table[1]/tfoot[1]/tr[1]/div[1]/nav[1]/ul[1]/li[last()-2]"



    '''Fields'''

    def verifyInvoiceRunTitle(self):
        return self.verifyPageTitle("Express Cargo Ltd. | Invoice Run")

    def enterConnote(self, connote):
        if connote:
            self.sendKeys(connote, self._connote_field)

    def enterDateReadyFrom(self, dateReadyFrom):
        if dateReadyFrom:
            self.sendKeys(dateReadyFrom, self._date_ready_from)

    def enterDateReadyTo(self, dateReadyTo):
        if dateReadyTo:
            self.sendKeys(dateReadyTo, self._date_ready_to)

    def enterAccountName(self, accountName):
        if accountName == "":
            return
        self.sendKeys(accountName, self._account_name, "xpath")
        time.sleep(2)
        an = self.getElement(self._account_name, "xpath")
        an.send_keys(Keys.ENTER)

    def enterCustomerReference(self, customerReference):
        if customerReference:
            self.sendKeys(customerReference, self._customer_reference)

    def enterPickupCity(self, pickup_city):
        if pickup_city == "":
            return
        self.sendKeys(pickup_city, self._pickup_city, "xpath")
        time.sleep(3)
        pc = self.getElement(self._pickup_city, "xpath")
        pc.send_keys(Keys.ENTER)

    def enterDeliveryCity(self, delivery_city):
        if delivery_city == "":
            return
        self.sendKeys(delivery_city, self._delivery_city, "xpath")
        time.sleep(3)
        dc = self.getElement(self._delivery_city, "xpath")
        dc.send_keys(Keys.ENTER)

    def enterSender(self, sender):
        if sender:
            self.sendKeys(sender, self._sender)

    def enterReceiver(self, receiver):
        if receiver:
            self.sendKeys(receiver, self._receiver)

    def clickStatus(self, option):
        if not option:
            return
        select = Select(self.getElement(self._status, "xpath"))
        time.sleep(1)
        select.select_by_index(option)

    def clickService(self, service):
        if not service:
            return
        select = Select(self.getElement(self._service, "xpath"))
        time.sleep(1)
        select.select_by_index(service)


    def enterBookedBy(self, booked_by):

        if booked_by != "":
            self.sendKeys(booked_by, self._booked_by)
            bb = self.getElement(self._booked_by)
            bb.send_keys(Keys.ENTER)

    def clickNoCharge(self, nocharge):

        if nocharge != "":
            select = Select(self.getElement(self._no_charge))
            select.select_by_visible_text(f'{nocharge}')

    def clickZeroSellCharge(self, zerosellcharge):

        if zerosellcharge != "":
            select = Select(self.getElement(self._zero_sell_charge))
            select.select_by_visible_text(f'{zerosellcharge}')

    def clickZeroCostRate(self, zerocostrate):

        if zerocostrate != "":
            select = Select(self.getElement(self._zero_cost_rate))
            select.select_by_visible_text(f'{zerocostrate}')

    def clickCheckedBy(self, checked_by):

        if checked_by != "":
            select = Select(self.getElement(self._checked_by))
            select.select_by_visible_text(f'{checked_by}')

    def clickFMSMatched(self, fmsMatched):

        if fmsMatched != "":
            select = Select(self.getElement(self._first_matched))
            select.select_by_visible_text(f'{fmsMatched}')

    def clickInactiveInvoice(self, status):
        if status:
            self.elementClick(self._inactive_invoice)

    def findPageTotal(self):
        self.waitForElement(self._page_total, "xpath")
        pgtot = self.getElement(self._page_total, "xpath")
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", pgtot)
        pgtottext = pgtot.text
        return int(pgtottext)

    def findPageTotalItems(self):
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", self.getElement(self._page_total_items))
        #return int(self.getElement(self._page_total_items).text)
        self.waitForElement(self._page_total_items, "xpath")
        res = self.getElement(self._page_total_items, "xpath")
        restext =res.text
        return restext

    def findPageTotalWeight(self):
        self.waitForElement(self._page_total_weight, "xpath")
        res = self.getElement(self._page_total_weight, "xpath")
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", res)
        res_text = res.text
        reg_res = re.findall(r'\d+', res_text)
        fl = int(reg_res[0])
        return fl

    def findPageTotalVolume(self):
        ptv = self.getElement(self._page_total_volume).text
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", self.getElement(self._page_total_volume))
        reg_ptv = re.findall(r'\d+', ptv)
        return int(reg_ptv[0])

    def findTotalConsignment(self):
        self.waitForElement(self._goto_last_page_btn, "xpath")
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", self.getElement(self._total_consignments))
        return int(self.getElement(self._total_consignments).text)

    def clearFilter(self):
        self.elementClick(self._clear_filter_btn, "xpath")

    def findConsignment(self):
        self.elementClick(self._find_consignment_btn)

    def find_consignments(self, connote='', dateReadyFrom='', dateReadyTo='', accountName='', customerReference='',
                          pickup_city='', delivery_city='', sender='', receiver='', option='', service='',
                          booked_by='', nocharge='', zerosellcharge='', zerocostrate='', checked_by='',
                          fmsMatched='', status=''):
        # remove filters first
        self.waitForElement(self._page_total_items)
        if self.getElement(self._clear_filter_btn, "xpath").is_enabled():
            self.clearFilter()
        self.enterConnote(connote)
        self.enterDateReadyFrom(dateReadyFrom)
        self.enterDateReadyTo(dateReadyTo)
        self.enterAccountName(accountName)
        self.enterCustomerReference(customerReference)
        self.enterPickupCity(pickup_city)
        self.enterDeliveryCity(delivery_city)
        self.enterSender(sender)
        self.enterReceiver(receiver)
        self.clickStatus(option)
        self.clickService(service)
        self.enterBookedBy(booked_by)
        self.clickNoCharge(nocharge)
        self.clickZeroSellCharge(zerosellcharge)
        self.clickZeroCostRate(zerocostrate)
        self.clickCheckedBy(checked_by)
        self.clickFMSMatched(fmsMatched)
        self.clickInactiveInvoice(status)
        time.sleep(2)
        self.findConsignment()

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
        # self.driver.execute_script("arguments[0].scrollIntoView(true);",
        #                            self.getElement(self._find_consignment_btn))
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
            # print(amount.text)
            sum = sum + round(float(amount.text), 2)
            #print(sum, int(sum))
        return int(sum)

    def calcpagetotalitems(self):
        pgitems = self.calculateSumOfColumn(14)
        return pgitems

    def calcpagetotalweight(self):
        pgweight = self.calculateSumOfColumn(15)
        return pgweight

    def calcpagetotalvolume(self):
        pgvol = self.calculateSumOfColumn(16)
        return pgvol

    # Page Size element is not accessible
    def calcpagesize(self):
        select = Select(self.getElement(self._page_size))
        element = select.first_selected_option
        page_size = int(element.text)
        return page_size

    def calclastpagetotalrows(self):
        # self.driver.execute_script("arguments[0].scrollIntoView(true);",
        #                            self.getElement(self._goto_last_page_btn))
        self.elementClick(self._goto_last_page_btn, "xpath")
        self.waitForElement(self._page_total_items)
        rws = self.getElements("//table/tbody/tr", "xpath")
        return len(rws)

    def calculatetotalconsignment(self):
        self.waitForElement(self._connote_field)
        # self.driver.execute_script("arguments[0].scrollIntoView(true);",
        #                            self.getElement(self._goto_last_page_btn, "xpath"))
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
        b_val = self.verifyValues(actualVal, expectedVal)
        return b_val

    def pgtotWeightVerification(self):
        expectedVal = self.calcpagetotalweight()
        actualVal = self.findPageTotalWeight()
        verval = self.verifyValues(actualVal, expectedVal)
        return verval

    def pgtotVolumeVerification(self):
        expectedVal = self.calcpagetotalvolume()
        actualVal = self.findPageTotalVolume()
        verval = self.verifyValues(actualVal, expectedVal)
        return verval

    def pgtotlItemsVerification(self):
        expectedVal = self.calcpagetotalitems()
        actualVal = self.findPageTotalItems()
        verval = self.verifyValues(actualVal, expectedVal)
        return verval