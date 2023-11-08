import time
from pages.dashboard.transaction_page import TransactionPage
from pages.home.home_page import HomePage
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData


@pytest.mark.use_fixtures("oneTimeSetup", "setUp")
@ddt
class TransactionTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.tp = TransactionPage(self.driver)

    @pytest.mark.order(1)
    def test_validPage(self):
        self.lp = LoginPage(self.driver)
        self.lp.login("fatin.khan@w4solutions.com.au", "devexpresscargo@fatiN97")
        self.dp = self.hp.clickDashboard()
        self.tp = self.dp.goToTransactions()
        result1 = self.tp.verifyTransactionsTitle()
        self.ts.markFinal("Transaction Title verification" , result1, "Transactions page loaded")



    @pytest.mark.order(2)
    @data(*getCSVData("D:\\work\\workspace_python\\wayne_express_cargo\\data\\transaction_data.csv"))
    @unpack
    def test_csv(self, connote, dateReadyFrom, dateReadyTo, accountName, customerReference,
                 carrier, carrierInvoices, carrierReference, manifest, pickup_city,
                 delivery_city, sender, receiver, option, service, receiver_reference,
                 booked_by, nocharge, zerosellcharge, zerocostrate, invoiced, checked_by,
                 fmsMatched, status):
        self.tp.find_consignments(connote=connote, dateReadyFrom=dateReadyFrom, dateReadyTo=dateReadyTo,
                                  accountName=accountName, customerReference=customerReference,
                                  carrier=carrier, carrierInvoices=carrierInvoices, carrierReference=carrierReference,
                                  manifest=manifest, pickup_city=pickup_city,
                                  delivery_city=delivery_city, sender=sender, receiver=receiver, option=option,
                                  service=service, receiver_reference=receiver_reference,
                                  booked_by=booked_by, nocharge=nocharge, zerosellcharge=zerosellcharge,
                                  zerocostrate=zerocostrate, invoiced=invoiced, checked_by=checked_by,
                                  fmsMatched=fmsMatched, status=status)

        if self.tp.infonotpresent():
            self.ts.markFinal("Test_dataPresence", False, "###What you are looking for doesn't exist###")
        else:
            self.ts.mark(True, "Data Exists!!!")

        if self.tp.pgtotWeightVerification():
            self.ts.mark(True, "page total weight is same")
        else:
            self.ts.mark(False, "page total Weight is NOT same!!")

        if self.tp.pgtotVolumeVerification():
            self.ts.mark(True, "page total Volume is same")
        else:
            self.ts.mark(False, "page total Volume is NOT same!!")

        if self.tp.pgtotlItemsVerification():
            self.ts.mark(True, "page total Items is same")
        else:
            self.ts.mark(False, "page total Items is NOT same!!")

        if self.tp.totalConsVerification():
            self.ts.markFinal("totalconsignment_test",True, "Consignment amount is same")
        else:
            self.ts.markFinal("totalconsignment_test",False, "Consignment amount is NOT same!!")



'''
filter the connotes then test for correctness((DONE)).. ((NEED))transition to ddt check afterwards. change tp code for select types and formlists if needed ((DONE)).. 
'''
