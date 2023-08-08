from selenium.webdriver.common.by import By

from pages.system_admin.systemadmin_page import SystemAdminPage
from pages.home.home_page import HomePage
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.use_fixtures("oneTimeSetup", "setUp")
class SystemAdminTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.sa = SystemAdminPage(self.driver)

    @pytest.mark.order(1)
    def test_validPage(self):
        self.lp = LoginPage(self.driver)
        self.lp.login("sabbir.sristy@bishudigital.com", "Iamtheone@36")
        self.sa = self.hp.gotoSystemAdministration()
        result1 = self.sa.verifySystemAdminTitle()
        self.ts.markFinal("System Admin Title verification", result1, "System Admin page loaded")

    @pytest.mark.order(2)
    def test_validPages(self):
        self.services = self.sa.gotoServices()
        service_test = self.services.verifyServicesTitle()
        self.ts.mark(service_test, "Service Page Loaded")
        self.driver.back()
        self.status = self.sa.gotoStatus()
        status_test = self.status.verifyStatusTitle()
        self.ts.mark(status_test, "Status Page loaded")
        self.driver.back()
        self.items = self.sa.gotoItems()
        items_test = self.items.verifyItemsTitle()
        self.ts.mark(items_test, "Items Page loaded")
        self.driver.back()
        self.vehicles = self.sa.gotoVehicles()
        vehicles_test = self.vehicles.verifyVehiclesTitle()
        self.ts.mark(vehicles_test, "Vehicles Page loaded")
        self.driver.back()
        self.le = self.sa.gotoLiftingEquipment()
        le_test = self.le.verifyLiftingEquipmentTitle()
        self.ts.mark(le_test, "Lifting Equipment Page loaded")
        self.driver.back()
        self.fo = self.sa.gotoFleetOptions()
        fo_test = self.fo.verifyFleetOptionsTitle()
        self.ts.mark(fo_test, "Fleet Options Page loaded")
        self.driver.back()
        self.od = self.sa.gotoOperationDays()
        od_test = self.od.verifyOperationDaysTitle()
        self.ts.mark(od_test, "Operation Days Page loaded")
        self.driver.back()
        self.ed = self.sa.gotoEstimatedDays()
        ed_test = self.ed.verifyEstimatedDaysTitle()
        self.ts.mark(ed_test, "Estimated Days Page loaded")
        self.driver.back()
        self.bookingsystem = self.sa.gotoBookingSystem()
        bookingsystem_test = self.bookingsystem.verifyBookingSystemTitle()
        self.ts.mark(bookingsystem_test, "Booking System Page loaded")
        self.driver.back()
        self.pc = self.sa.gotoPostCodes()
        pc_test = self.pc.verifyPostCodesTitle()
        self.ts.mark(pc_test,"Post Codes Page loaded")
        self.driver.back()
        self.lg = self.sa.gotoLocationGroups()
        lg_test = self.lg.verifyLocationGroupsTitle()
        self.ts.mark(lg_test, "Location Groups Page Loaded")
        self.driver.back()
        self.am = self.sa.gotoAreaMatric()
        am_test = self.am.verifyAreaMatricTitle()
        self.ts.mark(am_test, "Area Matric Page loaded")
        self.driver.back()
        self.rmp = self.sa.gotoRMPCategories()
        rmp_test = self.rmp.verifyRMPCategoriesTitle()
        self.ts.mark(rmp_test, "RMPCategories Page loaded")
        self.driver.back()
        self.ag = self.sa.gotoAgencies()
        ag_test = self.ag.verifyAgenciesTitle()
        self.ts.mark(ag_test, "Agencies Page loaded")
        self.driver.back()
        self.dc = self.sa.gotoDocumentCategories()
        dc_test = self.dc.verifyDocumentCategoriesTitle()
        self.ts.mark(dc_test, "Document Categories Page loaded")
        self.driver.back()
        self.pl = self.sa.gotoPriorityLevels()
        pl_test = self.pl.verifyPriorityLevelsTitle()
        self.ts.mark(pl_test, "Priority Page Loaded")
        self.driver.back()

        # FINANCE MASTER DATA

        self.iv = self.sa.gotoInvoices()
        iv_test = self.iv.verifyInvoicesTitle()
        self.ts.mark(iv_test, "Invoices Page Loaded")
        self.driver.back()
        self.su = self.sa.gotoSurcharge()
        su_test = self.su.verifySurchargeTitle()
        self.ts.mark(su_test, "Surcharge Page Loaded")
        self.driver.back()
        self.cu = self.sa.gotoCustomers()
        cu_test = self.cu.verifyCustomersTitle()
        self.ts.mark(cu_test, "Customers Page Loaded")
        self.driver.back()
        self.us = self.sa.gotoUsers()
        us_test = self.us.verifyUsersTitle()
        self.ts.mark(us_test, "Users Page Loaded")
        self.driver.back()
        self.ch = self.sa.gotoCharges()
        ch_test = self.ch.verifyChargesTitle()
        self.ts.mark(ch_test, "Charges Page Loaded")
        self.driver.back()
        self.ct = self.sa.gotoChargeTypes()
        ct_test = self.ct.verifyChargeTypesTitle()
        self.ts.mark(ct_test, "Charge Types Page loaded")
        self.driver.back()
        self.ac = self.sa.gotoAppliedCharge()
        ac_test = self.ac.verifyAppliedChargeTitle()
        self.ts.mark(ac_test, "Applied Charge Page loaded")
        self.driver.back()

        # SALES MASTER DATA

        self.gs = self.sa.gotoGenerateCRSchedule()
        gs_test = self.gs.verifyGenerateCRScheduleTitle()
        self.ts.mark(gs_test, "Generate CR Schedule Page Loaded")
        self.driver.back()
        self.ms = self.sa.gotoMetroSRSchedule()
        ms_test = self.ms.verifyMetroSRScheduleTitle()
        self.ts.mark(ms_test, "Metro SR Schedule Page Loaded")
        self.driver.back()
        self.cms = self.sa.gotoCustomerMetroSRSchedule()
        cms_test = self.cms.verifyCustomerMetroSRScheduleTitle()
        self.ts.mark(cms_test, "Customer Metro SR Schedule Page Loaded")
        self.driver.back()
        self.cs = self.sa.gotoCustomerSRSchedule()
        cs_test = self.cs.verifyCustomerSRScheduleTitle()
        self.ts.mark(cs_test, "Customer SR Schedule Page Loaded")
        self.driver.back()
        self.ccs = self.sa.gotoCustomerCommoditySRSchedule()
        ccs_test = self.ccs.verifyCustomerCommodityCRScheduleTitle()
        self.ts.mark(ccs_test, "Customer Commodity CR Schedule")
        self.driver.back()
        self.ind = self.sa.gotoIndustry()
        ind_test = self.ind.verifyIndustryTitle()
        self.ts.mark(ind_test, "Industry Page Loaded")
        self.driver.back()
        self.st = self.sa.gotoScheduleTypes()
        st_test = self.st.verifyScheduleTypesTitle()
        self.ts.mark(st_test, "Schedule Types Page Loaded")
        self.driver.back()

        # CUSTOMER SERVICE MASTER DATA

        # carr cc adr dpt doc

        self.carr = self.sa.gotoCarriers()
        carr_test = self.carr.verifyCarriersTitle()
        self.ts.mark(carr_test, "Carriers Page Loaded")
        self.driver.back()
        self.cc = self.sa.gotoContacts()
        cc_test = self.cc.verifyContactsTitle()
        self.ts.mark(cc_test, "Contacts Page Loaded")
        self.driver.back()
        self.adr = self.sa.gotoAddresses()
        adr_test = self.adr.verifyAddressesTitle()
        self.ts.mark(adr_test, "Addresses Page Loaded")
        self.driver.back()
        self.dpt = self.sa.gotoDepot()
        dpt_test = self.dpt.verifyDepotTitle()
        self.ts.mark(dpt_test, "Depot Page Loaded")
        self.driver.back()
        self.doc = self.sa.gotoDocuments()
        doc_test = self.doc.verifyDocumentsTitle()
        self.ts.mark(doc_test, "Documents Page Loaded")
        self.driver.back()


        # SYSTEM MASTER DATA
        # md ls rp conf

        self.md = self.sa.gotoMigrationDictionary()
        md_test = self.md.verifyMigrationDictionaryTitle()
        self.ts.mark(md_test, "Migration Dictionary Page Loaded")
        self.driver.back()
        self.ls = self.sa.gotoLookUpSets()
        ls_test = self.ls.verifyLookUpSetsTitle()
        self.ts.mark(ls_test, "LookUp Sets Page Loaded")
        self.driver.back()
        self.rp = self.sa.gotoRoles()
        rp_test = self.rp.verifyRolesTitle()
        self.ts.mark(rp_test, "Roles Page Loaeded")
        self.driver.back()
        self.conf = self.sa.gotoConfigurations()
        conf_test = self.conf.verifyConfigurationsTitle()
        self.ts.mark(conf_test, "Configurations Page Loaded")
        logo = self.driver.find_element(By.XPATH, "//div[@title = 'Home']")
        logo.click()
        last_test = self.hp.verifyPageTitle("Express Cargo Ltd. | Home")
        self.ts.markFinal("All Pages Load Test", last_test, "All tests ran successfully")