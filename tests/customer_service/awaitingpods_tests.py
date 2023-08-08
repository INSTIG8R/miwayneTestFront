from pages.home.home_page import HomePage
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from pages.customer_service.awaitingpods_page import AwaitingPodsPage
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData


@pytest.mark.use_fixtures("oneTimeSetup", "setUp")
@ddt
class AwaitingPodsTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.ap = AwaitingPodsPage(self.driver)

    @pytest.mark.order(1)
    def test_validPage(self):
        self.lp = LoginPage(self.driver)
        self.lp.login("fatin.khan@w4solutions.com.au", "devexpresscargo@fatiN97")
        self.ap = self.hp.gotoAwaitingPods()
        result1 = self.ap.verifyAwaitingPodsTitle()
        self.ts.markFinal("Awaiting Pods Title verification", result1, "Awaiting Pods page loaded")

    @pytest.mark.order(2)
    @data(*getCSVData("D:\\work\\workspace_python\\wayne_express_cargo\\awaitingpods_data.csv"))
    @unpack
    def test_apcsv(self, connote, dateReadyFrom, dateReadyTo, accountName, service, customerReference,
                   booked_by, pickup_city, delivery_city, sender, receiver, level, assigned_to, status):

        self.ap.find_consignment(connote=connote, dateReadyFrom=dateReadyFrom, dateReadyTo=dateReadyTo,
                                 accountName=accountName,
                                 service=service, customerReference=customerReference, booked_by=booked_by,
                                 pickup_city=pickup_city,
                                 delivery_city=delivery_city, sender=sender, receiver=receiver, level=level,
                                 assigned_to=assigned_to, status=status)
        if self.ap.infonotpresent():
            self.ts.markFinal("Test_dataPresence", False, "###What you are looking for doesn't exist###")
        else:
            self.ts.mark(True, "Data Exists!!!")

        if self.ap.pgtotWeightVerification():
            self.ts.mark(True, "page total weight is same")
        else:
            self.ts.mark(False, "page total Weight is NOT same!!")

        if self.ap.pgtotVolumeVerification():
            self.ts.mark(True, "page total Volume is same")
        else:
            self.ts.mark(False, "page total Volume is NOT same!!")

        if self.ap.pgtotlItemsVerification():
            self.ts.mark(True, "page total Items is same")
        else:
            self.ts.mark(False, "page total Items is NOT same!!")

        if self.ap.totalConsVerification():
            self.ts.markFinal("totalconsignment_test", True, "Consignment amount is same")
        else:
            self.ts.markFinal("totalconsignment_test", False, "Consignment amount is NOT same!!")
