import time

from pages.dashboard.dashboardtab import DashboardPage
from pages.home.home_page import HomePage
from pages.home.login_page import LoginPage
from pages.sales.quoteform_page import QuoteForm
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.use_fixtures("oneTimeSetup", "setUp")
# @ddt
class NewQuoteFHTests(unittest.TestCase):
    _headertest = []

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.db = DashboardPage(self.driver)
        self.qf = QuoteForm(self.driver)

    @pytest.mark.order(1)
    def test_validPage(self):
        self.lp = LoginPage(self.driver)
        self.lp.login("sabbir.sristy@w4solutions.com.au", "Iamsristy@36")
        self.qf = self.hp.gotoQuoteForm()
        nc_res = self.qf.verifyNewQuoteTitle()
        self.ts.markFinal("Quote Form load Check", nc_res, "Quote Form Loaded")

    @pytest.mark.order(2)
    def test_header(self):

        self.qf.enterHeaderInformation(accountName='BELGOTEX NZ LTD', customerRef='1231231231',
                                       receiverRef='assdasd123123')
        self._headertest.append(self.qf.checkSenderAddressClickable())
        self._headertest.append(self.qf.checkDateReady())

        print(self._headertest)
        # print(data_fetched_test)
        if False not in self._headertest:
            self.ts.markFinal("Header Test", True, "Data Fetched Without Issues")
        else:
            self.ts.markFinal("Header Test", False, "Data Could not be fetched")

    @pytest.mark.order(3)
    def test_checkSenderDetails(self):

        _sd_val = False
        self.qf.enterSenderDetails(senderCompanyName='BELGOTEX NZ LTD')
        # data_fetched_test = self.qf.checkDataFetchedPopUp()
        # print(data_fetched_test)
        # if data_fetched_test:
        #     self.ts.mark(True, "Data Fetched Without Issues")
        # else:
        #     self.ts.mark(False, "Data Could not be fetched")
        # time.sleep(5)
        print(self.qf.checkSenderAddressType())
        if self.qf.checkSenderAddressType():
            self.ts.mark(True, "Sender Address Type has field value")
            _sd_val = True
        else:
            self.ts.mark(False, "Sender Address Type IS EMPTY!!!!")
            _sd_val = False
        #
        print(self.qf.checkSenderRoad())
        if self.qf.checkSenderRoad():
            self.ts.mark(True, "Sender Road has field value")
            _sd_val = True
        else:
            self.ts.mark(False, "Sender Road IS EMPTY!!!!")
            _sd_val = False

        print(self.qf.checkSenderStreet())
        if self.qf.checkSenderStreet():
            self.ts.mark(True, "Sender Street has field value")
            _sd_val = True

        else:
            self.ts.mark(False, "Sender Street IS EMPTY!!!")
            _sd_val = False

        print(self.qf.checkSenderCity())
        if self.qf.checkSenderCity():
            self.ts.mark(True, "Sender City has field value")
            _sd_val = True

        else:
            self.ts.mark(False, "Sender City IS EMPTY!!!")
            _sd_val = False

        print(self.qf.checkSenderState())
        if self.qf.checkSenderState():
            self.ts.mark(True, "Sender State has field value")
            _sd_val = True

        else:
            self.ts.mark(True, "Sender State IS EMPTY!!!")
            _sd_val = False

        print(self.qf.checkSenderPostCode())
        if self.qf.checkSenderPostCode():
            self.ts.mark(True, "Sender Post Code has field value")
            _sd_val = True

        else:
            self.ts.mark(True, "Sender Post Code IS EMPTY!!!")
            _sd_val = False

        self.ts.markFinal("TEST -> (Required Fields) Receiver Details DATA FETCHING", _sd_val, "All tests working")

    # @pytest.mark.order(4)
    # def test_checkReceiverDetails(self):
    #     _rd_val = False
    #     # noinspection SpellCheckingInspection
    #     self.qf.enterReceiverDetails(receiverCompanyName="CARPET COURT MT ROSKILL")
    #     time.sleep(3)
    #     print(self.qf.checkReceiverAddressType())
    #     if self.qf.checkReceiverAddressType():
    #         self.ts.mark(True, "Receiver Address Type has field value")
    #         _rd_val = True
    #     else:
    #         self.ts.mark(False, "Receiver Address Type IS EMPTY!!!!")
    #         _rd_val = False
    #     #
    #     print(self.qf.checkReceiverRoad())
    #     if self.qf.checkReceiverRoad():
    #         self.ts.mark(True, "Receiver Road has field value")
    #         _rd_val = True
    #     else:
    #         self.ts.mark(False, "Receiver Road IS EMPTY!!!!")
    #         _rd_val = False
    #
    #     print(self.qf.checkReceiverStreet())
    #     if self.qf.checkReceiverStreet():
    #         self.ts.mark(True, "Receiver Street has field value")
    #         _rd_val = True
    #     else:
    #         self.ts.mark(False, "Receiver Street IS EMPTY!!!")
    #         _rd_val = False
    #
    #     print(self.qf.checkReceiverCity())
    #     if self.qf.checkReceiverCity():
    #         self.ts.mark(True, "Receiver City has field value")
    #         _rd_val = True
    #     else:
    #         self.ts.mark(False, "Receiver City IS EMPTY!!!")
    #         _rd_val = False
    #
    #     print(self.qf.checkReceiverState())
    #     if self.qf.checkReceiverState():
    #         self.ts.mark(True, "Receiver State has field value")
    #         _rd_val = True
    #     else:
    #         self.ts.mark(True, "Receiver State IS EMPTY!!!")
    #         _rd_val = False
    #
    #     print(self.qf.checkReceiverPostCode())
    #     if self.qf.checkReceiverPostCode():
    #         self.ts.mark(True, "Receiver Post Code has field value")
    #         _rd_val = True
    #     else:
    #         self.ts.mark(True, "Receiver Post Code IS EMPTY!!!")
    #         _rd_val = False
    #
    #     self.ts.markFinal("TEST -> (Required Fields) Receiver Details DATA FETCHING", _rd_val, "All tests working")


    @pytest.mark.order(5)
    def test_editSenderDetails(self):

        res_values = self.qf.editSenderDetailsCompanyNameAndCheckRequiredFields(senderCompanyName='BELGOTEX CHRISTCHURCH')
        print(res_values)
        if res_values:
            self.ts.markFinal("Check Required Fields", res_values, "Required Fields are FILLED")
        else:
            self.ts.markFinal("Check Required Fields", res_values, "Required Fields are EMPTY!!!")

        # addrTy, Road, Street, City, State, PostCode
        # res_edit = self.qf.editSenderDetails(addressType="RESIDENTIAL BUSINESS", road='32', street='FOX STREET',
        #                                      city='INVERCARGILL', state='SOUTHLAND', postcode='9810')  #
        # if res_edit:
        #     self.ts.markFinal("Edited Existing Sender Details", res_edit, "Sender Details Edited Successfully")
        #
        # else:
        #     self.ts.markFinal("Edited Existing Sender Details", res_edit, "Sender Details couldn't be Edited!!!")


    @pytest.mark.order(6)
    def test_editReceiverDetails(self):
        res_values = self.qf.editReceiverDetailsCompanyName(receiverCompanyName="THE FLOORING ROOM CENTRE CHRISTCHURCH")
        print(res_values)
        if res_values:
            self.ts.markFinal("Check Required Fields", res_values, "Required Fields are FILLED")
        else:
            self.ts.markFinal("Check Required Fields", res_values, "Required Fields are EMPTY!!!")

        # res_edit = self.qf.editReceiverDetails(addressType="RESIDENTIAL BUSINESS", road='11', street='NICCOL AVENUE', city='CHRISTCHURCH', state='OTAGO', postcode='9510')  #
        #
        # if res_edit:
        #     self.ts.markFinal("Edited Existing Receiver Details", res_edit, "Receiver Details Edited Successfully")
        #
        # else:
        #     self.ts.markFinal("Edited Existing Receiver Details", res_edit, "Receiver Details couldn't be Edited!!!")
        # time.sleep(4)

    #
    #
