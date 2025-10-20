import time
from pages.dashboard.dashboardtab import DashboardPage
from pages.home.home_page import HomePage
from pages.home.login_page import LoginPage
from pages.sales.quoteform_page import QuoteForm
from utilities.teststatus import TestStatus
import unittest
import pytest


# from ddt import ddt, data, unpack
# from utilities.read_data import getCSVData


@pytest.mark.use_fixtures("oneTimeSetup", "setUp")  #
# @ddt
class NewQuoteSHTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.db = DashboardPage(self.driver)
        self.qf = QuoteForm(self.driver)

    @pytest.mark.order(1)
    def test_secondhalf(self):
        self.lp = LoginPage(self.driver)
        self.lp.login("sabbir.sristy@w4solutions.com.au", "Iamsristy@36")
        self.qf = self.hp.gotoQuoteForm()
        nc_res = self.qf.verifyNewQuoteTitle()
        self.ts.markFinal("Quote Form load Check", nc_res, "Quote Form Loaded")

        _res = False
        self.qf.enterHeaderInformation(accountName='BELGOTEX NZ LTD', customerRef='1231231231',
                                       receiverRef='assdasd123123')

        self.qf.enterSenderDetails(senderCompanyName='BELGOTEX HA CRES')
        self.qf.enterReceiverDetails(receiverCompanyName='BELGOTEX C/O EXPRESS CARGO')
        enabled = self.qf.enterConsignmentLine_1(services1='SUPERECONOMY', item1='ITEM', commodity1='GENERAL ITEM',
                                                 quantity1='2', weight1='100', volume1='0.448')
        time.sleep(3)
        # self.nc.enterConsignmentLine_2(item2='CARTON', commodity2='GENERAL CARTON', quantity2='1', weight2='100', volume2='0.804')
        rqf = self.qf.checkRequiredFieldsCL()
        if rqf:
            self.ts.mark(True, "Required Fields are filled")
        else:
            self.ts.mark(False, "Required Fields are not COMPLETELY FILLED!!!!!")

        # enabled: bool = self.qf.checkEstimatePriceBtnDisabled()
        if enabled:
            self.ts.mark(False, "Sell Rate Enabled before lines completed - Not Working!!")
        else:
            self.ts.mark(True, "Sell Rate Not Enabled Yet - Working")

        _res = rqf
        weight_verify = self.qf.totalWeightVerification()

        if weight_verify:
            self.ts.mark(True, "Weight of the consignment Lines are correct")
        else:
            self.ts.mark(False, "Weights don't MATCH!!!")

        _res = weight_verify

        volume_verify = self.qf.totalVolumeVerification()
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

        _res = False
        self.qf.scrollWindowDown()

    @pytest.mark.order(2)
    def last_half(self):
        print("---------------In Sell Rating Section---------------")
        self.qf.enterSellRating()
        srg_test = self.qf.checkSRGenerated()
        _err_logs = self.qf.returnErrorLogs()
        if srg_test:
            self.ts.mark(True, "Sell Rate Generated!!!")
        else:
            self.ts.mark(False, "### Sell Rate Not Generated!!!")
        _res = srg_test
        print(len(_err_logs))
        if len(_err_logs) > 0:
            self.ts.mark(False, "Error during Price Estimation")
        else:
            self.ts.mark(True, "Price estimated Successfully")

        print(_res)
        if _res:
            self.ts.mark(True, "Price Estimated!!!")
        else:
            self.ts.mark(False, "### Price Not Estimated!!!")
        time.sleep(2)

        _res = False

        self.qf.enterSellRateFields(pricingNotes='pc1')
        _srf = self.qf.checkSellRateFields()
        if _srf:
            self.ts.mark( True, "Sell Rate Fields are Working Correctly!!!")
        else:
            self.ts.mark( False, "### Sell Rate Fields are not Working Correctly!!!")
        time.sleep(2)

        _res = False
        self.qf.enterAdditionalInformation(atl='yes', cn='customers numba wan')
        _res = self.qf.checkAdditionalInformation()
        if _res:
            self.ts.mark(True,
                              "Additional Information Fields are Working Correctly!!!")
        else:
            self.ts.mark(False,
                              "### Additional Information Fields are not Working Correctly!!!")
        time.sleep(2)

        # cr_con = self.qf.clickCreateQuote()
        # if cr_con:
        #     self.ts.markFinal("New CONSIGNMENT TESTS", True, "Quote Created Successfully!!!")
        # else:
        #     self.ts.markFinal("New Consignment TESTS", False, "### Quote couldn't be CREATED!!!")
        #
        #
