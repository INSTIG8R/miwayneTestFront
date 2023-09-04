from pages.home.home_page import HomePage
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from pages.customer_service.drafts_page import DraftsPage
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData


@pytest.mark.use_fixtures("oneTimeSetup", "setUp")
@ddt
class DraftsTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.dp = DraftsPage(self.driver)

    @pytest.mark.order(1)
    def test_validPage(self):
        self.lp = LoginPage(self.driver)
        self.lp.login("fatin.khan@w4solutions.com.au", "devexpresscargo@fatiN97")
        self.dp = self.hp.gotoDrafts()
        result1 = self.dp.verifyDraftsTitle()
        self.ts.markFinal("Drafts Title verification", result1, "Drafts page loaded")

    @pytest.mark.order(2)
    @data(*getCSVData("D:\\work\\workspace_python\\wayne_express_cargo\\data\\drafts_data.csv"))
    @unpack
    def test_dpcsv(self, connote, dateReadyFrom, dateReadyTo, accountName, service, customerReference,
                   pickup_city, delivery_city, sender, receiver, converted_cons, status):

        errs = []
        self.dp.findConsignments(connote=connote, dateReadyFrom=dateReadyFrom, dateReadyTo=dateReadyTo,
                                 accountName=accountName,
                                 service=service, customerReference=customerReference,
                                 pickup_city=pickup_city,
                                 delivery_city=delivery_city, sender=sender, receiver=receiver,
                                 converted_cons=converted_cons, status=status)
        if self.dp.infonotpresent():
            self.ts.markFinal("Test_dataPresence", False, "###What you are looking for doesn't exist###")
            errs.append(False)
        else:
            self.ts.mark(True, "Data Exists!!!")

        if self.dp.pgtotWeightVerification():
            self.ts.mark(True, "page total weight is same")
        else:
            self.ts.mark(False, "page total Weight is NOT same!!")
            errs.append(False)

        if self.dp.pgtotVolumeVerification():
            self.ts.mark(True, "page total Volume is same")
        else:
            self.ts.mark(False, "page total Volume is NOT same!!")
            errs.append(False)

        if self.dp.pgtotlItemsVerification():
            self.ts.mark(True, "page total Items is same")
        else:
            self.ts.mark(False, "page total Items is NOT same!!")
            errs.append(False)

        if self.dp.totalConsVerification():
            self.ts.mark(True, "Consignment amount is same")
        else:
            self.ts.mark(False, "Consignment amount is NOT same!!")
            errs.append(False)

        if False in errs:
            self.ts.markFinal("Test_valueEquality", False, "###Error in values!!!")
        else:
            self.ts.markFinal("Test_equality", True, "###No Issues Found!!")
