import time
from pages.home.home_page import HomePage
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from pages.system_admin.sales_master_data.customermetrosrschedule_page import CustomerMetroSRSchedulePage
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData


@pytest.mark.use_fixtures("oneTimeSetup", "setUp")
@ddt
class CustomerMetroSRScheduleTests(unittest.TestCase):
    final_test: bool = True
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.ccsr = CustomerMetroSRSchedulePage(self.driver)

    @pytest.mark.order(1)
    def test_validPage(self):
        self.lp = LoginPage(self.driver)
        self.lp.login("sabbir.sristy@w4solutions.com.au", "Iamsristy@36")
        self.sa = self.hp.gotoMasterData()
        time.sleep(2)
        self.ccsr = self.sa.gotoCustomerMetroSRSchedule()
        result1 = self.ccsr.verifyCustomerMetroSRScheduleTitle()
        self.ts.markFinal("CustomerMetroSRSchedule Title verification", result1, "Customer Metro SRSchedule Page Loaded")
        time.sleep(1)

    @pytest.mark.order(2)
    @data(*getCSVData("C:\\work\\miwayneTestFront\\data\\customermetrosrschedule_data.csv"))
    @unpack
    def test_ccsv(self, accountName, origin, destination, service, gri, activity):
        working = self.ccsr.find_schedule(accountName=accountName, origin=origin, destination=destination, service=service, gri=gri, activity=activity)
        if self.ccsr.infonotpresent():
            self.ts.markFinal("Test_dataPresence", False, "###What you are looking for doesn't exist###")
        else:
            self.ts.mark(True, "Data Exist!!!")
        print(working)
        if working:
            self.ts.markFinal("Test_Filtering", True, "Filtering is working properly")
        else:
            self.ts.markFinal("Test_Filtering", False, "Filtering has ISSUES!!!")


