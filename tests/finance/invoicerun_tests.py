from pages.home.home_page import HomePage
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from pages.finance.invoicerun_page import InvoiceRunPage
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData


@pytest.mark.use_fixtures("oneTimeSetup", "setUp")
@ddt
class InvoiceRunTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.ir = InvoiceRunPage(self.driver)

    @pytest.mark.order(1)
    def test_validPage(self):
        self.lp = LoginPage(self.driver)
        self.lp.login("fatin.khan@w4solutions.com.au", "devexpresscargo@fatiN97")
        self.ir = self.hp.gotoInvoiceRun()
        result1 = self.ir.verifyInvoiceRunTitle()
        self.ts.markFinal("Invoice Run Title verification", result1, "Invoice Run page loaded")

    @pytest.mark.order(2)
    @data(*getCSVData("D:\\work\\workspace_python\\wayne_express_cargo\\invoicerun_data.csv"))
    @unpack
    def test_ircsv(self, connote, dateReadyFrom, dateReadyTo, accountName, customerReference,
                   pickup_city, delivery_city, sender, receiver, option, service,
                   booked_by, nocharge, zerosellcharge, zerocostrate, checked_by, fmsMatched, status):

        self.ir.find_consignments(connote=connote, dateReadyFrom=dateReadyFrom, dateReadyTo=dateReadyTo,
                                  accountName=accountName, customerReference=customerReference, pickup_city=pickup_city,
                                  delivery_city=delivery_city, sender=sender, receiver=receiver, option=option,
                                  service=service,
                                  booked_by=booked_by, nocharge=nocharge, zerosellcharge=zerosellcharge,
                                  zerocostrate=zerocostrate,
                                  checked_by=checked_by, fmsMatched=fmsMatched, status=status)

        if self.ir.infonotpresent():
            self.ts.markFinal("Test_dataPresence", False, "###What you are looking for doesn't exist###")
        else:
            self.ts.mark(True, "Data Exists!!!")

        if self.ir.pgtotWeightVerification():
            self.ts.mark(True, "page total weight is same")
        else:
            self.ts.mark(False, "page total Weight is NOT same!!")

        if self.ir.pgtotVolumeVerification():
            self.ts.mark(True, "page total Volume is same")
        else:
            self.ts.mark(False, "page total Volume is NOT same!!")

        if self.ir.totalConsVerification():
            self.ts.markFinal("totalconsignment_test", True, "Consignment amount is same")
        else:
            self.ts.markFinal("totalconsignment_test", False, "Consignment amount is NOT same!!")
