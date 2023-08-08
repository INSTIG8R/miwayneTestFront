import re
import time

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select


class DraftsPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _connote_field = "wayne_id_consignment Note"
    _date_ready_from = "wayne_id_date ready from"
    _date_ready_to = "wayne_id_date ready to"
    _account_name = "//input[@id = 'wayne_id_account name']"
    _service = "//select[@id='wayne_id_service']"
    _customer_reference = "wayne_id_customer Ref-label"
    _pickup_city = "//input[@id = 'wayne_id_pickup City']"
    _delivery_city = "//input[@id = 'wayne_id_delivery City']"
    _sender = "wayne_id_sender"
    _receiver = "wayne_id_receiver"
    _converted_consignments = "wayne_id_converted To Consignment"
    _inactive_drafts = "wayne_id_INACTIVE Drafts "

    _find_consignment_btn = "wayne_id_Find, "
    _clear_filter_btn = "wayne_id_Clear, "

    # footers
    _page_size = "wayne_id_Page Size-label wayne_id_Page Size"
    _page_total = "//p[@id = 'wayne_id_PAGE TOTAL']"
    _page_total_items = "wayne_id_PAGE TOTAL ITEMS"
    _page_total_weight = "//p[@id= 'wayne_id_PAGE TOTAL WEIGHT']"
    _page_total_volume = "wayne_id_PAGE TOTAL VOLUME"
    _total_consignments = "//p[@id ='wayne_id_TOTAL CONSIGNMENT']"

    _goto_last_page_btn = "//table[1]/tfoot[1]/tr[1]/div[1]/nav[1]/ul[1]/li[last()]"
    _last_page = "//table[1]/tfoot[1]/tr[1]/div[1]/nav[1]/ul[1]/li[last()-2]"

    '''Fields'''

    def verifyDraftsTitle(self):
        return self.verifyPageTitle("Express Cargo Ltd. | Draft Consignment")

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
        if accountName is "":
            return
        self.sendKeys(accountName, self._account_name, "xpath")
        time.sleep(2)
        an = self.getElement(self._account_name, "xpath")
        an.send_keys(Keys.ENTER)

    def clickService(self, service):
        if not service:
            return
        select = Select(self.getElement(self._service, "xpath"))
        time.sleep(1)
        select.select_by_index(service)

    def enterCustomerReference(self, customerReference):
        if customerReference:
            self.sendKeys(customerReference, self._customer_reference)

    def enterPickupCity(self, pickup_city):
        if pickup_city is "":
            return
        self.sendKeys(pickup_city, self._pickup_city, "xpath")
        time.sleep(3)
        pc = self.getElement(self._pickup_city, "xpath")
        pc.send_keys(Keys.ENTER)

    def enterDeliveryCity(self, delivery_city):
        if delivery_city is "":
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

    def clickConvertedConsignments(self, converted_cons):
        if converted_cons:
            self.elementClick(self._converted_consignments)

    def clickInactiveDrafts(self, status):
        if status:
            self.elementClick(self._inactive_drafts)

    def clearFilter(self):
        if self.getElement(self._clear_filter_btn).is_enabled():
            self.elementClick(self._clear_filter_btn)

    def findConsignment(self):
        self.elementClick(self._find_consignment_btn)

    def findConsignments(self, connote='', dateReadyFrom='', dateReadyTo='', accountName='', service='',
                         customerReference='', pickup_city='', delivery_city='', sender='',
                         receiver='', converted_cons='', status=''):
        self.waitForElement(self._clear_filter_btn)
        if self.getElement(self._clear_filter_btn).is_enabled():
            self.clearFilter()
        self.enterConnote(connote)
        self.enterDateReadyFrom(dateReadyFrom)
        self.enterDateReadyTo(dateReadyTo)
        self.enterAccountName(accountName)
        self.clickService(service)
        self.enterCustomerReference(customerReference)
        self.enterPickupCity(pickup_city)
        self.enterDeliveryCity(delivery_city)
        self.enterSender(sender)
        self.enterReceiver(receiver)
        self.clickConvertedConsignments(converted_cons)
        self.clickInactiveDrafts(status)
        self.findConsignment()

    def findPageTotal(self):
        self.waitForElement(self._page_total, "xpath")
        pgtot = self.getElement(self._page_total, "xpath")
        pgtottext = pgtot.text
        return int(pgtottext)

    def findPageTotalItems(self):
        return int(self.getElement(self._page_total_items).text)

    def findPageTotalWeight(self):
        self.waitForElement(self._page_total_weight, "xpath")
        res = self.getElement(self._page_total_weight, "xpath")
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
        if lastpagetext is not "":
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
        pgitems = self.calculateSumOfColumn(12)
        return pgitems

    def calcpagetotalweight(self):
        pgweight = self.calculateSumOfColumn(13)
        return pgweight

    def calcpagetotalvolume(self):
        pgvol = self.calculateSumOfColumn(14)
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