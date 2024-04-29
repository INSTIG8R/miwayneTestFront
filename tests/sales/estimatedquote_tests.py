import time
from pages.home.home_page import HomePage
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from pages.sales.estimatedquote_page import EstimatedQuotePage
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
import allure


@pytest.mark.use_fixtures("oneTimeSetup", "setUp")
@ddt
class EstimatedQuoteTests(unittest.TestCase):
    final_test: bool = True

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.eq = EstimatedQuotePage(self.driver)

    @pytest.mark.order(1)
    def test_validPage(self):
        self.lp = LoginPage(self.driver)
        self.lp.login("sabbir.sristy@w4solutions.com.au", "Iamsristy@36")
        self.eq = self.hp.gotoEstimatedQuotePage()
        time.sleep(2)
        result1 = self.eq.verifyAcceptedQuoteTitle()
        self.ts.markFinal("Estimated Quote Title verification", result1, "Estimated Quote page loaded")

    @pytest.mark.order(2)
    @data(*getCSVData("D:\\work\\workspace_python\\wayne_express_cargo\\data\\estimatedquote_data.csv"))
    @unpack
    def test_ccsv(self, quote, dateReadyFrom, dateReadyTo, accountName, service, customerReference,
                  quoted_by, pickup_city, delivery_city, sender, receiver, verified_request,
                  inactive_transactions):

        self.eq.find_quote(quote=quote, dateReadyFrom=dateReadyFrom, dateReadyTo=dateReadyTo,
                           accountName=accountName, service=service,
                           customerReference=customerReference, quoted_by=quoted_by,
                           pickup_city=pickup_city, delivery_city=delivery_city, sender=sender, receiver=receiver,
                           verified_request=verified_request,
                           inactive_transactions=inactive_transactions
                           )
        if self.eq.infonotpresent():
            self.ts.markFinal("Test_dataPresence", False, "###What you are looking for doesn't exist###")
        else:
            self.ts.mark(True, "Data Exist!!!")
