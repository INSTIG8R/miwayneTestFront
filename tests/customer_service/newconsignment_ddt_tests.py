import time

from pages.customer_service.consignmentform_new23 import ConsignmentForm
from pages.customer_service.newconsignment_page import NewConsignmentPage
from pages.dashboard.dashboardtab import DashboardPage
from pages.home.home_page import HomePage
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest


from ddt import ddt, data, unpack
from utilities.read_data import getCSVData


@pytest.mark.use_fixtures("oneTimeSetup", "setUp")
@ddt
class NewConsignmentDDTTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.db = DashboardPage(self.driver)
        self.nc = ConsignmentForm(self.driver)

    @pytest.mark.order(1)
    def test_validPage(self):
        self.lp = LoginPage(self.driver)
        self.lp.login("fatin.khan@w4solutions.com.au", "devexpresscargo@fatiN97")
        self.db = self.hp.clickDashboard()
        self.nc = self.db.gotoConsignmentForm()
        nc_res = self.nc.verifyNewConsignmentTitle()
        self.ts.markFinal("New Consignment Page load Check", nc_res, "New Consignment Page Loaded")

    @pytest.mark.order(2)
    @data(*getCSVData("D:\\work\\workspace_python\\wayne_express_cargo\\data\\newconsignment_data.csv"))
    @unpack
    def test_ccsv(self, connote='', accountName='', status='', senderCompanyName='', receiverCompanyName='',
                  services1='', item1='', commodity1='', quantity1='', weight1='', volume1='',
                  item2='', commodity2='', quantity2='', weight2='', volume2='',
                  carrier1='', depot1='', frm1='', to1='', cost1='', cn1='',
                  carrier2='', depot2='', frm2='', to2='', cost2='', cn2='',
                  quotedPrice='', noCharge='', quotedBy='', pricingNotes='', cancelled=''):
        self.nc.enterHeaderInformation(connote=connote, accountName=accountName, status=status)
        ###
        data_fetched_test = self.nc.checkDataFetchedPopUp()
        if data_fetched_test:
            self.ts.mark(True, "Data Fetched Without Issues")
        else:
            self.ts.mark(False, "Data Could not be fetched")
        ###

        if self.nc.isElementPresent("//p[contains(normalize-space(), 'already exist')]", "xpath"):
            self.nc.editConsignmentNumber()
        self.nc.enterSenderDetails(senderCompanyName=senderCompanyName)

        # ###
        # if self.nc.checkSenderAddressType():
        #     self.ts.mark(True, "Sender Address Type has field value")
        # else:
        #     self.ts.mark(False, "Sender Address Type IS EMPTY!!!!")
        # if self.nc.checkSenderRoad():
        #     self.ts.mark(True, "Sender Road has field value")
        # else:
        #     self.ts.mark(False, "Sender Road IS EMPTY!!!!")
        # if self.nc.checkSenderStreet():
        #     self.ts.mark(True, "Sender Street has field value")
        # else:
        #     self.ts.mark(False, "Sender Street IS EMPTY!!!")
        # if self.nc.checkSenderCity():
        #     self.ts.mark(True, "Sender City has field value")
        # else:
        #     self.ts.mark(False, "Sender City IS EMPTY!!!")
        # if self.nc.checkSenderState():
        #     self.ts.mark(True, "Sender State has field value")
        # else:
        #     self.ts.mark(True, "Sender State IS EMPTY!!!")
        # if self.nc.checkSenderPostCode():
        #     self.ts.mark(True, "Sender Post Code has field value")
        # else:
        #     self.ts.mark(True, "Sender Post Code IS EMPTY!!!")
        # ###

        self.nc.enterReceiverDetails(receiverCompanyName=receiverCompanyName)
        #
        # ###
        # if self.nc.checkReceiverAddressType():
        #     self.ts.mark(True, "Receiver Address Type has field value")
        # else:
        #     self.ts.mark(False, "Receiver Address Type IS EMPTY!!!!")
        # if self.nc.checkReceiverRoad():
        #     self.ts.mark(True, "Receiver Road has field value")
        # else:
        #     self.ts.mark(False, "Receiver Road IS EMPTY!!!!")
        # if self.nc.checkReceiverStreet():
        #     self.ts.mark(True, "Receiver Street has field value")
        # else:
        #     self.ts.mark(False, "Receiver Street IS EMPTY!!!")
        # if self.nc.checkReceiverCity():
        #     self.ts.mark(True, "Receiver City has field value")
        # else:
        #     self.ts.mark(False, "Receiver City IS EMPTY!!!")
        # if self.nc.checkReceiverState():
        #     self.ts.mark(True, "Receiver State has field value")
        # else:
        #     self.ts.mark(True, "Receiver State IS EMPTY!!!")
        # if self.nc.checkReceiverPostCode():
        #     self.ts.mark(True, "Receiver Post Code has field value")
        # else:
        #     self.ts.mark(True, "Receiver Post Code IS EMPTY!!!")
        #
        # ###
        # time.sleep(2)
        self.nc.enterConsignmentLine_1(services1=services1, item1=item1, commodity1=commodity1, quantity1=quantity1, weight1=weight1, volume1=volume1)
        self.nc.enterConsignmentLine_2(item2=item2, commodity2=commodity2, quantity2=quantity2, weight2=weight2, volume2=volume2)
        self.nc.enterLegging_1(carrier1=carrier1, depot1=depot1, frm1=frm1, to1=to1, cost1=cost1, cn1=cn1)
        self.nc.enterLegging_2(carrier2=carrier2, depot2=depot2, frm2=frm2, to2=to2, cost2=cost2, cn2=cn2)
        self.nc.enterSellRateFields(quotedPrice=quotedPrice, noCharge=noCharge, quotedBy=quotedBy, pricingNotes=pricingNotes, cancelled=cancelled)
        self.nc.enterSellRating()
        if self.nc.isElementPresent("//p[contains(normalize-space(), 'already exist')]", "xpath"):
            self.nc.editConsignmentNumber()
        cr_con = self.nc.clickCreateConsignment()
        print(cr_con)
        # goes to Dashboard when form created, Need to route back to form (?)
        self.nc = self.db.gotoConsignmentForm()
        nct = self.nc.verifyNewConsignmentTitle()
        print(nct)

        if cr_con:
            self.ts.markFinal("New CONSIGNMENT TESTS", True, "Consignment Created Successfully!!!")
        else:
            self.ts.markFinal("New Consignment TESTS", False, "### Consignment couldn't be CREATED!!!")



