import re
import time

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from pages.customer_service.consignmentform_new23 import ConsignmentForm


class CurrentConsignmentPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    # //button[@title='Create New Consignment']/span[@class ='MuiIconButton-label']
    _new_consignment_btn = "//button[@title='Create New Consignment']/span[@class ='MuiIconButton-label']"

    _connote_field = "wayne_id_consignment Note"
    _date_ready_from = "wayne_id_date ready from"
    _date_ready_to = "wayne_id_date ready to"
    _date_pickup_from = "wayne_id_date pickup from"
    _date_pickup_to = "wayne_id_date pickup to"
    _account_name = "//input[@id = 'wayne_id_account name']"
    _status = "//input[@id='wayne_id_status']"
    _service = "//input[@id='wayne_id_service']"
    _customer_reference = "wayne_id_customer Ref"
    _booked_by = "wayne_id_booked by"
    _pickup_city = "//input[@id = 'wayne_id_pickup City']"
    _delivery_city = "//input[@id = 'wayne_id_delivery City']"
    _sender = "wayne_id_sender"
    _receiver = "wayne_id_receiver"
    _container_number="wayne_id_Container Number"
    _priority_level = "wayne_id_priority level"
    _assigned_to = "wayne_id_assigned to"
    _carrier = "wayne_id_carrier"
    _estimated_delivery = "wayne_id_estimated Delivery"
    _inactive_transactions = "wayne_id_INACTIVE Consignments "

    _find_consignment_btn = "wayne_id_Find, "
    _clear_filter_btn = "wayne_id_Clear, "

    # footers
    _page_size = "//div[@tabindex='0'][@id='wayne_id_Page Size']"
    _page_total = "//p[@id = 'wayne_id_PAGE TOTAL']"
    _page_total_items = "wayne_id_PAGE TOTAL ITEMS"
    _page_total_weight = "//p[@id= 'wayne_id_PAGE TOTAL WEIGHT']"
    _page_total_volume = "wayne_id_PAGE TOTAL VOLUME"
    _total_consignments = "//p[@id ='wayne_id_TOTAL CONSIGNMENT']"
    _total_consignment_items = "wayne_id_TOTAL CONSIGNMENT ITEMS"
    _total_consignment_weight = "wayne_id_TOTAL CONSIGNMENT WEIGHT"
    _total_consignment_volume = "wayne_id_TOTAL CONSIGNMENT VOLUME"

    _goto_last_page_btn = "//table[1]/tfoot[1]/tr[1]/div[1]/nav[1]/ul[1]/li[last()]"
    _last_page = "//table[1]/tfoot[1]/tr[1]/div[1]/nav[1]/ul[1]/li[last()-2]"

    ''' Fields '''

    def verifyCurrentConsignmentTitle(self):
        return self.verifyPageTitle("Express Cargo Ltd. | Consignments")

    def enterConnote(self, connote):
        if connote:
            self.sendKeys(connote, self._connote_field)

    def enterDateReadyFrom(self, dateReadyFrom):
        if dateReadyFrom:
            self.sendKeys(dateReadyFrom, self._date_ready_from)

    def enterDateReadyTo(self, dateReadyTo):
        if dateReadyTo:
            self.sendKeys(dateReadyTo, self._date_ready_to)

    def enterDatePickUpFrom(self, datePickUpFrom):
        if datePickUpFrom:
            self.sendKeys(datePickUpFrom, self._date_pickup_from)

    def enterDatePickUpTo(self, datePickUpTo):
        if datePickUpTo:
            self.sendKeys(datePickUpTo, self._date_pickup_to)

    def enterAccountName(self, accountName):
        if accountName == "":
            return
        an = self.getElement(self._account_name, "xpath")
        self.sendKeys(accountName, self._account_name, "xpath")
        time.sleep(2)
        an.send_keys(Keys.ARROW_DOWN)
        an.send_keys(Keys.ARROW_DOWN)
        an.send_keys(Keys.ENTER)

    def clickStatus(self, option):
        if not option:
            return
        sel = self.getElement(self._status, "xpath")
        self.sendKeys(option, self._status, "xpath")
        time.sleep(2)
        if option == "ALLOCATED":
            sel.send_keys(Keys.ARROW_DOWN)
            sel.send_keys(Keys.ENTER)
            return
        sel.send_keys(Keys.ARROW_DOWN)
        sel.send_keys(Keys.ARROW_DOWN)
        sel.send_keys(Keys.ENTER)

    def clickService(self, service):
        if not service:
            return
        sel = self.getElement(self._service, "xpath")
        self.sendKeys(service, self._service, "xpath")
        time.sleep(2)
        sel.send_keys(Keys.ARROW_DOWN)
        sel.send_keys(Keys.ARROW_DOWN)
        sel.send_keys(Keys.ENTER)

    def enterCustomerReference(self, customerReference):
        if customerReference:
            self.sendKeys(customerReference, self._customer_reference)

    def enterBookedBy(self, booked_by):
        if booked_by != "":
            bb = self.getElement(self._booked_by)
            self.sendKeys(booked_by, self._booked_by)
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
            self.sendKeys(sender, self._sender)

    def enterReceiver(self, receiver):
        if receiver:
            self.sendKeys(receiver, self._receiver)

    def enterContainerNumber(self, container_number):
        if container_number:
            self.sendKeys(container_number, self._container_number)

    def enterCarrier(self, carrier):
        if carrier == "":
            return
        ca = self.getElement(self._carrier)
        self.sendKeys(carrier, self._carrier)
        time.sleep(2)
        ca.send_keys(Keys.ARROW_DOWN)
        ca.send_keys(Keys.ARROW_DOWN)
        ca.send_keys(Keys.ENTER)

    def enterAssignedTo(self, assigned_to):
        if assigned_to == "":
            return
        ca = self.getElement(self._assigned_to)
        self.sendKeys(assigned_to, self._assigned_to)
        time.sleep(2)
        ca.send_keys(Keys.ARROW_DOWN)
        ca.send_keys(Keys.ARROW_DOWN)
        ca.send_keys(Keys.ENTER)

    def enterEstimatedDelivery(self, estimated_delivery):
        if estimated_delivery == "":
            return
        self.sendKeys(estimated_delivery, self._estimated_delivery)
        time.sleep(3)
        ca = self.getElement(self._estimated_delivery)
        ca.send_keys(Keys.ENTER)

    def clickInactiveTransactions(self, status):
        if status:
            self.elementClick(self._inactive_transactions)

    def enterPriorityLevel(self, priority_level):
        if priority_level == "":
            return
        self.sendKeys(priority_level, self._priority_level)
        time.sleep(3)
        dc = self.getElement(self._priority_level)
        dc.send_keys(Keys.ENTER)

    def clearFilter(self):
        if self.getElement(self._clear_filter_btn).is_enabled():
            self.elementClick(self._clear_filter_btn)

    def findConsignment(self):
        self.elementClick(self._find_consignment_btn)

    # calculations
    def find_consignment(self, connote='', dateReadyFrom='', dateReadyTo='', datePickUpFrom= '', datePickUpTo= '', accountName='', option='', service='',
                          customerReference='', booked_by='', pickup_city='', delivery_city='', estimated_delivery='',
                          sender='', receiver='', container_number='', carrier='', status='', priority_level='', assigned_to=''):
        # remove filters first
        self.waitForElement(self._clear_filter_btn)
        if self.getElement(self._clear_filter_btn).is_enabled():
            self.clearFilter()
        self.enterConnote(connote)
        self.enterDateReadyFrom(dateReadyFrom)
        self.enterDateReadyTo(dateReadyTo)
        self.enterDatePickUpFrom(datePickUpFrom)
        self.enterDatePickUpTo(datePickUpTo)
        self.enterAccountName(accountName)
        self.enterCustomerReference(customerReference)
        self.enterCarrier(carrier)
        self.enterPickupCity(pickup_city)
        self.enterDeliveryCity(delivery_city)
        self.enterSender(sender)
        self.enterReceiver(receiver)
        self.enterContainerNumber(container_number)
        self.clickStatus(option)
        self.clickService(service)
        self.enterBookedBy(booked_by)
        self.enterAssignedTo(assigned_to)
        self.enterEstimatedDelivery(estimated_delivery)
        self.clickInactiveTransactions(status)
        self.enterPriorityLevel(priority_level)
        time.sleep(2)
        self.findConsignment()

    def findPageTotal(self):
        self.waitForElement(self._page_total, "xpath")
        pgtot = self.getElement(self._page_total, "xpath")
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", pgtot)
        pgtottext = pgtot.text
        return int(pgtottext)

    def findPageTotalItems(self):
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", self.getElement(self._page_total_items))
        return int(self.getElement(self._page_total_items).text)

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
        sum = int(sum)
        return sum

    def calcpagetotalweight(self):
        pgweight = self.calculateSumOfColumn(23)
        return pgweight

    def calcpagetotalvolume(self):
        pgvol = self.calculateSumOfColumn(24)
        return pgvol

    # Page Size element is not accessible
    def calcpagesize(self):
        select = self.getElement(self._page_size)
        # element = select.first_selected_option
        page_size = int(select.value)
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
            time.sleep(2)
            pgbl = self.getpagebeforelast()
            time.sleep(3)
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
        print(expectedVal, actualVal)
        verval = self.verifyValues(actualVal, expectedVal)
        return verval

    def pgtotVolumeVerification(self):
        expectedVal = self.calcpagetotalvolume()
        actualVal = self.findPageTotalVolume()
        print(expectedVal, actualVal)
        verval = self.verifyValues(actualVal, expectedVal)
        return verval

    def calcpagetotalitems(self):
        pgitems = self.calculateSumOfColumn(22)
        return pgitems

    def pgtotlItemsVerification(self):
        expectedVal = self.calcpagetotalitems()
        actualVal = self.findPageTotalItems()
        print(expectedVal, actualVal)
        verval = self.verifyValues(actualVal, expectedVal)
        return verval


