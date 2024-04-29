import re
import time
from typing import Set
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains

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

    _connote_field = "//input[@id='wayne_id_consignment note']"
    _date_ready_from = "//input[@id='wayne_id_date ready from']"
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

    _find_consignment_btn = "//div/button[@id='wayne_id_Find, ']"
    _clear_filter_btn = "//div/button[@id='wayne_id_Clear, ']"

    # footers
    #_page_size = "//div[@tabindex='0'][@id='wayne_id_Page Size']"
    _page_total = "//p[@id = 'wayne_id_Scrolled TOTAL']"
    _page_total_items = "wayne_id_Scrolled TOTAL ITEMS"
    _page_total_weight = "wayne_id_Scrolled TOTAL WEIGHT"
    _page_total_volume = "wayne_id_Scrolled TOTAL VOLUME"
    #_total_consignments = "//p[@id ='wayne_id_TOTAL CONSIGNMENT']"
    # _total_consignment_items = "wayne_id_TOTAL CONSIGNMENT ITEMS"
    # _total_consignment_weight = "wayne_id_TOTAL CONSIGNMENT WEIGHT"
    # _total_consignment_volume = "wayne_id_TOTAL CONSIGNMENT VOLUME"

    _goto_last_page_btn = "//table[1]/tfoot[1]/tr[1]/div[1]/nav[1]/ul[1]/li[last()]"
    _last_page = "//table[1]/tfoot[1]/tr[1]/div[1]/nav[1]/ul[1]/li[last()-2]"

    ''' Fields '''

    def verifyCurrentConsignmentTitle(self):
        return self.verifyPageTitle("Express Cargo Ltd. | Current Consignments")

    def enterConnote(self, connote):
        if connote:
            self.sendKeys(connote, self._connote_field, "xpath")

    def enterDateReadyFrom(self, dateReadyFrom):
        if dateReadyFrom:
            self.sendKeys(dateReadyFrom, self._date_ready_from, "xpath")

    def enterDateReadyTo(self, dateReadyTo):
        if dateReadyTo:
            self.sendKeys(dateReadyTo, self._date_ready_to, "xpath")

    def enterDatePickUpFrom(self, datePickUpFrom):
        if datePickUpFrom:
            self.sendKeys(datePickUpFrom, self._date_pickup_from, "xpath")

    def enterDatePickUpTo(self, datePickUpTo):
        if datePickUpTo:
            self.sendKeys(datePickUpTo, self._date_pickup_to, "xpath")

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
        if self.getElement(self._clear_filter_btn, "xpath").is_enabled():
            self.elementClick(self._clear_filter_btn, "xpath")

    def findConsignment(self):
        self.elementClick(self._find_consignment_btn, "xpath")

    # calculations
    def find_consignment(self, connote='', dateReadyFrom='', dateReadyTo='', datePickUpFrom= '', datePickUpTo= '', accountName='', option='', service='',
                          customerReference='', booked_by='', pickup_city='', delivery_city='', estimated_delivery='',
                          sender='', receiver='', container_number='', carrier='', status='', priority_level='', assigned_to=''):
        # remove filters first
        self.waitForElement(self._clear_filter_btn, "xpath")
        if self.getElement(self._clear_filter_btn, "xpath").is_enabled():
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
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

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
        self.waitForElement(self._page_total_weight)
        res = self.getElement(self._page_total_weight)
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

    # def findTotalConsignment(self):
    #     self.waitForElement(self._goto_last_page_btn, "xpath")
    #     # self.driver.execute_script("arguments[0].scrollIntoView(true);", self.getElement(self._total_consignments))
    #     return int(self.getElement(self._total_consignments, "xpath").text)

    def findPageValues(self):
        self.findPageTotal()
        self.findPageTotalItems()
        self.findPageTotalWeight()
        self.findPageTotalVolume()
        #self.findTotalConsignment()

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
        #                            self.getElement(self._find_quote_btn))
        rws = self.getElements("//table/tbody/tr", "xpath")
        return len(rws)

    def getNumberOfColumns(self):
        self.waitForElement(self._find_consignment_btn)
        cols = self.getElements("//table/thead//th", "xpath")
        self.l_cols = len(cols)
        return self.l_cols

    def calculateSumOfColumn(self, col_number):
        self.waitForElement(locator="tr:nth-of-type(1)", locatorType="css") # div[title='WEIGHT']
        sum = 0.0
        amounts: [float] = []
        # amounts = self.getElements(" td:nth-of-type(" + str(col_number) + ")", "css")
        first_row = self.getElement(
            "//div[@id='root']/div/main/div[3]/div[2]/div/table/tbody/tr/td[" + str(col_number) + "]",
            "xpath")
        # //div[@id='root']/div/main/div[3]/div[2]/div/table/tbody/tr/td[14]
        first_row_val = float(first_row.text)
        self.log.info(first_row_val)
        amounts.append(first_row_val)
        for i in range(2, 16):
            ele = self.getElement("//div[@id='root']/div/main/div[3]/div[2]/div/table/tbody/tr["+str(i)+"]/td["+str(col_number)+"]", "xpath")
            el_value = float(ele.text)
            self.log.info(el_value)
            amounts.append(el_value)
        #print(col_number, str(col_number), "div[title='"+str(col_number)+"']")
        # amounts = self.getElements(" //div[@id='root']/div/main/div[3]/div[2]/div/table/thead/tr/th["+str(col_number)+"]/div/div/div", "xpath")
        print(amounts)
        for amount in amounts:
            # print(amount.text)
            # sum = sum + round(float(amount.text), 2)
            sum = sum + round(amount, 2)
        sum = int(sum)
        return sum

    def calcpagetotalweight(self):
        pgweight = self.calculateSumOfColumn(15)
        return pgweight

    def calcpagetotalvolume(self):
        pgvol = self.calculateSumOfColumn(16)
        return pgvol

    # Page Size element is not accessible
    # def calcpagesize(self):
    #     select = self.getElement(self._page_size)
    #     # element = select.first_selected_option
    #     page_size = int(select.value)
    #     return page_size

    # def calclastpagetotalrows(self):
    #     # self.driver.execute_script("arguments[0].scrollIntoView(true);",
    #     #                            self.getElement(self._goto_last_page_btn))
    #     self.elementClick(self._goto_last_page_btn, "xpath")
    #     self.waitForElement(self._page_total_items)
    #     rws = self.getElements("//table/tbody/tr", "xpath")
    #     return len(rws)

    # def calculatetotalconsignment(self):
    #     self.waitForElement(self._quote_field)
    #     # self.driver.execute_script("arguments[0].scrollIntoView(true);",
    #     #                            self.getElement(self._goto_last_page_btn, "xpath"))
    #     lpb = self.getElement(self._goto_last_page_btn, "xpath")
    #     if lpb.is_enabled():
    #         pgsz = self.calcpagesize()
    #         time.sleep(2)
    #         pgbl = self.getpagebeforelast()
    #         time.sleep(3)
    #         lpgtot = self.calclastpagetotalrows()
    #         totalconsignment = (pgsz * pgbl) + lpgtot
    #         print(pgsz, pgbl, lpgtot, totalconsignment)
    #         return totalconsignment
    #     totalconsignment = self.getNumberOfRows()
    #     return totalconsignment

    # def totalConsVerification(self):
    #     expectedVal = self.calculatetotalconsignment()
    #     actualVal = self.findTotalConsignment()
    #     b_val = self.verifyValues(actualVal, expectedVal)
    #     return b_val

    def pgtotWeightVerification(self):
        actualVal= self.calcpagetotalweight()
        expectedVal = self.findPageTotalWeight()
        print(expectedVal, actualVal)
        verval = self.verifyValues(actualVal, expectedVal)
        return verval

    def pgtotVolumeVerification(self):
        actualVal = self.calcpagetotalvolume()
        expectedVal= self.findPageTotalVolume()
        print(expectedVal, actualVal)
        verval = self.verifyValues(actualVal, expectedVal)
        return verval

    def calcpagetotalitems(self):
        pgitems = self.calculateSumOfColumn(14)
        return pgitems

    def pgtotlItemsVerification(self):
        actualVal = self.calcpagetotalitems()
        expectedVal = self.findPageTotalItems()
        print(expectedVal, actualVal)
        verval = self.verifyValues(actualVal, expectedVal)
        return verval

    def storedConsignments(self):
        #store the consignments in an array and return the array. This fn is called by checkDuplicates fn
        connote_Array = []
        self.waitForElement("(.//*[normalize-space(text()) and normalize-space(.)='Filters'])[1]/following::*[name()='svg'][1]", "xpath")
        self.elementClick("(.//*[normalize-space(text()) and normalize-space(.)='Filters'])[1]/following::*[name()='svg'][1]", "xpath")
        #window scrolling first
        self.waitForElement("/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[2]/div[2]/div[1]", "xpath")
        table_body = self.getElement("/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[2]/div[2]/div[1]", "xpath")
        print(table_body)
        self.driver.execute_script("window.scroll(0, 300)")
        actions = ActionChains(self.driver)
        actions.move_to_element(table_body).click_and_hold().move_by_offset(0, 100).release().perform()
        time.sleep(5)
        verical_ordinate = 100
        for i in range(0, 28):
            self.waitForElement("//tr[@data-index='"+str(i)+"']/td[@data-index='2']/span", "xpath")
            ele = self.getElement("//tr[@data-index='"+str(i)+"']/td[@data-index='2']/span", "xpath")
            ele_val = ele.text.strip()
            print(ele_val)
            connote_Array.append(ele_val)
        time.sleep(10)
        self.waitForElement("//tr[@data-index='35']/td[@data-index='2']/span", "xpath")
        for i in range(29, 39):
            self.waitForElement("//tr[@data-index='"+str(i)+"']/td[@data-index='2']/span", "xpath")
            ele = self.getElement("//tr[@data-index='"+str(i)+"']/td[@data-index='2']/span", "xpath")
            ele_val = ele.text.strip()
            print(ele_val)
            connote_Array.append(ele_val)

        self.driver.execute_script("arguments[0].scrollTop = arguments[1]", table_body, verical_ordinate)
        # # 30th one. wait for x sec
        # time.sleep(20)
        # self.waitForElement("//tr[@data-index='38']/td[@data-index='2']/span", "xpath")
        # ele = self.getElement("//tr[@data-index='38']/td[@data-index='2']/span", "xpath")
        # ele_val = ele.text.strip()
        # print(ele_val)
        # connote_Array.append(ele_val)
        # print(connote_Array)
        # dd = self.driver.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", table_body)
        # print(dd)
        return connote_Array

    def checkDuplicates(self):
        #array of 30 consignments
        duplicateFound = False
        connotes = self.storedConsignments()
        cons_set: Set[str] = set()
        for i in connotes:
            if i in cons_set:
                self.log.warning(f'Duplicate string detected: {i}')
                duplicateFound = True
            else:
                cons_set.add(i)
        return duplicateFound

    def scrollTableHorizontally(self):
        hScrollTable = self.getElement("//div[@id='root']/div/main/div[3]/div[2]/div/table", "xpath")
        self.driver.execute_script("arguments[0].scrollLeft = 700;", hScrollTable)


