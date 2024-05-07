import time

from pages.dashboard.dashboardtab import DashboardPage
from pages.home.home_page import HomePage
from pages.home.login_page import LoginPage
from pages.sales.quoteform_page import QuoteForm
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.use_fixtures("oneTimeSetup", "setUp") #, "setUp"
# @ddt
class NewQuoteFHTests(unittest.TestCase):
    _headertest: list = []

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.db = DashboardPage(self.driver)
        self.qf = QuoteForm(self.driver)

    @pytest.mark.order(1)
    def test_firsthalf(self):
        self.lp = LoginPage(self.driver)
        self.lp.login("sabbir.sristy@w4solutions.com.au", "Iamsristy@36")
        self.qf = self.hp.gotoQuoteForm()
        nc_res = self.qf.verifyNewQuoteTitle()
        self.ts.markFinal("Quote Form load Check", nc_res, "Quote Form Loaded")


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

        _rd_val = False
        # noinspection SpellCheckingInspection
        self.qf.enterReceiverDetails(receiverCompanyName="CARPET COURT MT ROSKILL")
        time.sleep(3)
        print(self.qf.checkReceiverAddressType())
        if self.qf.checkReceiverAddressType():
            self.ts.mark(True, "Receiver Address Type has field value")
            _rd_val = True
        else:
            self.ts.mark(False, "Receiver Address Type IS EMPTY!!!!")
            _rd_val = False
        #
        print(self.qf.checkReceiverRoad())
        if self.qf.checkReceiverRoad():
            self.ts.mark(True, "Receiver Road has field value")
            _rd_val = True
        else:
            self.ts.mark(False, "Receiver Road IS EMPTY!!!!")
            _rd_val = False

        print(self.qf.checkReceiverStreet())
        if self.qf.checkReceiverStreet():
            self.ts.mark(True, "Receiver Street has field value")
            _rd_val = True
        else:
            self.ts.mark(False, "Receiver Street IS EMPTY!!!")
            _rd_val = False

        print(self.qf.checkReceiverCity())
        if self.qf.checkReceiverCity():
            self.ts.mark(True, "Receiver City has field value")
            _rd_val = True
        else:
            self.ts.mark(False, "Receiver City IS EMPTY!!!")
            _rd_val = False

        print(self.qf.checkReceiverState())
        if self.qf.checkReceiverState():
            self.ts.mark(True, "Receiver State has field value")
            _rd_val = True
        else:
            self.ts.mark(True, "Receiver State IS EMPTY!!!")
            _rd_val = False

        print(self.qf.checkReceiverPostCode())
        if self.qf.checkReceiverPostCode():
            self.ts.mark(True, "Receiver Post Code has field value")
            _rd_val = True
        else:
            self.ts.mark(True, "Receiver Post Code IS EMPTY!!!")
            _rd_val = False

        self.ts.markFinal("TEST -> (Required Fields) Receiver Details DATA FETCHING", _rd_val, "All tests working")

        res_values = self.qf.editSenderDetailsCompanyNameAndCheckRequiredFields(
            senderCompanyName='BELGOTEX CHRISTCHURCH')
        print(res_values)
        if res_values:
            self.ts.markFinal("Check Required Fields", res_values, "Required Fields are FILLED")
        else:
            self.ts.markFinal("Check Required Fields", res_values, "Required Fields are EMPTY!!!")

        res_values = self.qf.editReceiverDetailsCompanyName(receiverCompanyName="THE FLOORING ROOM CENTRE CHRISTCHURCH")
        print(res_values)
        if res_values:
            self.ts.markFinal("Check Required Fields", res_values, "Required Fields are FILLED")
        else:
            self.ts.markFinal("Check Required Fields", res_values, "Required Fields are EMPTY!!!")


