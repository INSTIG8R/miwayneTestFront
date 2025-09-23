import time

from pages.customer_service.consignmentform_new23 import ConsignmentForm
from pages.dashboard.dashboardtab import DashboardPage
from pages.home.home_page import HomePage
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.use_fixtures("oneTimeSetup", "setUp")
# @ddt
class NewConsignmentFHTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.db = DashboardPage(self.driver)
        self.nc = ConsignmentForm(self.driver)

    @pytest.mark.order(1)
    def test_validPage(self):
        self.lp = LoginPage(self.driver)
        self.lp.login("sabbir.sristy@w4solutions.com.au", "Iamsristy@36")
        self.db = self.hp.clickDashboard()
        self.nc = self.db.gotoConsignmentForm()
        nc_res = self.nc.verifyNewConsignmentTitle()
        self.ts.markFinal("New Consignment Page load Check", nc_res, "New Consignment Page Loaded")

    @pytest.mark.order(2)
    def test_header(self):
        self.nc.enterHeaderInformation(connote='DEMO0001001', accountName='BELGOTEX NZ LTD', status='DELIVERED', customerRef='1233AS', priorityLevel='STANDARD', assignedTo='DONE')
        addressinfotest = self.nc.checkSenderAddressClickable()
        # print(data_fetched_test)
        if addressinfotest:
            self.ts.markFinal("Address Fields are Open", True, "Data Fetched Without Issues")
        else:
            self.ts.markFinal("Address Fields are Closed", False, "Data Could not be fetched")

    @pytest.mark.order(3)
    def test_checkSenderDetails(self):
        _sd_val = False
        self.nc.enterSenderDetails(senderCompanyName='BELGOTEX NZ LTD')
        # data_fetched_test = self.nc.checkDataFetchedPopUp()
        # # print(data_fetched_test)
        # if data_fetched_test:
        #     self.ts.mark(True, "Data Fetched Without Issues")
        # else:
        #     self.ts.mark(False, "Data Could not be fetched")
        # time.sleep(2)
        print(self.nc.checkSenderAddressType())
        if self.nc.checkSenderAddressType():
            self.ts.mark(True, "Sender Address Type has field value")
            _sd_val = True
        else:
            self.ts.mark(False, "Sender Address Type IS EMPTY!!!!")
            _sd_val = False
        #
        print(self.nc.checkSenderRoad())
        if self.nc.checkSenderRoad():
            self.ts.mark(True, "Sender Road has field value")
            _sd_val = True
        else:
            self.ts.mark(False, "Sender Road IS EMPTY!!!!")
            _sd_val = False

        print(self.nc.checkSenderStreet())
        if self.nc.checkSenderStreet():
            self.ts.mark(True, "Sender Street has field value")
            _sd_val = True
        else:
            self.ts.mark(False, "Sender Street IS EMPTY!!!")
            _sd_val = False

        print(self.nc.checkSenderCity())
        if self.nc.checkSenderCity():
            self.ts.mark(True, "Sender City has field value")
            _sd_val = True
        else:
            self.ts.mark(False, "Sender City IS EMPTY!!!")
            _sd_val = False

        print(self.nc.checkSenderState())
        if self.nc.checkSenderState():
            self.ts.mark(True, "Sender State has field value")
            _sd_val = True
        else:
            self.ts.mark(True, "Sender State IS EMPTY!!!")
            _sd_val = False

        print(self.nc.checkSenderPostCode())
        if self.nc.checkSenderPostCode():
            self.ts.mark(True, "Sender Post Code has field value")
            _sd_val = True
        else:
            self.ts.mark(True, "Sender Post Code IS EMPTY!!!")
            _sd_val = False

        self.ts.markFinal("TEST -> (Required Fields) Sender Details DATA FETCHING", _sd_val, "All tests working")

    @pytest.mark.order(4)
    def test_checkReceiverDetails(self):
        _rd_val = False
        # noinspection SpellCheckingInspection
        self.nc.enterReceiverDetails(receiverCompanyName="BELGOTEX HA CRES")
        # time.sleep(5)
        print(self.nc.checkReceiverAddressType())
        if self.nc.checkReceiverAddressType():
            self.ts.mark(True, "Receiver Address Type has field value")
            _rd_val = True
        else:
            self.ts.mark(False, "Receiver Address Type IS EMPTY!!!!")
            _rd_val = False
        #
        print(self.nc.checkReceiverRoad())
        if self.nc.checkReceiverRoad():
            self.ts.mark(True, "Receiver Road has field value")
            _rd_val = True
        else:
            self.ts.mark(False, "Receiver Road IS EMPTY!!!!")
            _rd_val = False

        print(self.nc.checkReceiverStreet())
        if self.nc.checkReceiverStreet():
            self.ts.mark(True, "Receiver Street has field value")
            _rd_val = True
        else:
            self.ts.mark(False, "Receiver Street IS EMPTY!!!")
            _rd_val = False

        print(self.nc.checkReceiverCity())
        if self.nc.checkReceiverCity():
            self.ts.mark(True, "Receiver City has field value")
            _rd_val = True
        else:
            self.ts.mark(False, "Receiver City IS EMPTY!!!")
            _rd_val = False

        print(self.nc.checkReceiverState())
        if self.nc.checkReceiverState():
            self.ts.mark(True, "Receiver State has field value")
            _rd_val = True
        else:
            self.ts.mark(True, "Receiver State IS EMPTY!!!")
            _rd_val = False

        print(self.nc.checkReceiverPostCode())
        if self.nc.checkReceiverPostCode():
            self.ts.mark(True, "Receiver Post Code has field value")
            _rd_val = True
        else:
            self.ts.mark(True, "Receiver Post Code IS EMPTY!!!")
            _rd_val = False

        self.ts.markFinal("TEST -> (Required Fields) Receiver Details DATA FETCHING", _rd_val, "All tests working")


    @pytest.mark.order(5)
    def test_editSenderDetails(self):

        verified_acc = self.nc.verifiedaccount_l()
        if verified_acc:
            self.ts.markFinal("Verified Account", True, "Editing not needed")
        else:
            res_values = self.nc.editSenderDetailsCompanyNameAndCheckRequiredFields(senderCompanyName="BELGOTEX NZ LTD")
            print(res_values)
            if res_values:
                self.ts.mark(res_values, "Required Fields are FILLED")
            else:
                self.ts.mark(res_values, "Required Fields are EMPTY!!!")

        # addrTy, Road, Street, City, State, PostCode
            res_edit = self.nc.editSenderDetails( road='32', street='FOX STREET',
                                             city='INVERCARGILL', state='SOUTHLAND', postcode='9810')  #
            if res_edit:
                self.ts.markFinal("Edited Existing Sender Details", res_edit, "Sender Details Edited Successfully")

            else:
                self.ts.markFinal("Edited Existing Sender Details", res_edit, "Sender Details couldn't be Edited!!!")

        time.sleep(5)
    #
    @pytest.mark.order(6)
    def test_editReceiverDetails(self):
        verifiedacc = self.nc.verifiedaccount_r()
        if verifiedacc:
            self.ts.markFinal("Verified Account", True, "Editing not needed")
        else:
            res_values = self.nc.editReceiverDetailsCompanyName(receiverCompanyName="BELGOTEX HA CRES")

            if res_values:
                self.ts.mark(res_values, "Required Fields are FILLED")
            else:
                self.ts.mark(res_values, "Required Fields are EMPTY!!!")

            res_edit = self.nc.editReceiverDetails( road='11', street='NICCOL AVENUE', city='CHRISTCHURCH', state='OTAGO', postcode='9510')  #

            if res_edit:
                self.ts.markFinal("Edited Existing Receiver Details", res_edit, "Receiver Details Edited Successfully")

            else:
                self.ts.markFinal("Edited Existing Receiver Details", res_edit, "Receiver Details couldn't be Edited!!!")
    #     time.sleep(4)
    #
    #
    #
