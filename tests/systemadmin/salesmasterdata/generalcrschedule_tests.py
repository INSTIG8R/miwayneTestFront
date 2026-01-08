import time
from pages.home.home_page import HomePage
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from pages.system_admin.sales_master_data.generalcrschedule_page import GeneralCRSchedulePage
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData


@pytest.mark.use_fixtures("oneTimeSetup", "setUp")
@ddt
class GeneralCRScheduleTests(unittest.TestCase):
    final_test: bool = True
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.ccsr = GeneralCRSchedulePage(self.driver)

    @pytest.mark.order(1)
    def test_validPage(self):
        self.lp = LoginPage(self.driver)
        self.lp.login("sabbir.sristy@w4solutions.com.au", "Iamsristy@36")
        self.sa = self.hp.gotoMasterData()
        time.sleep(2)
        self.ccsr = self.sa.gotoGeneralCRSchedule()
        result1 = self.ccsr.verifyGeneralCRScheduleTitle()
        self.ts.markFinal("GeneralCRSchedule Title verification", result1, "General CRSchedule Page Loaded")
        time.sleep(1)

    @pytest.mark.order(2)
    def test_edit(self):
        edit_ok = self.ccsr.edit()
        if edit_ok:
            self.ts.markFinal("Test_Editing", True, "Editing is working properly")
        else:
            self.ts.markFinal("Test_Editing", False, "Editing is NOT!! working properly")


    @pytest.mark.order(3)
    @data(*getCSVData("C:\\work\\miwayneTestFront\\data\\generalcrschedule_data.csv"))
    @unpack
    def test_ccsv(self, origin, destination, service, schedule, effectiveDate, effectiveDateTo, activity):
        working = self.ccsr.find_schedule(origin=origin, destination=destination, service=service, schedule=schedule, effectiveDate=effectiveDate, effectiveDateTo=effectiveDateTo, activity=activity)
        if self.ccsr.infonotpresent():
            self.ts.markFinal("Test_dataPresence", False, "###What you are looking for doesn't exist###")
        else:
            self.ts.mark(True, "Data Exist!!!")
        print(working)
        if working:
            self.ts.markFinal("Test_Filtering", True, "Filtering is working properly")
        else:
            self.ts.markFinal("Test_Filtering", False, "Filtering has ISSUES!!!")
