import time
from pages.home.home_page import HomePage
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from pages.customer_service.currentconsignment_page import CurrentConsignmentPage
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
import allure


@pytest.mark.use_fixtures("oneTimeSetup", "setUp")
@ddt
class CurrentConsignmentTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.cc = CurrentConsignmentPage(self.driver)

    @pytest.mark.order(1)
    def test_validPage(self):
        self.lp = LoginPage(self.driver)
        self.lp.login("fatin.khan@w4solutions.com.au", "devexpresscargo@fatiN97")
        self.cc = self.hp.gotoCurrentConsignment()
        result1 = self.cc.verifyCurrentConsignmentTitle()
        self.ts.markFinal("Current Consignment Title verification", result1, "Current Consignment page loaded")

    @pytest.mark.order(2)
    @data(*getCSVData("D:\\work\\workspace_python\\wayne_express_cargo\\data\\currentconsignment_data.csv"))
    @unpack
    def test_ccsv(self, connote, dateReadyFrom, dateReadyTo, datePickUpFrom, datePickUpTo, accountName, option, service, customerReference,
                  booked_by, pickup_city, delivery_city, sender, receiver, container_number, priority_level,
                  assigned_to, carrier,
                  estimated_delivery, status):
        self.cc.find_consignment(connote=connote, dateReadyFrom=dateReadyFrom, dateReadyTo=dateReadyTo, datePickUpFrom=datePickUpFrom, datePickUpTo=datePickUpTo,
                                 accountName=accountName, option=option, service=service,
                                 customerReference=customerReference, booked_by=booked_by,
                                 pickup_city=pickup_city,
                                 delivery_city=delivery_city, sender=sender, receiver=receiver,
                                 container_number=container_number,
                                 priority_level=priority_level, assigned_to=assigned_to, carrier=carrier,
                                 estimated_delivery=estimated_delivery, status=status)
        if self.cc.infonotpresent():
            self.ts.markFinal("Test_dataPresence", False, "###What you are looking for doesn't exist###")
        else:
            self.ts.mark(True, "Data Exist!!!")

        if self.cc.pgtotWeightVerification():
            self.ts.mark(True, "page total weight is same")
        else:
            self.ts.mark(False, "page total Weight is NOT same!!")

        if self.cc.pgtotVolumeVerification():
            self.ts.mark(True, "page total Volume is same")
        else:
            self.ts.mark(False, "page total Volume is NOT same!!")

        if self.cc.pgtotlItemsVerification():
            self.ts.mark(True, "page total Items is same")
        else:
            self.ts.mark(False, "page total Items is NOT same!!")

