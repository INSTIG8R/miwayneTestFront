import time

from pages.customer_service.consignmentform_new23 import ConsignmentForm
from pages.customer_service.newconsignment_page import NewConsignmentPage
from pages.dashboard.dashboardtab import DashboardPage
from pages.home.home_page import HomePage
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest


# from ddt import ddt, data, unpack
# from utilities.read_data import getCSVData


@pytest.mark.use_fixtures("oneTimeSetup", "setUp")
# @ddt
class NewConsignmentSHTests(unittest.TestCase):
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
    def test_lines(self):
        _res = False
        self.nc.enterHeaderInformation(connote='DEMO0001001', accountName='BELGOTEX NZ LTD', status='DELIVERED')
        if self.nc.isElementPresent("//p[contains(normalize-space(), 'already exist')]", "xpath"):
            self.nc.editConsignmentNumber()
        time.sleep(2)
        self.nc.enterSenderDetails(senderCompanyName='BELGOTEX NZ LTD')
        self.nc.enterReceiverDetails(receiverCompanyName='CARPET AND MATLAND HENDERSON')
        self.nc.enterConsignmentLine_1(services1='SUPERECONOMY', item1='CONTAINER', commodity1='SOC TWENTY FOOT', quantity1='2', weight1='200', volume1='0.200')
        time.sleep(3)
        self.nc.enterConsignmentLine_2(item2='CARTON', commodity2='GENERAL CARTON', quantity2='1', weight2='100', volume2='0.804')
        rqf = self.nc.checkRequiredFieldsCL()
        if rqf:
            self.ts.mark(True, "Required Fields are filled")
        else:
            self.ts.mark(False, "Required Fields are not COMPLETELY FILLED!!!!!")

        _res = rqf
        weight_verify = self.nc.totalWeightVerification()

        if weight_verify:
            self.ts.mark(True, "Weight of the consignment Lines are correct")
        else:
            self.ts.mark(False, "Weights don't MATCH!!!")

        _res = weight_verify

        volume_verify = self.nc.totalVolumeVerification()
        if volume_verify:
            self.ts.mark(True, "Volumes of the consignment Lines are correct")
        else:
            self.ts.mark(False, "Volumes don't MATCH!!!")

        _res = volume_verify

        print(_res)
        if _res:
            self.ts.markFinal("Consignment Lines Test!!", True, "Consignment Lines Section is Working Fine!!!")
        else:
            self.ts.markFinal("Consignment Lines Test!!", False, "### Consignment Lines Section Test Failed!!!")
        time.sleep(3)

    @pytest.mark.order(3)
    def test_leggings(self):
        _res = False
        self.nc.enterLegging_1(carrier1='MAINSTREAM NZ LTD', depot1='', frm1='AUCKLAND', to1='CHRISTCHURCH', cost1='150', cn1='LC1')
        self.nc.enterLegging_2(carrier2='MAINSTREAM NZ LTD', depot2='', frm2='CHRISTCHURCH', to2='GREYMOUTH', cost2='150', cn2='LC2')
        #Verify Required Fields are Filled
        rqf = self.nc.checkRequiredFieldsLG()
        if rqf:
            self.ts.mark(True, "Required Fields are filled")
        else:
            self.ts.mark(False, "Required Fields are not COMPLETELY FILLED!!!!!")
        _res = rqf

        # Verify Total Legging Cost
        tlc = self.nc.verifyTotalLeggingCost()
        if tlc:
            self.ts.mark(True, "Legging Costs are EQUAL")
        else:
            self.ts.mark(False, "Legging Costs don't MATCH!!!")
        _res = tlc
        if _res:
            self.ts.markFinal("Consignment Leggings Test!!", True, "Consignment Leggings is Working Fine!!!")
        else:
            self.ts.markFinal("Consignment Leggings Test!!", False, "### Consignment Leggings Section Test Failed!!!")
        time.sleep(3)

    @pytest.mark.order(4)
    def test_sellRating(self):
        _res = False
        self.nc.enterSellRating()
        # err_logs = self.nc.returnErrorLogs()
        srg_test = self.nc.checkSRGenerated()
        if srg_test:
            self.ts.mark(True, "Sell Rate Generated!!!")
        else:
            self.ts.mark(False, "### Sell Rate Not Generated!!!")
        _res = srg_test
        if _res:
            self.ts.markFinal("Sell Rating Test", True, "Sell Rate Generated!!!")
        else:
            self.ts.markFinal("Sell Rating Test", False, "### Sell Rate Not Generated!!!")
        time.sleep(3)

    @pytest.mark.order(5)
    def test_sellRateSection(self):
        _res = False

        self.nc.enterSellRateFields(quotedPrice='275', noCharge='yes', quotedBy='EMBERSAW', pricingNotes='pc1', cancelled='yes')
        _srf = self.nc.checkSellRateFields()
        in_list = False in _srf
        if not in_list:
            _res = True

        if _res:
            self.ts.markFinal("Sell Rate Section Test", True, "Sell Rate Fields are Working Correctly!!!")
        else:
            self.ts.markFinal("Sell Rate Section Test", False, "### Sell Rate Fields are not Working Correctly!!!")
        time.sleep(3)

    @pytest.mark.order(6)
    def test_createconsignment(self):
        if self.nc.isElementPresent("//p[contains(normalize-space(), 'already exist')]", "xpath"):
            self.nc.editConsignmentNumber()
        if self.nc.checkGSR():
            self.nc.enterSellRating()
        cr_con = self.nc.clickCreateConsignment()
        if cr_con:
            self.ts.markFinal("New CONSIGNMENT TESTS", True, "Consignment Created Successfully!!!")
        else:
            self.ts.markFinal("New Consignment TESTS", False, "### Consignment couldn't be CREATED!!!")

