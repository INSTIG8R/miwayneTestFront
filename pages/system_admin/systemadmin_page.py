import time

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.system_admin.customer_service_master_data.addresses_page import AddressesPage
from pages.system_admin.customer_service_master_data.carriers_page import CarriersPage
from pages.system_admin.customer_service_master_data.contacts_page import ContactsPage
from pages.system_admin.customer_service_master_data.depot_page import DepotPage
from pages.system_admin.customer_service_master_data.documents_page import DocumentsPage

from pages.system_admin.finance_master_data.appliedcharge_page import AppliedChargePage
from pages.system_admin.finance_master_data.charges_page import ChargesPage
from pages.system_admin.finance_master_data.chargetypes_page import ChargeTypesPage
from pages.system_admin.finance_master_data.customers_page import CustomersPage
from pages.system_admin.finance_master_data.invoices_page import InvoicesPage
from pages.system_admin.finance_master_data.surcharge_page import SurchargePage
from pages.system_admin.finance_master_data.users_page import UsersPage

from pages.system_admin.operations_master_data.agencies_page import AgenciesPage
from pages.system_admin.operations_master_data.areamatric_page import AreaMatricPage
from pages.system_admin.operations_master_data.bookingsystem_page import BookingSystemPage
from pages.system_admin.operations_master_data.documentcategories_page import DocumentCategoriesPage
from pages.system_admin.operations_master_data.estimateddays_page import EstimatedDaysPage
from pages.system_admin.operations_master_data.fleetoptions_page import FleetOptionsPage
from pages.system_admin.operations_master_data.items_page import ItemsPage
from pages.system_admin.operations_master_data.liftingequipment_page import LiftingEquipmentPage
from pages.system_admin.operations_master_data.locationgroups_page import LocationGroupsPage
from pages.system_admin.operations_master_data.operationdays_page import OperationDaysPage
from pages.system_admin.operations_master_data.postcodes_page import PostCodesPage
from pages.system_admin.operations_master_data.prioritylevels_page import PriorityLevelsPage
from pages.system_admin.operations_master_data.rmpcategories_page import RMPCategoriesPage
from pages.system_admin.operations_master_data.services_page import ServicesPage
from pages.system_admin.operations_master_data.status_page import StatusPage
from pages.system_admin.operations_master_data.vehicles_page import VehiclesPage

from pages.system_admin.sales_master_data.customercommoditysrschedule_page import CustomerCommodityCRSchedulePage
from pages.system_admin.sales_master_data.customermetrosrschdeule_page import CustomerMetroSRSchedulePage
from pages.system_admin.sales_master_data.customersrschedule_page import CustomerSRSchedulePage
from pages.system_admin.sales_master_data.generatecrschedule_page import GenerateCRSchedulePage
from pages.system_admin.sales_master_data.industry_page import IndustryPage
from pages.system_admin.sales_master_data.metrosrschedule_page import MetroSRSchedulePage
from pages.system_admin.sales_master_data.schedule_types import ScheduleTypesPage

from pages.system_admin.system_master_data.configurations_page import ConfigurationsPage
from pages.system_admin.system_master_data.lookupsets_page import LookUpSetsPage
from pages.system_admin.system_master_data.migrationdictionary_page import MigrationDictionaryPage
from pages.system_admin.system_master_data.roles_page import RolesPage


class SystemAdminPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    #OPERATIONS MATER DATA

    _services = "wayne_id_Services"
    _status = "wayne_id_Status"
    _items = "wayne_id_Items"
    _vehicles = "wayne_id_Vehicles"
    _lifting_equipment = "wayne_id_Lifting Equipment"
    _fleet_options = "wayne_id_Fleet Options"
    _operation_days = "wayne_id_Operation Days"
    _estimated_days = "wayne_id_Estimated Days"
    _booking_systems = "wayne_id_Booking Systems"
    _postcodes = "wayne_id_Postcodes"
    _location_groups = "wayne_id_Location Groups"
    _area_matric = "wayne_id_Area Matric"
    _rmp_categories = "wayne_id_RMP Categories"
    _agencies = "wayne_id_Agencies"
    _document_categories = "wayne_id_Document Categories"
    _priority_levels = "wayne_id_Priority Levels"

    #finance_master_data

    _invoices ="wayne_id_Invoices"
    _surcharge = "wayne_id_Surcharge"
    _customers = "wayne_id_Customers"
    _users = "wayne_id_Users"
    _charges = "wayne_id_Charges"
    _charge_types = "wayne_id_Charge Types"
    _applied_charge = "wayne_id_Applied Charge"

    #SALES MASTER DATA

    _general_cr_schedule = "wayne_id_General Cost Rate Schedule"
    _metro_sr_schedule = "wayne_id_Metro Sell Rate Schedule"
    _customer_metro_sr_schedule = "wayne_id_Customer Metro Sell Rate Schedule"
    _customer_sr_schedule = "wayne_id_Customer Sell Rate Schedule"
    _customer_commodity_sr_schedule = "wayne_id_Customer Commodity Sell Rate Schedule"
    _industry = "wayne_id_Industry"
    _schedule_types = "wayne_id_Schedule Types"

    #CUSTOMER SERVICE MASTER DATA

    _carriers = "wayne_id_Carriers"
    _contacts = "wayne_id_Contacts"
    _addresses = "wayne_id_Addresses"
    _depot = "wayne_id_Depot"
    _documents = "wayne_id_Documents"

    #SYSTEM MASTER DATA

    _migration_dictionary = "wayne_id_Migration Dictionary"
    _lookup_sets = "wayne_id_LookUp Sets"
    _roles = "wayne_id_Roles"
    _configurations = "wayne_id_Configurations"


    #verification process
    _add_btn = "//button[@aria-label = 'Add']"


    ''' Fields '''

    def verifySystemAdminTitle(self):
        return self.verifyPageTitle("Express Cargo Ltd. | System Administration")

    '''OPERATIONS MASTER DATA'''



    def gotoServices(self):
        self.waitForElement(self._services)
        self.elementClick(self._services)
        self.waitForElement(self._add_btn, locatorType='xpath')
        #return Service page
        services = ServicesPage(self.driver)
        return services

    def gotoStatus(self):
        self.waitForElement(self._status)
        self.elementClick(self._status)
        self.waitForElement(self._add_btn, locatorType='xpath')
        #return Status Page
        status = StatusPage(self.driver)
        return status

    def gotoItems(self):
        self.waitForElement(self._items)
        self.elementClick(self._items)
        self.waitForElement("//button[@aria-label = 'Add Item']", locatorType='xpath')
        #return Items Page
        items = ItemsPage(self.driver)
        return items

    def gotoVehicles(self): #nothing inside this page yet
        self.waitForElement(self._vehicles)
        self.elementClick(self._vehicles)
        time.sleep(1)
        #self.waitForElement("//button[@aria-label = 'Add Item']", locatorType='xpath')
        #return Vehicles Page
        vehicles = VehiclesPage(self.driver)
        return vehicles

    def gotoLiftingEquipment(self):
        self.waitForElement(self._lifting_equipment)
        self.elementClick(self._lifting_equipment)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        #return Lifting Equipment Page
        le = LiftingEquipmentPage(self.driver)
        return le

    def gotoFleetOptions(self):
        self.waitForElement(self._fleet_options)
        self.elementClick(self._fleet_options)
        self.waitForElement(self._add_btn, locatorType='xpath')
        #return Fleet Options Page
        fo = FleetOptionsPage(self.driver)
        return fo

    def gotoOperationDays(self):
        self.waitForElement(self._operation_days)
        self.elementClick(self._operation_days)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        #return Operation Days Page
        od = OperationDaysPage(self.driver)
        return od

    def gotoEstimatedDays(self):
        self.waitForElement(self._estimated_days)
        self.elementClick(self._estimated_days)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        #return Estimated Days Page
        ed = EstimatedDaysPage(self.driver)
        return ed

    def gotoBookingSystem(self):
        self.waitForElement(self._booking_systems)
        self.elementClick(self._booking_systems)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        #return Booking Systems Page
        bookingsystem = BookingSystemPage(self.driver)
        return bookingsystem

    def gotoPostCodes(self):
        self.waitForElement(self._postcodes)
        self.elementClick(self._postcodes)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        #return Post Codes Page
        pc = PostCodesPage(self.driver)
        return pc

    def gotoLocationGroups(self):
        self.waitForElement(self._location_groups)
        self.elementClick(self._location_groups)
        # verify page loaded
        self.waitForElement("//button[@title = 'Add Country']", locatorType='xpath')
        #return Location Groups Page
        lg = LocationGroupsPage(self.driver)
        return lg

    def gotoAreaMatric(self):
        self.waitForElement(self._area_matric)
        self.elementClick(self._area_matric)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        # return Area Matric Page
        am = AreaMatricPage(self.driver)
        return am

    def gotoRMPCategories(self):
        self.waitForElement(self._rmp_categories)
        self.elementClick(self._rmp_categories)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        # return RMP Categories Page
        rmp = RMPCategoriesPage(self.driver)
        return rmp

    def gotoAgencies(self):
        self.waitForElement(self._agencies)
        self.elementClick(self._agencies)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        # return agencies
        ag = AgenciesPage(self.driver)
        return ag

    def gotoDocumentCategories(self):
        self.waitForElement(self._document_categories)
        self.elementClick(self._document_categories)
        # verify page loaded
        self.waitForElement("//button[@title='Add Doc Cateogry']", locatorType='xpath')
        # return Document Categories Page
        dc = DocumentCategoriesPage(self.driver)
        return dc

    def gotoPriorityLevels(self):
        self.waitForElement(self._priority_levels)
        self.elementClick(self._priority_levels)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        pl = PriorityLevelsPage(self.driver)
        return pl


    '''finance_master_data'''

    def gotoInvoices(self):
        self.waitForElement(self._invoices)
        self.elementClick(self._invoices)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        # return Invoices Page
        iv = InvoicesPage(self.driver)
        return iv

    def gotoSurcharge(self):
        self.waitForElement(self._surcharge)
        self.elementClick(self._surcharge)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        # return Surcharge Page
        su = SurchargePage(self.driver)
        return su

    def gotoCustomers(self):
        self.waitForElement(self._customers)
        self.elementClick(self._customers)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        # return Customers Page
        cu = CustomersPage(self.driver)
        return cu

    def gotoUsers(self):
        self.waitForElement(self._users)
        self.elementClick(self._users)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        # return Users Page
        us = UsersPage(self.driver)
        return us

    def gotoCharges(self):
        self.waitForElement(self._charges)
        self.elementClick(self._charges)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        # return Charges Page
        ch = ChargesPage(self.driver)
        return ch

    def gotoChargeTypes(self):
        self.waitForElement(self._charge_types)
        self.elementClick(self._charge_types)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        # return Charge Types Pages
        ct = ChargeTypesPage(self.driver)
        return ct

    def gotoAppliedCharge(self):
        self.waitForElement(self._applied_charge)
        self.elementClick(self._applied_charge)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        # return Applied Charge Page
        ac = AppliedChargePage(self.driver)
        return ac


    '''SALES MASTER DATA'''

    def gotoGenerateCRSchedule(self):
        self.waitForElement(self._general_cr_schedule)
        self.elementClick(self._general_cr_schedule)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        # return Generate CR Schedule Page
        gs = GenerateCRSchedulePage(self.driver)
        return gs

    def gotoMetroSRSchedule(self):
        self.waitForElement(self._metro_sr_schedule)
        self.elementClick(self._metro_sr_schedule)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        # return Metro SR Schedule Page
        ms = MetroSRSchedulePage(self.driver)
        return ms

    def gotoCustomerMetroSRSchedule(self):
        self.waitForElement(self._customer_metro_sr_schedule)
        self.elementClick(self._customer_metro_sr_schedule)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        # return Customer Metro SR Schedule Page
        cms =CustomerMetroSRSchedulePage(self.driver)
        return cms

    def gotoCustomerSRSchedule(self):
        self.waitForElement(self._customer_sr_schedule)
        self.elementClick(self._customer_sr_schedule)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        # return Customer SR Schedule Page
        cs = CustomerSRSchedulePage(self.driver)
        return cs

    def gotoCustomerCommoditySRSchedule(self):
        self.waitForElement(self._customer_commodity_sr_schedule)
        self.elementClick(self._customer_commodity_sr_schedule)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        # return Customer Commodity CR Schedule Page
        ccs =CustomerCommodityCRSchedulePage(self.driver)
        return ccs

    def gotoIndustry(self):
        self.waitForElement(self._industry)
        self.elementClick(self._industry)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        # return Industry Page
        ind = IndustryPage(self.driver)
        return ind

    def gotoScheduleTypes(self):
        self.waitForElement(self._schedule_types)
        self.elementClick(self._schedule_types)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        # return Schedule Types Page
        st = ScheduleTypesPage(self.driver)
        return st


    '''CUSTOMER SERVICE MASTER DATA'''

    def gotoCarriers(self):
        self.waitForElement(self._carriers)
        self.elementClick(self._carriers)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        # return Carriers Page
        carr = CarriersPage(self.driver)
        return carr

    def gotoContacts(self):
        self.waitForElement(self._contacts)
        self.elementClick(self._contacts)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        # return Contacts Page
        cc = ContactsPage(self.driver)
        return cc

    def gotoAddresses(self):
        self.waitForElement(self._addresses)
        self.elementClick(self._addresses)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        # return Addresses Page
        adr = AddressesPage(self.driver)
        return adr

    def gotoDepot(self):
        self.waitForElement(self._depot)
        self.elementClick(self._depot)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        # return depot page
        dpt = DepotPage(self.driver)
        return dpt

    def gotoDocuments(self):
        self.waitForElement(self._documents)
        self.elementClick(self._documents)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        #return Documents Page
        doc = DocumentsPage(self.driver)
        return doc


    '''SYSTEM MASTER DATA'''

    def gotoMigrationDictionary(self):
        self.waitForElement(self._migration_dictionary)
        self.elementClick(self._migration_dictionary)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        # return Migraion Dictionary Page
        md = MigrationDictionaryPage(self.driver)
        return md

    def gotoLookUpSets(self):
        self.waitForElement(self._lookup_sets)
        self.elementClick(self._lookup_sets)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        # return LookUp Sets Page
        ls = LookUpSetsPage(self.driver)
        return ls

    def gotoRoles(self):
        self.waitForElement(self._roles)
        self.elementClick(self._roles)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        # return Roles Page
        rp = RolesPage(self.driver)
        return rp

    def gotoConfigurations(self):
        self.waitForElement(self._configurations)
        self.elementClick(self._configurations)
        # verify page loaded
        self.waitForElement(self._add_btn, locatorType='xpath')
        # return Configurations Page
        conf = ConfigurationsPage(self.driver)
        return conf


