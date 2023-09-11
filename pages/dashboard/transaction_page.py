import re
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
import utilities.custom_logger as cl
import logging
import time
from base.basepage import BasePage


class TransactionPage(BasePage):
    log = cl.customLogger(logging.DEBUG)
    l_rws = None
    l_cols = None

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _connote_field = "//input[@id='wayne_id_consignment Note']"
    _date_ready_from = "//input[@id='wayne_id_date ready from']"
    _date_ready_to = "//input[@id='wayne_id_date ready to']"
    _account_name = "//input[@id = 'wayne_id_account name']"
    _date_pickup_from = "//input[@id='wayne_id_date pickup from']"
    _date_pickup_to = "//input[@id='wayne_id_date pickup to']"
    _customer_reference = "//input[@id='wayne_id_customer Ref']"
    _carrier = "//input[@id = 'wayne_id_Carrier']"
    _carrier_invoice = "//input[@id = 'wayne_id_Carrier Invoice']"
    _carrier_reference = "//input[@id = 'wayne_id_Carrier Ref.']"
    _manifest = "//input[@id='wayne_id_manifest']"
    _pickup_city = "//input[@id = 'wayne_id_Pickup city']"
    _delivery_city = "//input[@id = 'wayne_id_delivery City']"
    _sender = "//input[@id='wayne_id_sender']"
    _receiver = "//input[@id='wayne_id_receiver']"
    _status = "//input[@id='wayne_id_status']"
    _service = "//input[@id='wayne_id_service']"
    _receiver_reference = "//input[@id='wayne_id_receiver ref']"
    _booked_by = "//input[@id='wayne_id_booked By']"
    _no_charge = "//div[@id='wayne_id_no Charge']"
    _pricing_notes = "//div[@id='wayne_id_Pricing Notes']"
    _zero_sell_charge = "//div[@id='wayne_id_zero sell charge']"
    _zero_cost_rate = "//div[@id='wayne_id_zero cost rate']"
    _invoiced = "//div[@id='wayne_id_invoiced']"
    _checked_by = "//div[@id='wayne_id_checked']"
    _fms_matched = "//div[@id='wayne_id_fms Matched']"
    _inactive_transactions = "wayne_id_INACTIVE Transactions "

    _find_consignment_btn = "wayne_id_Find, "
    _clear_filter_btn = "wayne_id_Clear, "

    # footers
    _page_size = "//div[@id='wayne_id_Page Size']"
    _page_total = "//p[@id = 'wayne_id_PAGE TOTAL']"
    _page_total_items = "wayne_id_PAGE TOTAL ITEMS"
    _page_total_weight = "//p[@id= 'wayne_id_PAGE TOTAL WEIGHT']"
    _page_total_volume = "wayne_id_PAGE TOTAL VOLUME"
    _total_consignments = "wayne_id_TOTAL CONSIGNMENT"
    _total_consignment_items = "wayne_id_TOTAL CONSIGNMENT ITEMS"
    _total_consignment_weight = "wayne_id_TOTAL CONSIGNMENT WEIGHT"
    _total_consignment_volume = "wayne_id_TOTAL CONSIGNMENT VOLUME"

    _goto_last_page_btn = "//table[1]/tfoot[1]/tr[1]/div[1]/nav[1]/ul[1]/li[last()]"
    _last_page = "//table[1]/tfoot[1]/tr[1]/div[1]/nav[1]/ul[1]/li[last()-2]"
    # _page_before_last_page = "//table[1]/tfoot[1]/tr[1]/div[1]/nav[1]/ul[1]/li[last()-3]"

    ''' Fields '''

    def enterConnote(self, connote):
        if connote:
            self.sendKeys(connote, self._connote_field, "xpath")

    def enterDateReadyFrom(self, dateReadyFrom):
        if dateReadyFrom:
            self.sendKeys(dateReadyFrom, self._date_ready_from, "xpath")

    def enterDateReadyTo(self, dateReadyTo):
        if dateReadyTo:
            self.sendKeys(dateReadyTo, self._date_ready_to, "xpath")

    def enterDatePickupFrom(self, datePickupFrom):
        if datePickupFrom:
            self.sendKeys(datePickupFrom, self._date_pickup_from, "xpath")

    def enterDatePickupTo(self, datePickupTo):
        if datePickupTo:
            self.sendKeys(datePickupTo, self._date_pickup_to, "xpath")

    def enterAccountName(self, accountName):
        if accountName is "":
            return
        an = self.getElement(self._account_name, "xpath")
        self.sendKeys(accountName, self._account_name, "xpath")
        time.sleep(2)
        an.send_keys(Keys.ARROW_DOWN)
        an.send_keys(Keys.ARROW_DOWN)
        an.send_keys(Keys.ENTER)

    def enterCustomerReference(self, customerReference):
        if customerReference:
            self.sendKeys(customerReference, self._customer_reference, "xpath")

    def enterCarrier(self, carrier):
        if carrier is "":
            return
        ca = self.getElement(self._carrier, "xpath")
        self.sendKeys(carrier, self._carrier, "xpath")
        time.sleep(2)
        ca.send_keys(Keys.ARROW_DOWN)
        ca.send_keys(Keys.ARROW_DOWN)
        ca.send_keys(Keys.ENTER)

    def enterCarrierInvoice(self, carrierInvoices):
        if carrierInvoices:
            self.sendKeys(carrierInvoices, self._carrier_invoice, "xpath")

    def enterCarrierReference(self, carrierReference):
        if carrierReference:
            self.sendKeys(carrierReference, self._carrier_reference, "xpath")

    def enterManifest(self, manifest):
        if manifest is not "":
            self.sendKeys(manifest, self._manifest, "xpath")

    def enterPickupCity(self, pickup_city):
        if pickup_city is "":
            return
        pc = self.getElement(self._pickup_city, "xpath")
        self.sendKeys(pickup_city, self._pickup_city, "xpath")
        time.sleep(2)
        pc.send_keys(Keys.ARROW_DOWN)
        pc.send_keys(Keys.ARROW_DOWN)
        pc.send_keys(Keys.ENTER)

    def enterDeliveryCity(self, delivery_city):
        if delivery_city is "":
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

    def clickStatus(self, option):
        if not option:
            return
        select = self.getElement(self._status, "xpath")
        self.sendKeys(option, self._status, "xpath")
        time.sleep(2)
        if option == "ALLOCATED":
            select.send_keys(Keys.ARROW_DOWN)
            select.send_keys(Keys.ENTER)
            return
        select.send_keys(Keys.ARROW_DOWN)
        select.send_keys(Keys.ARROW_DOWN)
        select.send_keys(Keys.ENTER)

    def clickService(self, service):
        if not service:
            return
        select = self.getElement(self._service, "xpath")
        self.sendKeys(service, self._service, "xpath")
        time.sleep(2)
        if service == "ECONOMY":
            select.send_keys(Keys.ARROW_DOWN)
            select.send_keys(Keys.ENTER)
            return
        select.send_keys(Keys.ARROW_DOWN)
        select.send_keys(Keys.ARROW_DOWN)
        select.send_keys(Keys.ENTER)

    def enterReceiverReference(self, receiver_reference):
        if receiver_reference:
            self.sendKeys(receiver_reference, self._receiver_reference, "xpath")

    def enterBookedBy(self, booked_by):

        if booked_by is not "":
            bb = self.getElement(self._booked_by, "xpath")
            self.sendKeys(booked_by, self._booked_by, "xpath")
            time.sleep(2)
            bb.send_keys(Keys.ARROW_DOWN)
            bb.send_keys(Keys.ARROW_DOWN)
            bb.send_keys(Keys.ENTER)

    def clickNoCharge(self, nocharge):

        if nocharge is not "":
            select = self.getElement(self._no_charge)
            self.waitForElement("//div/ul/li[contains(normalize-space(),'YES')]", "xpath")
            self.elementClick("//div/ul/li[contains(normalize-space(),'" + nocharge.upper() + "')]", "xpath")

    def clickPricingNotes(self, pricingNotes):
        if pricingNotes:
            pn = self.getElement(self._pricing_notes, "xpath")
            self.waitForElement("//div/ul/li[contains(normalize-space(),'YES')]", "xpath")
            self.elementClick("//div/ul/li[contains(normalize-space(),'" + pricingNotes.upper() + "')]", "xpath")

    def clickZeroSellCharge(self, zerosellcharge):

        if zerosellcharge is not "":
            select = self.getElement(self._zero_sell_charge, "xpath")
            self.waitForElement("//div/ul/li[contains(normalize-space(),'YES')]", "xpath")
            self.elementClick("//div/ul/li[contains(normalize-space(),'" + zerosellcharge.upper() + "')]", "xpath")

    def clickZeroCostRate(self, zerocostrate):

        if zerocostrate is not "":
            select = self.getElement(self._zero_cost_rate, "xpath")
            self.waitForElement("//div/ul/li[contains(normalize-space(),'YES')]", "xpath")
            self.elementClick("//div/ul/li[contains(normalize-space(),'" + zerocostrate.upper() + "')]", "xpath")

    def clickInvoiced(self, invoiced):

        if invoiced is not "":
            select = self.getElement(self._invoiced, "xpath")
            self.waitForElement("//div/ul/li[contains(normalize-space(),'YES')]", "xpath")
            self.elementClick("//div/ul/li[contains(normalize-space(),'"+invoiced.upper()+"')]", "xpath")

    def clickCheckedBy(self, checked_by):

        if checked_by is not "":
            select = self.getElement(self._checked_by, "xpath")
            self.waitForElement("//div/ul/li[contains(normalize-space(),'YES')]", "xpath")
            self.elementClick("//div/ul/li[contains(normalize-space(),'" + checked_by.upper() + "')]", "xpath")

    def clickFMSMatched(self, fmsMatched):

        if fmsMatched is not "":
            select = self.getElement(self._fms_matched, "xpath")
            self.waitForElement("//div/ul/li[contains(normalize-space(),'YES')]", "xpath")
            self.elementClick("//div/ul/li[contains(normalize-space(),'" + fmsMatched.upper() + "')]", "xpath")

    def clickInactiveTransactions(self, status):
        if status:
            self.elementClick(self._inactive_transactions)

    # calculations

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
        return int(self.getElement(self._total_consignments).text)

    def findTotalConsignmentItems(self):
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", self.getElement(self._total_consignment_items))
        return int(self.getElement(self._total_consignment_items).text)

    def findTotalConsignmentWeight(self):
        tconswieght = self.getElement(self._total_consignment_weight).text
        # self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   #self.getElement(self._total_consignment_weight))
        reg_tconswieght = re.findall(r'\d+', tconswieght)
        return float(reg_tconswieght[0])

    def findTotalConsignmentVolume(self):
        tconsvolume = self.getElement(self._total_consignment_volume).text
        # self.driver.execute_script("arguments[0].scrollIntoView(true);",
        #                            self.getElement(self._total_consignment_volume))
        reg_tconsvolume = re.findall(r'\d+', tconsvolume)
        return float(reg_tconsvolume[0])

    def find_consignments(self, connote='', dateReadyFrom='', dateReadyTo='', accountName='', customerReference='',
                          carrier='', carrierInvoices='', carrierReference='', manifest='', pickup_city='',
                          delivery_city='', sender='', receiver='', option='', service='', receiver_reference='',
                          booked_by='', nocharge='', zerosellcharge='', zerocostrate='', invoiced='', checked_by='',
                          fmsMatched='', status=''):
        # remove filters first
        self.waitForElement(self._clear_filter_btn)
        if self.getElement(self._clear_filter_btn).is_enabled():
            self.clearFilter()
        self.enterConnote(connote)
        self.enterDateReadyFrom(dateReadyFrom)
        self.enterDateReadyTo(dateReadyTo)
        self.enterAccountName(accountName)
        self.enterCustomerReference(customerReference)
        self.enterCarrier(carrier)
        self.enterCarrierInvoice(carrierInvoices)
        self.enterCarrierReference(carrierReference)
        self.enterManifest(manifest)
        self.enterPickupCity(pickup_city)
        self.enterDeliveryCity(delivery_city)
        self.enterSender(sender)
        self.enterReceiver(receiver)
        self.clickStatus(option)
        self.clickService(service)
        self.enterReceiverReference(receiver_reference)
        self.enterBookedBy(booked_by)
        self.clickNoCharge(nocharge)
        self.clickZeroSellCharge(zerosellcharge)
        self.clickZeroCostRate(zerocostrate)
        self.clickInvoiced(invoiced)
        self.clickCheckedBy(checked_by)
        self.clickFMSMatched(fmsMatched)
        self.clickInactiveTransactions(status)
        time.sleep(2)
        self.findConsignment()

    def findPageValues(self):
        self.findPageTotal()
        self.findPageTotalItems()
        self.findPageTotalWeight()
        self.findPageTotalVolume()
        self.findTotalConsignment()
        self.findTotalConsignmentItems()
        self.findTotalConsignmentWeight()
        self.findTotalConsignmentVolume()

    def clearFilter(self):
        if self.getElement(self._clear_filter_btn).is_enabled():
            self.elementClick(self._clear_filter_btn)

    def findConsignment(self):
        self.elementClick(self._find_consignment_btn)

    def verifyTransactionsTitle(self):

        return self.verifyPageTitle("Express Cargo Ltd. | Transactions")

    def getpagebeforelast(self):
        lastpagetext = self.getElement(self._last_page, "xpath").text
        pgbeforelast = int(lastpagetext) - 1
        print(pgbeforelast)
        return pgbeforelast

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
        self.waitForElement(locator="td:nth-of-type(16)", locatorType="css")
        sum = 0.0
        amounts = self.getElements(" td:nth-of-type(" + str(col_number) + ")", "css")
        for amount in amounts:
            # print(amount.text)
            sum = sum + round(float(amount.text), 2)
        sum = int(sum)
        return sum

    def calcpagetotalweight(self):
        pgweight = self.calculateSumOfColumn(16)
        return pgweight

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
            time.sleep(2)
            pgbl = self.getpagebeforelast()
            time.sleep(3)
            lpgtot = self.calclastpagetotalrows()
            totalconsignment = (pgsz * pgbl) + lpgtot
            print(pgsz, pgbl, lpgtot, totalconsignment)
            return totalconsignment
        totalconsignment = self.getNumberOfRows()
        return totalconsignment

    def infonotpresent(self):
        presence = self.isElementPresent("//td[normalize-space()='No records to display']", "xpath")
        return presence

    def totalConsVerification(self):
        expectedVal = self.calculatetotalconsignment()
        actualVal = self.findTotalConsignment()
        b_val = self.verifyValues(actualVal, expectedVal)
        return b_val

    def calcpagetotalvolume(self):
        pgvol = self.calculateSumOfColumn(17)
        return pgvol

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

    def calcpagetotalitems(self):
        pgitems = self.calculateSumOfColumn(14)
        return pgitems

    def pgtotlItemsVerification(self):
        expectedVal = self.calcpagetotalitems()
        actualVal = self.findPageTotalItems()
        verval = self.verifyValues(actualVal, expectedVal)
        return verval






