import random
import re
import time

from selenium.webdriver.common.by import By

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains


class ConsignmentForm(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.alert = Alert(driver)
        self.action = ActionChains(driver)

    # Locators

    # Headers
    _connote = "//input[@tabindex = 1]"
    _account_name = "//input[@tabindex = 2]"
    _status = "//input[@tabindex = 4]"
    _date_allocated = "//input[@id = 'wayne_id_Date Allocated']"
    _customer_ref = "//input[@tabindex = 7]"
    _receiver_ref = "//input[@tabindex = 8]"
    _date_ready = "//input[@id = 'wayne_id_Date Ready']"
    _estimated_delivery_date = "//input[@id = 'wayne_id_Estimated Delivery Date']"
    _assigned_to = "//input[@id = 'wayne_id_Assigned To']"
    _priority_level = "//input[@id = 'wayne_id_Priority Level']"

    _data_fetched_popup = "//div[contains(text(),'Account Info Fetched')]"

    # Sender Details

    ## ADDRESS TYPES
    _residential_at = "// li[normalize - space() = 'RESIDENTIAL']"
    _business_at = " //li[normalize-space()='BUSINESS']"
    _residential_business_at = " //li[normalize-space()='RESIDENTIAL BUSINESS']"

    _enter_addr_l = "//input[@tabindex = '16']"
    _company_l = "//input[@tabindex='17'][@id='wayne_id_company Name']"
    _addr_type_l = "//div[@id ='wayne_id_address type'][@tabindex='18']"
    _lot_l = "//input[@tabindex='19']"
    _road_l = "//input[@tabindex='20']"
    _street_l = "//input[@tabindex='21']"
    _suburb_l = "//input[@tabindex='22']"
    _city_l = "//input[@tabindex='23']"
    _state_l = "//input[@tabindex='24']"
    _post_code_l = "//input[@tabindex='25']"
    _forklift_l = "//input[@tabindex='27']"
    _driver_l = "//input[@tabindex='28']"
    _open_time_l = "//input[@id='wayne_id_openTime']"  # [0]
    _close_time_l = "//input[@id='wayne_id_close Time']"  # [0]
    _vehicle_l = "//input[@id='wayne_id_vehicle'][@tabindex =31]"
    _vehicle_type_l = "//input[@id='wayne_id_vehicle Type'][@tabindex =32]"
    _charges_l = "//input[@tabindex = '33']"
    _special_instruction_l = "//textarea[@tabindex = '34']"
    _create_addr_l = "//button[@tabindex='35'][@id = 'wayne_id_Edit Address']"  ##Not Used

    _charges_lst_f = "//div[@data-tag-index=0]/span"  # [0]
    _charges_rst_f = ""

    # Receiver details

    _enter_addr_r = "//input[@tabindex = '36']"
    _company_r = "//input[@tabindex = '37']"
    _addr_type_r = "//div[@tabindex = '38']"
    _lot_r = "//input[@tabindex = '39']"
    _road_r = "//input[@tabindex = '40']"
    _street_r = "//input[@tabindex = '41']"
    _suburb_r = "//input[@tabindex = '42']"
    _city_r = "//input[@tabindex = '43']"
    _state_r = "//input[@tabindex = '44']"
    _post_code_r = "//input[@tabindex = '45']"
    _forklift_r = "//input[@tabindex = '47']"
    _driver_r = "//input[@tabindex = '48']"
    _open_time_r = "//input[@id='wayne_id_openTime']"  # [1]
    _close_time_r = "//input[@id='wayne_id_close Time']"  # [1]
    _vehicle_r = "//input[@tabindex = '51']"
    _vehicle_type_r = "//input[@tabindex = '52']"
    _charges_r = "//input[@tabindex = '53']"
    _special_instruction_r = "//textarea[@tabindex = '54']"
    _create_addr_r = "//button[@tabindex='60']/span[normalize-space()='EDIT ADDRESS']"  ##Not Used

    # Contact Details sender

    _first_name_l = "//input[@tabindex = '56']"
    _last_name_l = "//input[@tabindex = '57']"
    _email_l = "//input[@tabindex = '58']"
    _phone_number_l = "//input[@tabindex = '59']"
    _mobile_number_l = "//input[@tabindex = '60']"
    _role_l = "//div[@tabindex = '61']"
    _create_contact_l = "//button[@tabindex='62']"

    # Contact Details receiver

    _first_name_r = "//input[@tabindex='63']"
    _last_name_r = "//input[@tabindex='64']"
    _email_r = "//input[@tabindex='65']"
    _phone_number_r = "//input[@tabindex='66']"
    _mobile_number_r = "//input[@tabindex='67']"
    _role_r = "//select[@tabindex = '68']"
    _create_contact_r = "//button[@tabindex='69']"

    # Consignment Lines ( CAN HAVE VARIOUS LINES)

    _line_number = "//strong[text() = 1]"  # [0]
    _services1 = "//input[@tabindex='70']"
    _weight_unit1 = "//div[@tabindex='71']"
    _dimension_unit1 = "//div[@tabindex='72']"
    _container_number1 = "//input[@tabindex='73']"
    _agency1 = "//input[@tabindex='74']"
    _item1 = "//input[@tabindex='75'][@id ='wayne_id_Item0']"
    _commodity1 = "//input[@tabindex='76'][@id ='wayne_id_Commodity0']"
    _description1 = "//input[@tabindex='77'][@id ='wayne_id_Description0']"
    _quantity1 = "//input[@tabindex='78'][@id ='wayne_id_Quantity0']"
    _weight1 = "//input[@tabindex='79'][@id ='wayne_id_Weight0']"
    _volume1 = "//input[@tabindex='80'][@id ='wayne_id_Volume0']"
    _length1 = "//input[@tabindex='81'][@id ='wayne_id_Length0']"
    _width1 = "//input[@tabindex='82'][@id='wayne_id_Width0']"
    _height1 = "//input[@tabindex='83'][@id ='wayne_id_Height0']"
    _dg1 = "//input[@tabindex='84'][@id ='wayne_id_dangerous goods ?0']"
    _add_line_btn = "//button[@id ='wayne_id_Add line']"
    _total_lines = "wayne_id_Total lines"
    _total_item_count = "wayne_id_Total item count"
    _total_weight = "wayne_id_Total weight"
    _total_volume = "wayne_id_Total volume"

    _item2 = "//input[@tabindex='89'][@id='wayne_id_Item1']"
    _commodity2 = "//input[@tabindex='90'][@id='wayne_id_Commodity1']"
    _description2 = "//input[@tabindex='91'][@id='wayne_id_Description1']"
    _quantity2 = "//input[@tabindex='92'][@id='wayne_id_Quantity1']"
    _weight2 = "//input[@tabindex='93'][@id='wayne_id_Weight1']"
    _volume2 = "//input[@tabindex='94'][@id='wayne_id_Volume1']"
    _length2 = "//input[@tabindex='95'][@id='wayne_id_Length1']"
    _width2 = "//input[@tabindex='96'][@id='wayne_id_Width1']"
    _height2 = "//input[@tabindex='97'][@id='wayne_id_Height1']"
    _dg2 = "//input[@tabindex='98'][@id='wayne_id_dangerous goods ?1']"

    # delete button
    _delete_line_one = "//button[@tabindex = 88]"
    _delete_line_two = "button[@tabindex = 102]"

    _date1 = "//input[@tabindex = 112]"
    _carrier1 = "//input[@id='wayne_id_Carrier0']"
    _depot1 = "//input[@id='wayne_id_Depot0']"
    _type1 = "//div[@id='wayne_id_type0']"
    _from1 = "//input[@id='wayne_id_from0']"
    _to1 = "//input[@id='wayne_id_to0']"
    _carrier_ref1 = "//input[@id='wayne_id_carrier Reference0']"
    _carrier_invoice1 = "//input[@id='wayne_id_carrier invoice0']"
    _cost1 = "//input[@id='wayne_id_cost0']"
    _cost_more1 = "//button[@id='Legging Notes0']"

    _cost_more1_desc = "//textarea[@id='wayne_id_Notes0']"
    _cost_more1_cancel_btn = "//button[@id='wayne_id_Close']"
    _add_leg_btn = "wayne_id_Add leg"
    _total_legs = "wayne_id_Total legs"
    _total_legging_cost = "wayne_id_Total cost"

    # 2nd leg
    _date2 = "//input[@id = 'wayne_id_Collection Date']"
    _carrier2 = "//input[@id = 'wayne_id_Carrier1']"
    _depot2 = "//input[@id = 'wayne_id_Depot1']"
    _type2 = "//div[@id = 'wayne_id_type1']"
    _from2 = "//input[@id = 'wayne_id_from1']"
    _to2 = "//input[@id = 'wayne_id_to1']"
    _carrier_ref2 = "//input[@id = 'wayne_id_carrier Reference1']"
    _carrier_invoice2 = "//input[@id = 'wayne_id_carrier invoice1']"
    _cost2 = "//input[@id = 'wayne_id_cost1']"
    _cost_more2 = "(.//*[normalize-space(text()) and normalize-space(.)='cost'])[4]/following::*[name()='svg'][1]"
    _cost_more2_desc = "//textarea[@id='wayne_id_Notes1']"
    _cost_more2_cancel_btn = "//*/text()[normalize-space(.)='CLOSE']/parent::*"

    # Sell Rating
    _general_sell_rate = "wayne_id_Generate Sell Rate"
    _total_sell_rate = "//input[@id='wayne_id_Total sell rate']"
    _connote_sr = "wayne_id_CONNOTE"
    _account_name_sr = "//p[@id ='BELGOTEX NZ LTD']"
    _total_sr_btn = "//button[@tabindex='141']"
    _total_sr_cancel_btn = "//button[@tabindex =0]"
    _quoted_price = "//input[@id='wayne_id_Quoted price']"
    _quoted_by = "//input[@id='wayne_id_Quoted By']"
    _no_charge = "wayne_id_No charge?"
    _pricing_notes = "wayne_id_Pricing Notes?"
    _pricing_notes_description = "wayne_id_Pricing Notes"
    _pricing_notes_desc_save_btn = "wayne_id_Save"
    _pricing_notes_desc_close_btn = "wayne_id_Close"
    _cancelled = "wayne_id_cancelled?"

    # Additional Information

    _insurance = "//div[@id='wayne_id_Insurance Type']"
    _authority_to_leave = "wayne_id_Authority To Leave?"
    _dangerous_goods_ai = "//input[@tabindex='112']"
    _pod_uploaded = "//input[@tabindex='107']"
    _christell_notes = "wayne_id_Christel Notes"
    _special_instruction_ai = "//textarea[@tabindex='111']"
    _general_docs = "//button[@tabindex='109']"
    _general_docs_close = "wayne_id_Close"

    # Calculations

    _total_charge = "wayne_id_Total Sell Charge:"
    _total_cost = "wayne_id_Total Cost:"
    _gross_margin = "wayne_id_Gross Margin($): "
    _gross_margin_percentage = "wayne_id_Gross Margin(%): "

    # Footer buttons

    _create_consignment = "(.//*[normalize-space(text()) and normalize-space(.)='Quoted By'])[2]/following::button[2]"  # //button[@tabindex='151']
    _go_back = "wayne_id_Cancel Submit"
    _save_draft = "wayne_id_Save Draft"

    # DEPOT REQUIRED ERROR CHECK
    _depot_required = "//p[@id='wayne_id_Depot0-helper-text']"

    # Pop Up Windows

    _check_popUp = "//h2[normalize-space() = 'Do you want to create or edit the address?']"
    _edit_cancel_btn = "//button[normalize-space() = 'Cancel']"
    _edit_address_btn = "//button[normalize-space() = 'Edit Address'][@tabindex =0]"
    _edit_address_btn_r = "//button[normalize-space() = 'Edit Address'][@tabindex =55]"
    _edit_create_address_btn = "//button[normalize-space() = 'Create Address']"
    _addr_upadted_successfully = "//span[normalize-space() ='Address updated Successfully']"
    # error logs array
    _error_logs = []

    # sell rate fields
    _pn_f = False
    _nc_f = False
    _nc_clicked_gsr_enabled = False
    _nc_clicked_gsr_enabled2 = False
    _cancelled_status = ""
    _cs = False
    _sr_f = []

    def verifyNewConsignmentTitle(self):
        print('#' * 100)
        print("Express Cargo Ltd. | Consignment Form")
        print('#' * 100)
        self.waitForElement(self._connote, "xpath")
        time.sleep(2)
        return self.verifyPageTitle("Express Cargo Ltd. | Consignment Form")

    '''HEADER'''

    def enterConnote(self, connote):
        self.waitForElement(self._connote, "xpath")
        self.sendKeys(connote, self._connote, "xpath")

    def enterAccountName(self, accountName):
        self.waitForElement(self._account_name, "xpath")
        self.sendKeys(accountName, self._account_name, "xpath")
        an = self.getElement(self._account_name, "xpath")
        an.send_keys(Keys.ENTER)

    def enterStatus(self, status):
        self.sendKeys(status, self._status, "xpath")
        st = self.getElement(self._status, "xpath")
        if status == "ALLOCATED":
            st.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        st.send_keys(Keys.ENTER)

    def enterDateAllocated(self, dateAllocated):
        self.sendKeys(dateAllocated, self._date_allocated, "xpath")

    def enterCustomerRef(self, customerRef):
        if customerRef:
            self.sendKeys(customerRef, self._customer_ref, "xpath")

    def enterReceiverRef(self, receiverRef):
        if receiverRef:
            self.sendKeys(receiverRef, self._receiver_ref, "xpath")

    def enterDateReady(self, dateReady):
        if dateReady:
            self.sendKeys(dateReady, self._date_ready, "xpath")

    def enterEstimatedDeliveryDate(self, estDeliveryDate):
        if estDeliveryDate:
            self.sendKeys(estDeliveryDate, self._estimated_delivery_date, "xpath")

    def enterAssignedTo(self, assignedTo):
        if assignedTo:
            self.sendKeys(assignedTo, self._assigned_to, "xpath")
            at = self.getElement(self._assigned_to, "xpath")
            at.send_keys(Keys.ENTER)

    def enterPriorityLevel(self, priorityLevel):
        if priorityLevel:
            self.sendKeys(priorityLevel, self._priority_level, "xpath")
            pl = self.getElement(self._priority_level, "xpath")
            pl.send_keys(Keys.ENTER)

    def checkDataFetchedPopUp(self):
        self.waitForElement(self._data_fetched_popup, "xpath")
        print(self.getElement(self._data_fetched_popup, "xpath").text)
        if self.getElement(self._data_fetched_popup, "xpath").text == "Account Info Fetched":
            return True
        else:
            return False

    # connote accountName status dateAllocated customerRef receiverRef dateReady estDeliveryDate assignedTo priorityLevel

    def enterHeaderInformation(self, connote='', accountName='', status='', dateAllocated='', customerRef='',
                               receiverRef='',
                               dateReady='', estDeliveryDate='', assignedTo='', priorityLevel=''):
        self.enterConnote(connote)
        self.enterAccountName(accountName)
        self.enterStatus(status)
        self.enterDateAllocated(dateAllocated)
        self.enterCustomerRef(customerRef)
        self.enterReceiverRef(receiverRef)
        self.enterDateReady(dateReady)
        self.enterEstimatedDeliveryDate(estDeliveryDate)
        self.enterAssignedTo(assignedTo)
        self.enterPriorityLevel(priorityLevel)
        # if self.isElementPresent("//p[contains(normalize-space(), 'already exist')]", "xpath"):
        #     self.editConsignmentNumber()
        time.sleep(2)

    '''SENDER DETAILS'''


    def enterSenderAddress(self, senderNewAddress):
        if senderNewAddress:
            self.sendKeys(senderNewAddress, self._enter_addr_l, "xpath")
            sa = self.getElement(self._enter_addr_l, "xpath")
            sa.send_keys(Keys.ENTER)

    def editSenderCompany(self, senderCompanyName):
        # after filling the account name in HEADER values will be available due to api call
        # self.waitForElement(self._company_l, "xpath")
        # sce = self.getElement(self._company_l, "xpath")
        # self.elementClick("(//button[@title='Clear'])[5]", "xpath")
        self.elementClick(self._company_l, "xpath")
        self.driver.execute_script("arguments[0].value = ''", self.getElement(self._company_l, "xpath"))
        self.sendKeys(senderCompanyName, self._company_l, "xpath")
        sc = self.getElement(self._company_l, "xpath")
        sc.send_keys(Keys.ENTER)
        time.sleep(2)

    def checkSenderAddressType(self):
        self.waitForElement(self._addr_type_l, "xpath")
        addrtype_l = self.getElement(self._addr_type_l, "xpath")
        addrtypeText_l_input = addrtype_l.find_element(By.XPATH, "following-sibling::*[1]")
        _sender_ini_adrType = addrtypeText_l_input.get_attribute("value")
        print(_sender_ini_adrType)
        print(type(_sender_ini_adrType))
        if len(_sender_ini_adrType) > 0:
            return True
        else:
            return False

    def editSenderAddressType(self, addressType):  # index
        if addressType != '':
            self.waitForElement(self._addr_type_l, "xpath")
            addrtype_l = self.getElement(self._addr_type_l, "xpath")
            # addrtypeText_l = addrtype_l.get_attribute("value")
            addrtypeText_l_input = addrtype_l.find_element(By.XPATH, "following-sibling::*[1]")
            sender_ini_adrType = addrtypeText_l_input.get_attribute("value")
            if addressType == sender_ini_adrType:
                if addressType == 'RESIDENTIAL BUSINESS':
                    addressType = 'BUSINESS' if (random.randint(1, 2) == 1) else 'RESIDENTIAL'
                elif addressType == 'BUSINESS':
                    addressType = 'RESIDENTIAL BUSINESS' if (random.randint(1, 2) == 1) else 'RESIDENTIAL'
                else:
                    addressType = 'RESIDENTIAL BUSINESS' if (random.randint(1, 2) == 1) else 'BUSINESS'
            self.elementClick(self._addr_type_l, "xpath")
            time.sleep(3)
            self.waitForElement("//li[normalize-space()='" + addressType + "']/span", "xpath")
            self.elementClick("//li[normalize-space()='" + addressType + "']", "xpath")
            self.editPopUpWindow()
            time.sleep(5)

    def enterSenderLot(self, lot):
        if lot:
            self.sendKeys(lot, self._lot_l, "xpath")

    def checkSenderRoad(self):
        self.waitForElement(self._road_l, "xpath")
        road_l = self.getElement(self._road_l, "xpath")
        if road_l.is_displayed():
            roadText_l = road_l.get_attribute("value")
            _sender_ini_roadNo = roadText_l
            print(roadText_l)
            if type(roadText_l):
                return True
            else:
                return False
        else:
            return False

    def checkSenderStreet(self):
        self.waitForElement(self._street_l, "xpath")
        street_l = self.getElement(self._street_l, "xpath")
        if street_l.is_displayed():
            streetText_l = street_l.get_attribute("value")
            _sender_ini_street = streetText_l
            print(streetText_l)
            if streetText_l:
                return True
            else:
                return False
        else:
            return False

    def checkSenderSuburb(self):

        self.waitForElement(self._suburb_l, "xpath")
        suburb_l = self.getElement(self._suburb_l, "xpath")
        suburbText_l = suburb_l.get_attribute("value")
        print(suburbText_l)
        if suburb_l.is_displayed():
            return True
        else:
            return False

    def checkSenderCity(self):
        self.waitForElement(self._city_l, "xpath")
        city_l = self.getElement(self._city_l, "xpath")
        cityText_l = city_l.get_attribute("value")
        print(cityText_l)
        if city_l.is_displayed():
            return True
        else:
            return False

    def checkSenderState(self):
        self.waitForElement(self._state_l, "xpath")
        state_l = self.getElement(self._state_l, "xpath")
        stateText_l = state_l.get_attribute("value")
        print(stateText_l)
        if state_l.is_displayed():
            return True
        else:
            return False

    def checkSenderPostCode(self):
        self.waitForElement(self._post_code_l, "xpath")
        postcode_l = self.getElement(self._post_code_l, "xpath")
        time.sleep(3)
        postcodeText_l = postcode_l.get_attribute("value")
        print(int(postcodeText_l))
        # print(type(postcodeText_l))
        if postcode_l.is_displayed():
            return True
        else:
            return False

    def clickSenderForkLift(self, forkLift):
        if forkLift:
            self.waitForElement(self._forklift_l, "xpath")
            self.elementClick(self._forklift_l, "xpath")

    def clickSenderDriver(self, driver):
        if driver:
            self.waitForElement(self._driver_l, "xpath")
            self.elementClick(self._driver_l, "xpath")

    def enterSenderOpenTime(self, openTime):
        if openTime:
            self.waitForElement(self._open_time_l, "xpath")
            self.sendKeys(openTime, self._open_time_l, "xpath")

    def enterSenderClosedTime(self, closedtime):
        if closedtime:
            self.waitForElement(self._close_time_l, "xpath")
            self.sendKeys(self._close_time_l, "xpath")

    def enterSenderVehicle(self, vehicle):  #######
        if vehicle:
            self.waitForElement(self._vehicle_l, "xpath")
            self.sendKeys(self._vehicle_l, "xpath")
            ve = self.getElement(self._vehicle_l, "xpath")
            ve.send_keys(Keys.ENTER)

    def enterSenderVehicleType(self, vehicleType):
        if vehicleType:
            self.waitForElement(self._vehicle_type_l, "xpath")
            self.sendKeys(self._vehicle_type_l, "xpath")
            vt = self.getElement(self._vehicle_type_l, "xpath")
            vt.send_keys(Keys.ENTER)

    def enterSenderSpecialInstructions(self, specialInstructions):
        if specialInstructions:
            self.waitForElement(self._special_instruction_l)
            self.sendKeys(specialInstructions, self._special_instruction_l, "xpath")

    def checkSenderCharges(self):
        sch = self.getElement(self._charges_lst_f, "xpath").text
        print(sch)
        if sch != "":
            return True

    def enterSenderCharges(self, charges):
        if charges:
            self.waitForElement(self._charges_l, "xpath")
            self.sendKeys(charges, self._charges_l, "xpath")
            ch = self.getElement(self._charges_l, "xpath")
            ch.send_keys(Keys.ENTER)

    def createAddressSender(self):
        self.elementClick(self._create_addr_l, "xpath")

    def editSenderRoad(self, road):
        if road:
            self.waitForElement(self._road_l, "xpath")
            road_element = self.getElement(self._road_l, "xpath")
            self.elementClick(self._road_l, "xpath")
            road_val = self.getElement(self._road_l, "xpath").get_attribute("value")
            self.driver.execute_script("arguments[0].value = ''", road_element)
            print(10 * '#')
            print(road_val)
            print(10 * '#')
            self.elementClick(self._road_l, "xpath")
            self.sendKeys(road_val, self._road_l, "xpath")
            print(self.getElement(self._road_l, "xpath").get_attribute("value"))

    def enterSenderRoad(self, road):
        if road:
            self.waitForElement(self._road_l, "xpath")
            road_element = self.getElement(self._road_l, "xpath")
            self.elementClick(self._road_l, "xpath")
            self.driver.execute_script("arguments[0].value = ''", road_element)
            self.elementClick(self._road_l, "xpath")
            self.sendKeys(road, self._road_l, "xpath")
            print(self.getElement(self._road_l, "xpath").get_attribute("value"))

    def editSenderStreet(self, street):
        if street:
            self.waitForElement(self._street_l, "xpath")
            street_element = self.getElement(self._street_l, "xpath")
            self.elementClick(self._street_l, "xpath")
            time.sleep(2)
            street_val = self.getElement(self._street_l, "xpath").get_attribute("value")
            self.driver.execute_script("arguments[0].value = ''", street_element)
            self.elementClick(self._street_l, "xpath")
            self.sendKeys(street_val, self._street_l, "xpath")
            print(self.getElement(self._street_l, "xpath").get_attribute("value"))

    def enterSenderStreet(self, street):
        if street:
            self.waitForElement(self._street_l, "xpath")
            street_element = self.getElement(self._street_l, "xpath")
            self.elementClick(self._street_l, "xpath")
            time.sleep(2)
            self.driver.execute_script("arguments[0].value = ''", street_element)
            self.elementClick(self._street_l, "xpath")
            self.sendKeys(street, self._street_l, "xpath")
            print(self.getElement(self._street_l, "xpath").get_attribute("value"))

    def editSenderSuburb(self, suburb):
        if suburb:
            self.waitForElement(self.getElement(self._suburb_l, "xpath"))
            suburb_element = self.getElement(self._suburb_l, "xpath")
            self.elementClick(self._suburb_l, "xpath")
            suburb_val = self.getElement(self._suburb_l, "xpath").get_attribute("value")
            self.driver.execute_script("arguments[0].value = ''", suburb_element)
            self.elementClick(self._suburb_l, "xpath")
            self.sendKeys(suburb_val, self._suburb_l, "xpath")
            print(self.getElement(self._suburb_l, "xpath").get_attribute("value"))

    def enterSenderSuburb(self, suburb):
        if suburb:
            self.waitForElement(self.getElement(self._suburb_l, "xpath"))
            suburb_element = self.getElement(self._suburb_l, "xpath")
            self.elementClick(self._suburb_l, "xpath")
            self.driver.execute_script("arguments[0].value = ''", suburb_element)
            self.elementClick(self._suburb_l, "xpath")
            self.sendKeys(suburb, self._suburb_l, "xpath")
            print(self.getElement(self._suburb_l, "xpath").get_attribute("value"))

    def editSenderCity(self, city):
        if city:
            self.waitForElement(self._city_l, "xpath")
            city_element = self.getElement(self._city_l, "xpath")
            self.elementClick(self._city_l, "xpath")
            city_val = self.getElement(self._city_l, "xpath").get_attribute("value")
            self.driver.execute_script("arguments[0].value = ''", city_element)
            self.elementClick(self._city_l, "xpath")
            self.sendKeys(city_val, self._city_l, "xpath")
            print(self.getElement(self._city_l, "xpath").get_attribute("value"))

    def enterSenderCity(self, city):
        if city:
            self.waitForElement(self._city_l, "xpath")
            city_element = self.getElement(self._city_l, "xpath")
            self.elementClick(self._city_l, "xpath")
            self.driver.execute_script("arguments[0].value = ''", city_element)
            self.elementClick(self._city_l, "xpath")
            self.sendKeys(city, self._city_l, "xpath")
            print(self.getElement(self._city_l, "xpath").get_attribute("value"))

    def editSenderState(self, state):
        if state:
            self.waitForElement(self._state_l, "xpath")
            state_element = self.getElement(self._state_l, "xpath")
            self.elementClick(self._state_l, "xpath")
            state_val = self.getElement(self._state_l, "xpath").get_attribute("value")
            self.driver.execute_script("arguments[0].value = ''", state_element)
            self.elementClick(self._state_l, "xpath")
            self.sendKeys(state_val, self._state_l, "xpath")
            print(self.getElement(self._state_l, "xpath").get_attribute("value"))

    def enterSenderState(self, state):
        if state:
            self.waitForElement(self._state_l, "xpath")
            state_element = self.getElement(self._state_l, "xpath")
            self.elementClick(self._state_l, "xpath")
            self.driver.execute_script("arguments[0].value = ''", state_element)
            self.elementClick(self._state_l, "xpath")
            self.sendKeys(state, self._state_l, "xpath")
            print(self.getElement(self._state_l, "xpath").get_attribute("value"))

    def editSenderPostCode(self, postcode):
        if postcode:
            self.waitForElement(self._post_code_l, "xpath")
            postcode_element = self.getElement(self._post_code_l, "xpath")
            self.elementClick(self._post_code_l, "xpath")
            postcode_val = self.getElement(self._post_code_l, "xpath").get_attribute("value")
            self.driver.execute_script("arguments[0].value = ''", postcode_element)
            self.elementClick(self._post_code_l, "xpath")
            self.sendKeys(postcode_val, self._post_code_l, "xpath")
            print(self.getElement(self._post_code_l, "xpath").get_attribute("value"))

    def enterSenderPostCode(self, postcode):
        if postcode:
            self.waitForElement(self._post_code_l, "xpath")
            postcode_element = self.getElement(self._post_code_l, "xpath")
            self.elementClick(self._post_code_l, "xpath")
            self.driver.execute_script("arguments[0].value = ''", postcode_element)
            self.elementClick(self._post_code_l, "xpath")
            self.sendKeys(postcode, self._post_code_l, "xpath")
            print(self.getElement(self._post_code_l, "xpath").get_attribute("value"))

    def cancelPopUpWindow(self):
        self.waitForElement(self._check_popUp, "xpath")
        pw = self.getElement(self._check_popUp, "xpath")
        self.elementClick(self._edit_cancel_btn, "xpath")
        if pw:
            return True
        else:
            return False

    def editPopUpWindow(self):
        self.waitForElement(self._check_popUp, "xpath")
        pw = self.getElement(self._check_popUp, "xpath")
        self.elementClick(self._edit_address_btn, "xpath")
        if pw:
            return True
        else:
            return False

    def cancelSenderEditing(self, senderCompanyName, addressType, road, street, city, postcode):  # suburb, state,
        _r1 = True
        self.sendKeys(senderCompanyName, self._company_l, "xpath")
        _r1 = self.cancelPopUpWindow()
        self.sendKeys(addressType, self._addr_type_l, "xpath")
        _r1 = self.cancelPopUpWindow()
        self.sendKeys(road, self._road_l, "xpath")
        _r1 = self.cancelPopUpWindow()
        self.sendKeys(street, self._street_l, "xpath")
        _r1 = self.cancelPopUpWindow()
        self.sendKeys(city, self._city_l, "xpath")
        _r1 = self.cancelPopUpWindow()
        self.sendKeys(postcode, self._post_code_l, "xpath")
        _r1 = self.cancelPopUpWindow()
        return _r1

    def cancelReceiverEditing(self, senderCompanyName, addressType, road, street, city, postcode):  # suburb, state,
        _r1 = False
        self.sendKeys(senderCompanyName, self._company_r, "xpath")
        _r1 = self.cancelPopUpWindow()
        self.sendKeys(addressType, self._addr_type_r, "xpath")
        _r1 = self.cancelPopUpWindow()
        self.sendKeys(road, self._road_l, "xpath")
        _r1 = self.cancelPopUpWindow()
        self.sendKeys(street, self._street_r, "xpath")
        _r1 = self.cancelPopUpWindow()
        self.sendKeys(city, self._city_r, "xpath")
        _r1 = self.cancelPopUpWindow()
        self.sendKeys(postcode, self._post_code_r, "xpath")
        _r1 = self.cancelPopUpWindow()
        return _r1

    def editSenderDetailsCompanyNameAndCheckRequiredFields(self, senderCompanyName):
        _r1 = False
        self.sendKeys("a", self._company_l, "xpath")
        self.editPopUpWindow()
        self.editSenderCompany(senderCompanyName=senderCompanyName)
        _r1 = self.checkSenderAddressType()
        _r1 = self.checkSenderRoad()
        _r1 = self.checkSenderStreet()
        _r1 = self.checkSenderCity()
        _r1 = self.checkSenderPostCode()
        if _r1:
            return True
        else:
            return False

    def editSenderDetails(self, addressType, road, street, city, state, postcode):  #
        _r1 = False
        _es = False
        self.editSenderAddressType(addressType=addressType)  # select type
        time.sleep(3)
        self.editSenderRoad(road=road)
        _r1 = self.checkSenderStreet()
        if not _r1:
            self.log.error("### Street Field Error")
        self.editSenderStreet(street=street)
        _r1 = self.checkSenderCity()
        if not _r1:
            self.log.error("### City Field Error")
        self.editSenderCity(city=city)
        _r1 = self.checkSenderState()
        if not _r1:
            self.log.error("### State Field Error")
        self.editSenderState(state=state)
        _r1 = self.checkSenderPostCode()
        if not _r1:
            self.log.error("### PostCode Field Error")
        self.editSenderPostCode(postcode=postcode)
        self.waitForElement(self._create_addr_l, "xpath")
        cab = self.getElement(self._create_addr_l, "xpath")

        if cab is None:
            self.log.error("### EDIT ADDRESS BUTTON NOT FOUND!!!")
        if cab is not None and cab.is_enabled():
            self.elementClick(self._create_addr_l, "xpath")
            _es = self.isElementPresent("//div[1]/div[1]/div[1][normalize-space()='Address updated Successfully']",
                                        "xpath")
        if not _es:
            self.log.info("### Receiver Address Not Edited!!!")
        if _r1 and _es:
            return True
        else:
            return False

    def editReceiverDetailsCompanyName(self, receiverCompanyName):
        _r1 = False
        self.sendKeys("a", self._company_r, "xpath")
        self.editPopUpWindow()
        self.enterReceiverCompany(receiverCompanyName)
        _r1 = self.checkReceiverAddressType()
        _r1 = self.checkReceiverRoad()
        _r1 = self.checkReceiverStreet()
        _r1 = self.checkReceiverCity()
        _r1 = self.checkReceiverPostCode()
        if _r1:
            return True
        else:
            return False

    def editReceiverDetails(self, addressType, road, street, city, state, postcode):  #
        _r1 = False
        _es = False
        # _r2 = False
        self.editReceiverAddressType(addressType=addressType)  # select type
        time.sleep(3)
        self.editReceiverRoad(road=road)
        _r1 = self.checkReceiverStreet()
        if not _r1:
            self.log.error("### Street Field Error")
        self.editReceiverStreet(street=street)
        _r1 = self.checkReceiverCity()
        if not _r1:
            self.log.error("### City Field Error")
        self.editReceiverCity(city=city)
        _r1 = self.checkReceiverState()
        if not _r1:
            self.log.error("### State Field Error")
        self.editReceiverState(state=state)
        _r1 = self.checkReceiverPostCode()
        if not _r1:
            self.log.error("### PostCode Field Error")
        self.editReceiverPostCode(postcode=postcode)
        # #
        self.waitForElement(self._edit_address_btn_r, "xpath")
        cab = self.getElement(self._edit_address_btn_r, "xpath")

        if cab is None:
            self.log.error("### CREATE ADDRESS BUTTON NOT FOUND!!!")
        if cab is not None and cab.is_enabled():
            self.elementClick(self._edit_address_btn_r, "xpath")
            _es = self.isElementPresent("//div[1]/div[1]/div[1][normalize-space()='Address updated Successfully']",
                                        "xpath")
        if not _es:
            self.log.error("### Receiver Address Not Edited!!!")
        if _r1 and _es:  #
            return True
        else:
            return False

    # addrTy, Road, Street, City, State, PostCode
    def enterSenderDetails(self, senderNewAddress='', senderCompanyName='', lot='', forkLift='', driver='', openTime='',
                           closedtime='', vehicle="",
                           vehicleType='', specialInstructions='', charges=''):
        self.enterSenderAddress(senderNewAddress)
        self.editSenderCompany(senderCompanyName)
        self.enterSenderLot(lot)
        self.clickSenderForkLift(forkLift)
        self.clickSenderDriver(driver)
        self.enterSenderOpenTime(openTime)
        self.enterSenderClosedTime(closedtime)
        self.enterSenderVehicle(vehicle)
        self.enterSenderVehicleType(vehicleType)
        self.enterSenderSpecialInstructions(specialInstructions)
        self.enterSenderCharges(charges)

    '''RECEIVER DETAILS'''

    def editReceiverRoad(self, road):
        if road:
            self.waitForElement(self._road_r, "xpath")
            road_element = self.getElement(self._road_r, "xpath")
            self.elementClick(self._road_r, "xpath")
            road_val = self.getElement(self._road_r, "xpath").get_attribute("value")
            self.driver.execute_script("arguments[0].value = ''", road_element)
            print(road_val)
            self.elementClick(self._road_r, "xpath")
            self.sendKeys(road_val, self._road_r, "xpath")
            print(self.getElement(self._road_r, "xpath").get_attribute("value"))

    def enterReceiverRoad(self, road):
        if road:
            self.waitForElement(self._road_r, "xpath")
            road_element = self.getElement(self._road_r, "xpath")
            self.elementClick(self._road_r, "xpath")
            self.driver.execute_script("arguments[0].value = ''", road_element)
            self.sendKeys(road, self._road_r, "xpath")
            print(self.getElement(self._road_r, "xpath").get_attribute("value"))

    def editReceiverStreet(self, street):
        if street:
            self.waitForElement(self._street_r, "xpath")
            street_element = self.getElement(self._street_r, "xpath")
            self.elementClick(self._street_r, "xpath")
            time.sleep(2)
            street_val = self.getElement(self._street_r, "xpath").get_attribute("value")
            self.driver.execute_script("arguments[0].value = ''", street_element)
            self.elementClick(self._street_r, "xpath")
            self.sendKeys(street_val, self._street_r, "xpath")
            print(self.getElement(self._street_r, "xpath").get_attribute("value"))

    def enterReceiverStreet(self, street):
        if street:
            self.waitForElement(self._street_r, "xpath")
            street_element = self.getElement(self._street_r, "xpath")
            self.elementClick(self._street_r, "xpath")
            self.driver.execute_script("arguments[0].value = ''", street_element)
            self.sendKeys(street, self._street_r, "xpath")
            print(self.getElement(self._street_r, "xpath").get_attribute("value"))

    def enterReceiverCompany(self, receiverCompanyName):
        self.elementClick(self._company_r, "xpath")
        self.driver.execute_script("arguments[0].value = ''", self.getElement(self._company_r, "xpath"))
        self.sendKeys(receiverCompanyName, self._company_r, "xpath")
        sc = self.getElement(self._company_r, "xpath")
        sc.send_keys(Keys.ENTER)

    def editReceiverCity(self, city):
        if city:
            self.waitForElement(self._city_r, "xpath")
            city_element = self.getElement(self._city_r, "xpath")
            self.elementClick(self._city_r, "xpath")
            city_val = self.getElement(self._city_r, "xpath").get_attribute("value")
            self.driver.execute_script("arguments[0].value = ''", city_element)
            self.elementClick(self._city_r, "xpath")
            self.sendKeys(city_val, self._city_r, "xpath")
            print(self.getElement(self._city_r, "xpath").get_attribute("value"))

    def enterReceiverCity(self, city):
        if city:
            self.waitForElement(self._city_r, "xpath")
            city_element = self.getElement(self._city_r, "xpath")
            self.elementClick(self._city_r, "xpath")
            self.driver.execute_script("arguments[0].value = ''", city_element)
            self.sendKeys(city, self._city_r, "xpath")
            print(self.getElement(self._city_r, "xpath").get_attribute("value"))

    def editReceiverState(self, state):
        if state:
            self.waitForElement(self._state_r, "xpath")
            state_element = self.getElement(self._state_r, "xpath")
            self.elementClick(self._state_r, "xpath")
            state_val = self.getElement(self._state_r, "xpath").get_attribute("value")
            self.driver.execute_script("arguments[0].value = ''", state_element)
            self.elementClick(self._state_r, "xpath")
            self.sendKeys(state_val, self._state_r, "xpath")
            print(self.getElement(self._state_r, "xpath").get_attribute("value"))

    def enterReceiverState(self, state):
        if state:
            self.waitForElement(self._state_r, "xpath")
            state_element = self.getElement(self._state_r, "xpath")
            self.elementClick(self._state_r, "xpath")
            self.driver.execute_script("arguments[0].value = ''", state_element)
            self.sendKeys(state, self._state_r, "xpath")
            print(self.getElement(self._state_r, "xpath").get_attribute("value"))

    def editReceiverPostCode(self, postcode):
        if postcode:
            self.waitForElement(self._post_code_r, "xpath")
            postcode_element = self.getElement(self._post_code_r, "xpath")
            self.elementClick(self._post_code_r, "xpath")
            postcode_val = self.getElement(self._post_code_r, "xpath").get_attribute("value")
            self.driver.execute_script("arguments[0].value = ''", postcode_element)
            self.elementClick(self._post_code_r, "xpath")
            self.sendKeys(postcode_val, self._post_code_r, "xpath")
            print(self.getElement(self._post_code_r, "xpath").get_attribute("value"))

    def enterReceiverPostCode(self, postcode):
        if postcode:
            self.waitForElement(self._post_code_r, "xpath")
            postcode_element = self.getElement(self._post_code_r, "xpath")
            self.elementClick(self._post_code_r, "xpath")
            self.driver.execute_script("arguments[0].value = ''", postcode_element)
            self.sendKeys(postcode, self._post_code_r, "xpath")
            print(self.getElement(self._post_code_r, "xpath").get_attribute("value"))

    def enterReceiverAddress(self, receiverNewAddress):
        if receiverNewAddress:
            self.sendKeys(receiverNewAddress, self._enter_addr_r, "xpath")
            ra = self.getElement(self._enter_addr_r, "xpath")
            ra.send_keys(Keys.ENTER)

    def enterReceiverDetailsCompanyName(self, senderCompanyName):
        self.waitForElement(self._company_r, "xpath")
        self.sendKeys(senderCompanyName, self._company_r, "xpath")
        rc = self.getElement(self._company_r, "xpath")
        rc.send_keys(Keys.ENTER)

    def checkReceiverAddressType(self):
        self.waitForElement(self._addr_type_r, "xpath")
        addrtype_r = self.getElement(self._addr_type_r, "xpath")
        addrtypeText_r_input = addrtype_r.find_element(By.XPATH, "following-sibling::*[1]")
        _sender_ini_adrType = addrtypeText_r_input.get_attribute("value")
        print(_sender_ini_adrType)
        print(type(_sender_ini_adrType))
        if addrtype_r.is_displayed():
            return True
        else:
            return False

    def editReceiverAddressType(self, addressType):
        if addressType:
            self.waitForElement(self._addr_type_r, "xpath")
            addrtype_r = self.getElement(self._addr_type_r, "xpath")
            addrtypeText_r_input = addrtype_r.find_element(By.XPATH, "following-sibling::*[1]")
            receiver_ini_adrType = addrtypeText_r_input.get_attribute("value")
            if addressType == receiver_ini_adrType:
                if addressType == 'RESIDENTIAL BUSINESS':
                    addressType = 'BUSINESS' if (random.randint(1, 2) == 1) else 'RESIDENTIAL'
                elif addressType == 'BUSINESS':
                    addressType = 'RESIDENTIAL BUSINESS' if (random.randint(1, 2) == 1) else 'RESIDENTIAL'
                else:
                    addressType = 'RESIDENTIAL BUSINESS' if (random.randint(1, 2) == 1) else 'BUSINESS'
            self.elementClick(self._addr_type_r, "xpath")
            time.sleep(3)
            self.waitForElement("//li[normalize-space()='" + addressType + "']/span", "xpath")
            self.elementClick("//li[normalize-space()='" + addressType + "']", "xpath")
            self.editPopUpWindow()
            time.sleep(5)

    def enterReceiverAddressType(self, addressType):
        if addressType:
            self.waitForElement(self._addr_type_r, "xpath")
            addrtype_r = self.getElement(self._addr_type_r, "xpath")
            self.elementClick(self._addr_type_r, "xpath")
            time.sleep(3)
            self.waitForElement("//li[normalize-space()='" + addressType + "']/span", "xpath")
            self.elementClick("//li[normalize-space()='" + addressType + "']", "xpath")
            self.editPopUpWindow()

    def enterReceiverLot(self, lot):
        if lot:
            self.sendKeys(lot, self._lot_r, "xpath")

    def checkReceiverRoad(self):
        self.waitForElement(self._road_r, "xpath")
        road_r = self.getElement(self._road_r, "xpath")
        roadText_r = road_r.get_attribute("value")
        if road_r.is_displayed():
            return True
        else:
            return False

    def checkReceiverStreet(self):
        self.waitForElement(self._street_r, "xpath")
        street_r = self.getElement(self._street_r, "xpath")
        streetText_r = street_r.get_attribute("value")
        if street_r.is_displayed():
            return True
        else:
            return False

    def checkReceiverSuburb(self):
        self.waitForElement(self._suburb_r, "xpath")
        suburb_r = self.getElement(self._suburb_r, "xpath")
        suburbText_r = suburb_r.get_attribute("value")
        if suburb_r.is_displayed():
            return True
        else:
            return False

    def checkReceiverCity(self):
        self.waitForElement(self._city_r, "xpath")
        city_r = self.getElement(self._city_r, "xpath")
        cityText_r = city_r.get_attribute("value")
        if city_r.is_displayed():
            return True
        else:
            return False

    def checkReceiverState(self):
        self.waitForElement(self._state_r, "xpath")
        state_r = self.getElement(self._state_r, "xpath")
        stateText_r = state_r.get_attribute("value")
        if state_r.is_displayed():
            return True
        else:
            return False

    def checkReceiverPostCode(self):
        self.waitForElement(self._post_code_r, "xpath")
        postcode_r = self.getElement(self._post_code_r, "xpath")
        postcodeText_r = postcode_r.get_attribute("value")
        if postcode_r.is_displayed():
            return True
        else:
            return False

    def clickReceiverForkLift(self, forkLift):
        if forkLift:
            self.elementClick(self._forklift_r, "xpath")

    def clickReceiverDriver(self, driver):
        if driver:
            self.elementClick(self._driver_r, "xpath")

    def enterReceiverOpenTime(self, openTime):
        if openTime:
            self.waitForElement(self._open_time_r, "xpath")
            self.sendKeys(openTime, self._open_time_r, "xpath")

    def enterReceiverClosedTime(self, closedtime):
        if closedtime:
            self.waitForElement(self._close_time_r, "xpath")
            self.sendKeys(self._close_time_r, "xpath")

    def enterReceiverVehicle(self, vehicle):
        if vehicle:
            self.waitForElement(self._vehicle_r, "xpath")
            self.sendKeys(self._vehicle_r, "xpath")
            ve = self.getElement(self._vehicle_r, "xpath")
            ve.send_keys(Keys.ENTER)

    def enterReceiverVehicleType(self, vehicleType):
        if vehicleType:
            self.waitForElement(self._vehicle_type_r, "xpath")
            self.sendKeys(self._vehicle_type_r, "xpath")
            vt = self.getElement(self._vehicle_type_r, "xpath")
            vt.send_keys(Keys.ENTER)

    def checkReceiverSpecialInstructions(self):

        if len(self.getElement(self._special_instruction_r, "xpath").text) > 0:
            return True

    def enterReceiverSpecialInstructions(self, spectialInstructions):
        if spectialInstructions:
            self.sendKeys(spectialInstructions, self._special_instruction_r, "xpath")

    def checkReceiverCharges(self):
        rch = self.getElement(self._charges_lst_f, "xpath").text
        print(rch)
        if rch != "":
            return True

    def enterReceiverCharges(self, charges):
        if charges:
            self.waitForElement(self._charges_r, "xpath")
            self.sendKeys(charges, self._charges_r, "xpath")

    # senderNewAddress senderCompanyName lot forkLift driver openTime closedtime vehicle vehicleType spectialInstructions charges

    def createAddressReceiver(self):
        self.elementClick(self._create_addr_r, "xpath")

    def enterReceiverDetails(self, receiverNewAddress='', receiverCompanyName='', lot='', forkLift='', driver='',
                             openTime='', closedtime='', vehicle='',
                             vehicleType='', specialInstructions='', charges=''):
        self.enterReceiverAddress(receiverNewAddress)
        self.enterReceiverDetailsCompanyName(receiverCompanyName)
        self.enterReceiverLot(lot)
        self.clickReceiverForkLift(forkLift)
        self.clickReceiverDriver(driver)
        self.enterReceiverOpenTime(openTime)
        self.enterReceiverClosedTime(closedtime)
        self.enterReceiverVehicle(vehicle)
        self.enterReceiverVehicleType(vehicleType)
        self.enterReceiverSpecialInstructions(specialInstructions)
        self.enterReceiverCharges(charges)
        # address creation is not needed
        # self.createAddressReceiver()

    '''Sender Contact Details'''

    def enterSenderFirstName(self, firstName):
        self.waitForElement(self._first_name_l, "xpath")
        self.sendKeys(firstName, self._first_name_l, "xpath")

    def enterSenderLastName(self, lastName):
        if lastName:
            self.waitForElement(self._last_name_l, "xpath")
            self.sendKeys(self._last_name_l, "xpath")

    def enterSenderEmail(self, email):
        self.waitForElement(self._email_l, "xpath")
        self.sendKeys(email, self._email_l, "xpath")

    def enterSenderPhoneNumber(self, phoneNumber):
        self.waitForElement(self._phone_number_l, "xpath")
        self.sendKeys(phoneNumber, self._phone_number_l, "xpath")

    def enterSenderMobileNumber(self, mobileNumber):
        if mobileNumber:
            self.waitForElement(self._mobile_number_l, "xpath")
            self.sendKeys(mobileNumber, self._mobile_number_l, "xpath")

    def enterSenderRole(self, role):
        self.waitForElement(self._role_l, "xpath")
        self.sendKeys(role, self._role_l, "xpath")

    def createSenderContact(self):
        self.elementClick(self._create_contact_l)

    def enterSenderContactDetails(self, firstName='', lastName='', email='', phoneNumber='', mobileNumber='', role=''):
        self.enterSenderFirstName(firstName)
        self.enterSenderLastName(lastName)
        self.enterSenderEmail(email)
        self.enterSenderPhoneNumber(phoneNumber)
        self.enterSenderMobileNumber(mobileNumber)
        self.enterSenderRole(role)
        time.sleep(2)
        self.createSenderContact()

    '''Receiver Contact Details'''

    def enterReceiverFirstName(self, firstName):
        self.waitForElement(self._first_name_r, "xpath")
        self.sendKeys(firstName, self._first_name_r, "xpath")

    def enterReceiverLastName(self, lastName):
        if lastName:
            self.waitForElement(self._last_name_r, "xpath")
            self.sendKeys(self._last_name_r, "xpath")

    def enterReceiverEmail(self, email):
        self.waitForElement(self._email_r, "xpath")
        self.sendKeys(email, self._email_r, "xpath")

    def enterReceiverPhoneNumber(self, phoneNumber):
        self.waitForElement(self._phone_number_r, "xpath")
        self.sendKeys(phoneNumber, self._phone_number_r, "xpath")

    def enterReceiverMobileNumber(self, mobileNumber):
        if mobileNumber:
            self.waitForElement(self._mobile_number_r, "xpath")
            self.sendKeys(mobileNumber, self._mobile_number_r, "xpath")

    def enterReceiverRole(self, role):
        self.waitForElement(self._role_r, "xpath")
        self.sendKeys(role, self._role_r, "xpath")

    def createReceiverContact(self):
        self.elementClick(self._create_contact_r)

    def enterReceiverContactDetails(self, firstName='', lastName='', email='', phoneNumber='', mobileNumber='',
                                    role=''):
        self.enterReceiverFirstName(firstName)
        self.enterReceiverLastName(lastName)
        self.enterReceiverEmail(email)
        self.enterReceiverPhoneNumber(phoneNumber)
        self.enterReceiverMobileNumber(mobileNumber)
        self.enterReceiverRole(role)
        time.sleep(2)
        self.createReceiverContact()

    '''CONSIGNMENT LINES'''

    # weight and dimension units are select form type, and all after dangerous goods are ids

    def enterServices_1(self,
                        services):  # input type- aria descendant,, USE KEYS ARROW DOWN, need to change code for that
        self.waitForElement(self._services1, "xpath")
        self.elementClick(self._services1, "xpath")
        services_element = self.getElement(self._services1, "xpath")
        if services == 'ECONOMY':
            # self.sendKeys(services, self._services1, "xpath")
            self.driver.execute_script("arguments[0].value = '" + services + "'", services_element)
            self.action.send_keys(Keys.ARROW_DOWN)
            services_element.send_keys(Keys.ENTER)
        self.sendKeys(services, self._services1, "xpath")
        serv = self.getElement(self._services1, "xpath")
        serv.send_keys(Keys.ENTER)

    def enterWeightUnit_1(self, weightUnit):  # select type
        if weightUnit:
            self.waitForElement(self._weight_unit1, "xpath")
            self.sendKeys(weightUnit, self._weight_unit1, "xpath")

    def enterDimensionUnit_1(self, dunit):  # select type
        if dunit:
            self.waitForElement(self._dimension_unit1, "xpath")
            self.sendKeys(dunit, self._dimension_unit1, "xpath")

    def enterContainerNumber_1(self, containerNumber):
        if containerNumber:
            self.waitForElement(self._container_number1, "xpath")
            self.sendKeys(containerNumber, self._container_number1, "xpath")

    def enterAgency_1(self, agency):
        pass

    def enterItem_1(self, item):
        self.waitForElement(self._item1, "xpath")
        self.sendKeys(item, self._item1, "xpath")
        it1 = self.getElement(self._item1, "xpath")
        it1.send_keys(Keys.ENTER)

    def enterCommodity_1(self, commodity):
        self.elementClick(self._commodity1, "xpath")
        self.sendKeys(commodity, self._commodity1, "xpath")
        cm1 = self.getElement(self._commodity1, "xpath")
        cm1.send_keys(Keys.ENTER)

    def enterDescription_1(self, description):
        if description:
            self.waitForElement(self._description1, "xpath")
            self.sendKeys(description, self._description1, "xpath")

    def enterQuantity_1(self, quantity):
        self.waitForElement(self._quantity1, "xpath")
        self.sendKeys(quantity, self._quantity1, "xpath")

    def enterWeight_1(self, weight):
        self.waitForElement(self._weight1, "xpath")
        self.sendKeys(weight, self._weight1, "xpath")

    def enterVolume_1(self, volume):
        self.waitForElement(self._volume1, "xpath")
        self.sendKeys(volume, self._volume1, "xpath")

    def enterLength_1(self, length):
        if length:
            self.waitForElement(self._length1, "xpath")
            self.sendKeys(length, self._length1, "xpath")

    def enterWidth_1(self, width):
        if width:
            self.waitForElement(self._width1, "xpath")
            self.sendKeys(width, self._width1, "xpath")

    def enterHeight_1(self, height):
        if height:
            self.waitForElement(self._height1, "xpath")
            self.sendKeys(height, self._height1, "xpath")

    def clickDangerousGoods_1(self, dg):
        if dg:
            self.waitForElement(self._dg1, "xpath")
            self.elementClick(self._dg1)

    def clickAddLine(self):
        self.elementClick(self._add_line_btn, "xpath")

    def enterItem_2(self, item):
        if item:
            self.waitForElement(self._item2, "xpath")
            self.sendKeys(item, self._item2, "xpath")
            it2 = self.getElement(self._item2, "xpath")
            it2.send_keys(Keys.ENTER)

    def enterCommodity_2(self, commodity):
        if commodity:
            self.waitForElement(self._commodity2, "xpath")
            self.elementClick(self._commodity2, "xpath")
            self.sendKeys(commodity, self._commodity2, "xpath")
            cmd2 = self.getElement(self._commodity2, "xpath")
            cmd2.send_keys(Keys.ENTER)
            time.sleep(2)

    def enterDescription_2(self, description):
        if description:
            self.sendKeys(description, self._description2, "xpath")

    def enterQuantity_2(self, quantity):
        if quantity:
            self.waitForElement(self._quantity2, "xpath")
            self.sendKeys(quantity, self._quantity2, "xpath")

    def enterWeight_2(self, weight):
        if weight:
            self.waitForElement(self._weight2, "xpath")
            self.sendKeys(weight, self._weight2, "xpath")

    def enterVolume_2(self, volume):
        if volume:
            self.waitForElement(self._volume2, "xpath")
            self.sendKeys(volume, self._volume2, "xpath")

    def enterLength_2(self, length):
        if length:
            self.waitForElement(self._length2, "xpath")
            self.sendKeys(length, self._length2, "xpath")

    def enterWidth_2(self, width):
        if width:
            self.waitForElement(self._width2, "xpath")
            self.sendKeys(width, self._width2, "xpath")

    def enterHeight_2(self, height):
        if height:
            self.waitForElement(self._height2, "xpath")
            self.sendKeys(height, self._height2, "xpath")

    def clickDangerousGoods_2(self, dg):
        if dg:
            self.waitForElement(self._dg2, "xpath")
            self.elementClick(self._dg2)

    def findTotalLines(self):
        self.waitForElement(self._total_lines)
        tl = self.getElement(self._total_lines)
        totalLines = int(tl.text)
        return totalLines

    def findTotalItemCount(self):
        self.waitForElement(self._total_item_count)
        tic = self.getElement(self._total_item_count)
        totalItemCount = int(tic.text)
        return totalItemCount

    def findTotalWeight(self):
        self.waitForElement(self._total_weight)
        tw = self.getElement(self._total_weight)
        reg_res = re.findall(r'\b\d+\.\d+\b', tw.text)
        print(reg_res[0])
        res = round(float(reg_res[0]), 3)
        return res

    def findTotalVolume(self): #'[\d\.\d]+'
        time.sleep(3)
        self.waitForElement(self._total_volume)
        tv = self.getElement(self._total_volume)
        reg_res = re.findall(r'\b\d+\.\d+\b', tv.text)
        print(reg_res[0])
        res = round(float(reg_res[0]), 3)
        return res

    def enterConsignmentLine_1(self, services1, item1, commodity1, quantity1, weight1,
                               volume1):  # , weightUnit1, dunit1, containerNumber1, agency1, description1, length1, width1, height1, dg1
        self.enterServices_1(services1)
        # self.enterWeightUnit_1(weightUnit1)
        # self.enterDimensionUnit_1(dunit1)
        # self.enterContainerNumber_1(containerNumber1)
        # self.enterAgency_1(agency1)
        self.enterItem_1(item1)
        self.enterCommodity_1(commodity1)
        time.sleep(2)
        # self.enterDescription_1(description1)
        self.enterQuantity_1(quantity1)
        self.enterWeight_1(weight1)
        self.enterVolume_1(volume1)
        # self.enterLength_1(length1)
        # self.enterWidth_1(width1)
        # self.enterHeight_1(height1)
        # self.clickDangerousGoods_1(dg1)

    def enterConsignmentLine_2(self, item2,
                               commodity2,
                               quantity2, weight2, volume2,
                               ):  # containerNumber2, agency2,  description2, length2, width2, height2, dg2
        if commodity2:
            self.clickAddLine()
        self.enterItem_2(item2)
        self.enterCommodity_2(commodity2)
        # self.enterDescription_2(description2)
        self.enterQuantity_2(quantity2)
        self.enterWeight_2(weight2)
        self.enterVolume_2(volume2)
        # self.enterLength_2(length2)
        # self.enterWidth_2(width2)
        # self.enterHeight_2(height2)
        # self.clickDangerousGoods_2(dg2)

    def checkServicesField(self):
        self.waitForElement(self._services1, "xpath")
        serv = self.getElement(self._services1, "xpath")
        addrtypeText_r = serv.get_attribute("value")
        if serv.is_displayed():
            return True
        else:
            self.log.error("### Services Field is not filled!!!")
            return False

    def checkItem1(self):
        self.waitForElement(self._item1, "xpath")
        it1 = self.getElement(self._item1, "xpath")
        addrtypeText_r = it1.get_attribute("value")
        if it1.is_displayed():
            return True
        else:
            self.log.error("### Item 1 Field is not filled!!!")
            return False

    def checkItem2(self):
        self.waitForElement(self._item2, "xpath")
        it2 = self.getElement(self._item2, "xpath")
        addrtypeText_r = it2.get_attribute("value")
        if it2.is_displayed():
            return True
        else:
            self.log.error("### Item 2 Field is not filled!!!")
            return False

    def checkCommodity1(self):
        self.waitForElement(self._commodity1, "xpath")
        cm1 = self.getElement(self._commodity1, "xpath")
        addrtypeText_r = cm1.get_attribute("value")
        if cm1.is_displayed():
            return True
        else:
            self.log.error("### Commodity 1 Field is not filled!!!")
            return False

    def checkCommodity2(self):
        self.waitForElement(self._commodity2, "xpath")
        cm2 = self.getElement(self._commodity2, "xpath")
        addrtypeText_r = cm2.get_attribute("value")
        if cm2.is_displayed():
            return True
        else:
            self.log.error("### Commodity 2 Field is not filled!!!")
            return False

    def checkQuantity1(self):
        self.waitForElement(self._quantity1, "xpath")
        qu1 = self.getElement(self._quantity1, "xpath")
        addrtypeText_r = qu1.get_attribute("value")
        if qu1.is_displayed():
            return True
        else:
            self.log.error("### Quantity 1 Field is not filled!!!")
            return False

    def checkQuantity2(self):
        self.waitForElement(self._quantity2, "xpath")
        qu2 = self.getElement(self._quantity2, "xpath")
        addrtypeText_r = qu2.get_attribute("value")
        if qu2.is_displayed():
            return True
        else:
            self.log.error("### Quantity 2 Field is not filled!!!")
            return False

    def checkWeight1(self):
        self.waitForElement(self._weight1, "xpath")
        wt1 = self.getElement(self._weight1, "xpath")
        addrtypeText_r = wt1.get_attribute("value")
        if wt1.is_displayed():
            return True
        else:
            self.log.error("### Weight 1 Field is not filled!!!")
            return False

    def checkWeight2(self):
        self.waitForElement(self._weight2, "xpath")
        wt2 = self.getElement(self._weight2, "xpath")
        ddrtypeText_r = wt2.get_attribute("value")
        if wt2.is_displayed():
            return True
        else:
            self.log.error("### Weight 2 Field is not filled!!!")
            return False

    def checkVolume1(self):
        self.waitForElement(self._volume1, "xpath")
        vol1 = self.getElement(self._volume1, "xpath")
        addrtypeText_r = vol1.get_attribute("value")
        if vol1.is_displayed():
            return True
        else:
            self.log.error("### Volume 1 Field is not filled!!!")
            return False

    def checkVolume2(self):
        self.waitForElement(self._volume2, "xpath")
        vol2 = self.getElement(self._volume2, "xpath")
        addrtypeText_r = vol2.get_attribute("value")
        if vol2.is_displayed():
            return True
        else:
            self.log.error("### Volume 2 Field is not filled!!!")
            return False

    def checkWeighUnit(self):
        self.waitForElement(self._weight_unit1, "xpath")
        wu = self.getElement(self._weight_unit1, "xpath")
        wu_input = wu.find_element(By.XPATH, "following-sibling::*[1]")
        wu_val = wu_input.get_attribute("value")
        if wu_val == "KG":
            return True
        else:
            self.log.error("### Weight Unit is Not Correct!!!")
            return False

    def checkVolumeUnit(self):
        self.waitForElement(self._dimension_unit1, "xpath")
        vu = self.getElement(self._dimension_unit1, "xpath")
        vu_input = vu.find_element(By.XPATH, "following-sibling::*[1]")
        vu_val = vu_input.get_attribute("value")
        if vu_val == "MM":
            return True
        else:
            self.log.error("### Dimension Unit is Not Correct!!!")
            return False

    def checkRequiredFieldsCL(self):
        _res = True
        _res = self.checkServicesField()
        _res = self.checkWeighUnit()
        _res = self.checkVolumeUnit()
        _res = self.checkItem1()
        _res = self.checkCommodity1()
        _res = self.checkQuantity1()
        _res = self.checkWeight1()
        _res = self.checkVolume1()
        if not self.isElementPresent("//strong[normalize-space()=2]", "xpath"):
            return _res
        _res = self.checkItem2()
        _res = self.checkCommodity2()
        _res = self.checkQuantity2()
        _res = self.checkWeight2()
        _res = self.checkVolume2()
        return _res

    def calctotalItemD(self):
        pass

    def calctotalweight(self):
        sum = 0.000
        wt = self.getElement(self._weight1, "xpath").get_attribute("value")
        qu = self.getElement(self._quantity1, "xpath").get_attribute("value")
        wt = float(wt)
        wt_f = "{:.3f}".format(wt)
        sum = sum + round(float(wt_f), 3)
        sum = sum * int(qu)

        print(int(qu))
        if self.isElementPresent(self._weight2, "xpath"):
            wt2 = self.getElement(self._weight2, "xpath").get_attribute("value")
            Wt2 = round(float(wt2), 3)
            qu2 = self.getElement(self._quantity2, "xpath").get_attribute("value")
            sum = round(sum + (Wt2 * int(qu2)), 3)
            print(Wt2, int(qu2))
        sum = round(sum, 3)
        print(sum)
        return sum

    def calctotalvolume(self):
        v_sum = 0.000
        rr = 0.000
        vol = self.getElement(self._volume1, "xpath").get_attribute("value")
        qu = self.getElement(self._quantity1, "xpath").get_attribute("value")
        res1 = v_sum + round(float(vol), 3)
        sum = res1 * int(qu)
        sum = round(sum, 3)
        print("Sum ", sum)
        if self.isElementPresent(self._weight2, "xpath"):
            vl = self.getElement(self._volume2, "xpath").get_attribute("value")
            vol2 = round(float(vl), 3)
            qu2 = self.getElement(self._quantity2, "xpath").get_attribute("value")
            rr = round(vol2 * int(qu2), 3)
            print("rr ", rr)
        res = sum + rr
        res = round(res, 3)
        print("res", res)
        time.sleep(3)
        return res

    def totalWeightVerification(self):
        actualVal = self.calctotalweight()
        time.sleep(2)
        expectedVal = self.findTotalWeight()
        print(actualVal, expectedVal)
        verval = self.verifyValues(actualVal, expectedVal)
        return verval

    def totalVolumeVerification(self):
        actualVal = self.calctotalvolume()
        self.elementClick("//strong[normalize-space()=2]", "xpath")
        expectedVal = self.findTotalVolume()
        print(actualVal, expectedVal)
        verval = self.verifyValues(expectedVal, actualVal)
        return verval

    'LEGGING'

    def enterDate(self, date):
        if date:
            self.waitForElement(self._date1, "xpath")
            self.sendKeys(self._date1, "xpath")

    def enterCarrier1(self, carrier):
        if self.isElementPresent("//strong[normalize-space()=2]", "xpath"):
            self.waitForElement(self._carrier1, "xpath")
            it1 = self.getElement(self._carrier1, "xpath")
            self.sendKeys(carrier, self._carrier1, "xpath")
            it1.send_keys(Keys.ENTER)
        else:
            self.waitForElement("//input[@id='wayne_id_Carrier0']", "xpath")
            it1 = self.getElement("//input[@id='wayne_id_Carrier0']", "xpath")
            self.sendKeys(carrier, "//input[@id='wayne_id_Carrier0']", "xpath")
            it1.send_keys(Keys.ENTER)

    def enterCarrier2(self, carrier):
        if self.isElementPresent(self._carrier2, "xpath"):
            self.waitForElement(self._carrier2, "xpath")
            self.sendKeys(carrier, self._carrier2, "xpath")
            ca2 = self.getElement(self._carrier2, "xpath")
            ca2.send_keys(Keys.ENTER)


    def enterDepot1(self, depot):
        if depot:
            if self.isElementPresent("//strong[normalize-space()=2]", "xpath"):
                self.waitForElement(self._depot1, "xpath")
                de1 = self.getElement(self._depot1, "xpath")
                self.elementClick(self._depot1, "xpath")
                self.sendKeys(depot, self._depot1, "xpath")
                de1.send_keys(Keys.ENTER)
            else:
                self.waitForElement("//input[@id='wayne_id_Depot0']", "xpath")
                de1 = self.getElement("//input[@id='wayne_id_Depot0']", "xpath")
                self.elementClick(self._depot1, "xpath")
                self.sendKeys(depot, self._depot1, "xpath")
                de1.send_keys(Keys.ENTER)

    def enterDepot2(self, depot):
        if depot:
            self.waitForElement(self._depot2, "xpath")
            self.elementClick(self._depot2, "xpath")
            self.sendKeys(depot, self._depot2, "xpath")
            de2 = self.getElement(self._depot2, "xpath")
            de2.send_keys(Keys.ENTER)

    def enterType1(self):  # select type
        if self.isElementPresent("//strong[normalize-space()=2]", "xpath"):
            self.waitForElement(self._type1, "xpath")
            self.elementClick(self._type1, "xpath")
            # selecting PU/LH/DL
            time.sleep(2)
            self.elementClick("//div[@id='menu-']/div[3]/ul/li[7]", "xpath")
        else:
            self.elementClick("//div[@id='wayne_id_type0']", "xpath")
            # selecting PU/LH/DL
            time.sleep(2)
            self.elementClick("//div[@id='menu-']/div[3]/ul/li[7]", "xpath")

    def enterType2(self):  # select type
        if self.isElementPresent("wayne_id_Collection Date1"):
            self.waitForElement(self._type2, "xpath")
            self.elementClick(self._type2, "xpath")
            time.sleep(2)
            # selecting PU/LH/DL, no way to automate selecting; not select type
            self.elementClick("//div[@id='menu-']/div[3]/ul/li[7]", "xpath")

    def enterFrom1(self, frm):
        if self.isElementPresent("//strong[normalize-space()=2]", "xpath"):
            self.waitForElement(self._from1, "xpath")
            self.sendKeys(frm, self._from1, "xpath")
            fr1 = self.getElement(self._from1, "xpath")
            fr1.send_keys(Keys.ENTER)
        else:
            self.waitForElement("//input[@id='wayne_id_from0']", "xpath")
            self.sendKeys(frm, "//input[@id='wayne_id_from0']", "xpath")
            fr1 = self.getElement("//input[@id='wayne_id_from0']", "xpath")
            fr1.send_keys(Keys.ENTER)

    def enterFrom2(self, frm):
        if frm:
            self.waitForElement(self._from2, "xpath")
            self.sendKeys(frm, self._from2, "xpath")
            fr1 = self.getElement(self._from2, "xpath")
            fr1.send_keys(Keys.ENTER)

    def enterTo1(self, to):  # returning when the source and destination locations are same in LEGGING 1
        if self.isElementPresent("//strong[normalize-space()=2]", "xpath"):
            self.waitForElement(self._to1, "xpath")
            self.sendKeys(to, self._to1, "xpath")
            frm = self.getElement(self._from1, "xpath").get_attribute("value")
            if frm == to:
                self.log.error("### Source and Destination can't be same!!!")
                return
            to1 = self.getElement(self._to1, "xpath")
            to1.send_keys(Keys.ENTER)
        else:
            self.waitForElement("//input[@id='wayne_id_to0']", "xpath")
            self.sendKeys(to, self._to1, "xpath")
            frm = self.getElement(self._from1, "xpath").get_attribute("value")
            if frm == to:
                self.log.error("### Source and Destination can't be same!!!")
                return
            to1 = self.getElement(self._to1, "xpath")
            to1.send_keys(Keys.ENTER)


    def enterTo2(self, to):
        if to:
            self.waitForElement(self._to2, "xpath")
            self.sendKeys(to, self._to2, "xpath")
            frm = self.getElement(self._from2, "xpath").get_attribute("value")
            if frm == to:
                self.log.error("### Source and Destination can't be same!!!")
                return
            to1 = self.getElement(self._to2, "xpath")
            to1.send_keys(Keys.ENTER)

    def enterCarrierRef1(self, carrRef):
        if carrRef:
            if self.isElementPresent("//strong[normalize-space()=2]", "xpath"):
                self.waitForElement(self._carrier_ref1,"xpath")
                self.sendKeys(carrRef, self._carrier_ref1, "xpath")
                cr1 = self.getElement(self._carrier_ref1, "xpath")
                cr1.send_keys(Keys.ENTER)
            else:
                self.waitForElement("//input[@id = 'wayne_id_carrier Reference0']", "xpath")
                self.sendKeys(carrRef, "//input[@id = 'wayne_id_carrier Reference0']", "xpath")
                cr1 = self.getElement("//input[@id = 'wayne_id_carrier Reference0']", "xpath")
                cr1.send_keys(Keys.ENTER)

    def enterCarrierRef2(self, carrRef):
        if carrRef:
            self.waitForElement(self._carrier_ref2)
            self.sendKeys(carrRef, self._carrier_ref2, "xpath")
            cr1 = self.getElement(self._carrier_ref2, "xpath")
            cr1.send_keys(Keys.ENTER)

    def entercarrierInvoice1(self, carrInv):
        if carrInv:
            if self.isElementPresent("//strong[normalize-space()=2]", "xpath"):
                self.waitForElement(self._carrier_invoice1, "xpath")
                self.sendKeys(carrInv, self._carrier_invoice1, "xpath")
                ci1 = self.getElement(self._carrier_invoice1, "xpath")
                ci1.send_keys(Keys.ENTER)
            else:
                self.waitForElement("//input[@id='wayne_id_carrier invoice0']", "xpath")
                self.sendKeys(carrInv, "//input[@id='wayne_id_carrier invoice0']", "xpath")
                ci1 = self.getElement("//input[@id='wayne_id_carrier invoice0']", "xpath")
                ci1.send_keys(Keys.ENTER)

    def entercarrierInvoice2(self, carrInv):
        if carrInv:
            self.waitForElement(self._carrier_invoice2, "xpath")
            self.sendKeys(carrInv, self._carrier_invoice2, "xpath")
            ci1 = self.getElement(self._carrier_invoice2, "xpath")
            ci1.send_keys(Keys.ENTER)

    def enterCost1(self, cost):
        if cost:
            if self.isElementPresent("//strong[normalize-space()=2]","xpath"):
                self.waitForElement(self._cost1, "xpath")
                self.sendKeys(cost, self._cost1, "xpath")
                co1 = self.getElement(self._cost1, "xpath")
                co1.send_keys(Keys.ENTER)
            else:
                self.waitForElement("//input[@id='wayne_id_cost0']", "xpath")
                self.sendKeys(cost, "//input[@id='wayne_id_cost0']", "xpath")
                co1 = self.getElement("//input[@id='wayne_id_cost0']", "xpath")
                co1.send_keys(Keys.ENTER)

    def enterCost2(self, cost):
        if cost:
            self.waitForElement(self._cost2, "xpath")
            self.sendKeys(cost, self._cost2, "xpath")
            co1 = self.getElement(self._cost2, "xpath")
            co1.send_keys(Keys.ENTER)

    # enter description if any
    def enterCostMore1(self, costmore):
        if costmore:
            self.waitForElement(self._cost_more1, "xpath")
            self.elementClick(self._cost_more1, "xpath")
            self.waitForElement(self._cost_more1_desc, "xpath")
            self.elementClick(self._cost_more1_desc, "xpath")
            self.sendKeys(costmore, self._cost_more1_desc, "xpath")
            cancel_btn_fc = self.getElement("//*/text()[normalize-space(.)='CLOSE']/parent::*",
                                            "xpath")  # following-sibling::*[1]
            # print(self.isElementPresent(cancel_btn_fc.find_element(By.XPATH, "following-sibling::*[1]")), "xpath")
            # cb = cancel_btn_fc.find_element(By.XPATH, "following-sibling::*[1]")
            # print(self.getElement(self._cost_more1_desc, "xpath").get_attribute("value"))
            self.elementClick("//*/text()[normalize-space(.)='CLOSE']/parent::*", "xpath")

    def enterCostMore2(self, costmore):
        if costmore:
            self.waitForElement(self._cost_more2, "xpath")
            self.elementClick(self._cost_more2, "xpath")
            self.waitForElement(self._cost_more2_desc, "xpath")
            self.elementClick(self._cost_more2_desc, "xpath")
            self.sendKeys(costmore, self._cost_more2_desc, "xpath")
            print(self.getElement(self._cost_more2_desc, "xpath").get_attribute("value"))
            self.elementClick(self._cost_more2_cancel_btn, "xpath")

    def checkCostMore1(self):
        self.waitForElement(self._cost_more1, "css")
        self.elementClick(self._cost_more1, "css")
        cm = self.getElement("(wayne_id_Note Description)[2]", "xpath")
        cmText = cm.text
        return cmText

    def checkCostMore2(self):
        self.waitForElement(self._cost_more2, "xpath")
        self.elementClick(self._cost_more2, "xpath")
        cm = self.getElement("(wayne_id_Note Description)[4]", "xpath")
        cmText = cm.text
        return cmText

    def verifyCostMore(self):
        pass

    def clickAddLeg(self):
        self.elementClick(self._add_leg_btn)

    # date carrier depot type frm to carrRef carrInv cost
    def enterLegging_1(self, carrier1, depot1, frm1, to1, cost1, cn1):  # date1,  carrRef1, carrInv1
        # self.enterDate(date1)
        self.enterCarrier1(carrier1)
        self.enterDepot1(depot1)
        self.enterType1()
        self.enterFrom1(frm1)
        self.enterTo1(to1)
        # self.enterCarrierRef1(carrRef1)
        # self.entercarrierInvoice1(carrInv1)
        self.enterCost1(cost1)
        self.enterCostMore1(cn1)

    def enterLegging_2(self, carrier2, depot2, frm2, to2, cost2, cn2):
        if carrier2:
            self.clickAddLeg()
        # self.enterDate(date2)
        self.enterCarrier2(carrier2)
        self.enterDepot2(depot2)
        self.enterType2()
        self.enterFrom2(frm2)
        self.enterTo2(to2)
        # self.enterCarrierRef2(carrRef2)
        # self.entercarrierInvoice2(carrInv2)
        self.enterCost2(cost2)
        self.enterCostMore2(cn2)

    def checkCarrier1(self):
        self.waitForElement(self._carrier1, "xpath")
        it1 = self.getElement(self._carrier1, "xpath")
        addrtypeText_r = it1.get_attribute("value")
        if it1.is_displayed():
            print(True)
            return True
        else:
            self.log.error("### Carrier 1 Field is not filled!!!")
            return False

    def checkCarrier2(self):
        self.waitForElement(self._carrier2, "xpath")
        it1 = self.getElement(self._carrier2, "xpath")
        addrtypeText_r = it1.get_attribute("value")
        if it1.is_displayed():
            print(True)
            return True
        else:
            self.log.error("### Carrier 2 Field is not filled!!!")
            return False

    def checkType1(self):
        self.waitForElement(self._type1, "xpath")
        it1 = self.getElement(self._type1, "xpath")
        addrtypeText_r = it1.get_attribute("value")
        if it1.is_displayed():
            print(True)
            return True
        else:
            self.log.error("### Type 1 Field is not filled!!!")
            return False

    def checkType2(self):
        self.waitForElement(self._type2, "xpath")
        it1 = self.getElement(self._type2, "xpath")
        addrtypeText_r = it1.get_attribute("value")
        if it1.is_displayed():
            print(True)
            return True
        else:
            self.log.error("### Type 2 Field is not filled!!!")
            return False

    def checkFrom1(self):
        self.waitForElement(self._from1, "xpath")
        it1 = self.getElement(self._from1, "xpath")
        addrtypeText_r = it1.get_attribute("value")
        if it1.is_displayed():
            print(True)
            return True
        else:
            self.log.error("### From 1 Field is not filled!!!")
            return False

    def checkFrom2(self):
        self.waitForElement(self._from2, "xpath")
        it1 = self.getElement(self._from2, "xpath")
        addrtypeText_r = it1.get_attribute("value")
        if it1.is_displayed():
            print(True)
            return True
        else:
            self.log.error("### From 1 Field is not filled!!!")
            return False

    def checkTo1(self):
        self.waitForElement(self._to1, "xpath")
        it1 = self.getElement(self._to1, "xpath")
        addrtypeText_r = it1.get_attribute("value")
        if it1.is_displayed():
            print(True)
            return True
        else:
            self.log.error("### To 1 Field is not filled!!!")
            return False

    def checkTo2(self):
        self.waitForElement(self._to2, "xpath")
        it1 = self.getElement(self._to2, "xpath")
        addrtypeText_r = it1.get_attribute("value")
        if it1.is_displayed():
            print(True)
            return True
        else:
            self.log.error("### To 2 Field is not filled!!!")
            return False

    def checkCost1(self):
        self.waitForElement(self._cost1, "xpath")
        it1 = self.getElement(self._cost1, "xpath")
        addrtypeText_r = it1.get_attribute("value")
        if it1.is_displayed():
            print(True)
            return True
        else:
            self.log.error("### Cost 1 Field is not filled!!!")
            return False

    def checkCost2(self):
        self.waitForElement(self._cost2, "xpath")
        it1 = self.getElement(self._cost2, "xpath")
        addrtypeText_r = it1.get_attribute("value")
        if it1.is_displayed():
            print(True)
            return True
        else:
            self.log.error("### Cost 2 Field is not filled!!!")
            return False

    def checkRequiredFieldsLG(self):
        _res = False
        _res = self.checkCarrier1()
        _res = self.checkType1()
        _res = self.checkFrom1()
        _res = self.checkTo1()
        if not self.isElementPresent(self._carrier2, "xpath"):
            self.log.info("## No other LEGGINGS!!")
            print("##############")
            print(_res)
            print("##############")
            return _res
        _res = self.checkCarrier2()
        _res = self.checkType2()
        _res = self.checkFrom2()
        _res = self.checkTo2()
        _res = self.checkCost2()
        return _res

    ## check legging notes are different or not, indiv.leggings from and to are different or not
    def checkLeggingNotes(self):
        cm1 = self.checkCostMore1()
        cm2 = self.checkCostMore2()
        if cm1 == cm2:
            self.log.debug("### The Leggings' Notes are same")
            return False
        return True

    def checkLeggingFromTo1(self):
        self.waitForElement(self._from1, "xpath")
        fr = self.getElement(self._from1, "xpath").get_attribute("value")
        print("########")
        print(fr)
        print("########")
        self.waitForElement(self._to1, "xpath")
        to = self.getElement(self._to1, "xpath").get_attribute("value")
        print("########")
        print(to)
        print("########")
        if fr == to:
            self.log.error("### From and To places are same for Legging 1")
            return False
        else:
            self.log.info("Source and Destination of LEGGING 1 are different")
            return True

    def checkLeggingFromTo2(self):
        self.waitForElement(self._from2, "xpath")
        fr = self.getElement(self._from2, "xpath").get_attribute("value")
        print("########")
        print(fr)
        print("########")
        self.waitForElement(self._to2, "xpath")
        to = self.getElement(self._to2, "xpath").get_attribute("value")
        print("########")
        print(to)
        print("########")
        if fr == to:
            self.log.error("### From and To places are same for Legging 2")
            return False
        else:
            self.log.info("Source and Destination of LEGGING 2 are different")
            return True

    def findTotalLegs(self):
        self.waitForElement(self._total_legs)
        tl = self.getElement(self._total_legs)
        reg_res = re.findall(r'\b\d+\.\d+\b', tl.text)
        print(reg_res[0])
        res = int(reg_res[0])
        return res

    def calctotalleggingcost(self):
        sum = 0.00
        self.waitForElement(self._cost1, "xpath")
        lc = self.getElement(self._cost1, "xpath").get_attribute("value")
        sum = round(sum + round(float(lc), 2), 2)
        if self.isElementPresent(self._cost2, "xpath"):
            lc2 = self.getElement(self._cost2, "xpath").get_attribute("value")
            Lc2 = round(float(lc2), 2)
            sum = round(sum + Lc2, 2)
            print(Lc2)
        print("leggings sum", sum)
        return sum

    def findTotalLeggingCost(self):
        self.waitForElement(self._total_legging_cost)
        tlc = self.getElement(self._total_legging_cost)
        reg_res = re.findall(r'\b\d+\.\d+\b', tlc.text)
        print(reg_res[0])
        res = round(float(reg_res[0]), 2)
        print("Found_leggings_cost", res)
        return res

    def verifyTotalLeggingCost(self):
        actualVal = self.calctotalleggingcost()
        expectedVal = self.findTotalLeggingCost()
        print(expectedVal, actualVal)
        verval = self.verifyValues(actualVal, expectedVal)
        return verval

    '''SELL RATING'''

    def checkSRGenerated(self):
        self.waitForElement(self._general_sell_rate)
        if self.getElement(self._general_sell_rate).is_enabled():
            self.log.info("### Sell Rate Not generated!!!")
            self.enterSellRating()
            return False
        else:
            tsr = self.getElement(self._total_sell_rate, "xpath").get_attribute("value")
            print(tsr)
            if tsr == "0.0": # or tsr is None
                self.log.info("### Sell Rate value is 0.0!!!")
                return True
            else:
                # print(tsr)
                self.log.info("Sell Rate generated!!!")
                val2 = True
                return val2

    def clickGenerateSR(self):
        self.waitForElement(self._general_sell_rate)
        if self.getElement(self._general_sell_rate).is_enabled():
            self.elementClick(self._general_sell_rate)
        if self.isElementPresent("//*/text()[normalize-space(.)='Rate calculated successfully']/parent::*", "xpath"):
            self.log.info("Sell Rate Generated!!!")
        else:
            self.log.info("### Sell Rate Not Generated!!!")
            self._error_logs.append("### Sell Rate Not Generated!!!")
        if self.isElementPresent("//*[contains(normalize-space(text()), 'No location found')]/parent::*", "xpath"):
            self.log.info("### No Location Found Error ....")
            self._error_logs.append("### No Location Found Error ....")
        if self.isElementPresent("//*[contains(normalize-space(text()), 'Customer')]/parent::*", "xpath"):
            self.log.info("### Customer Error ....")
            self._error_logs.append("### Customer Error ....")
        if self.isElementPresent("//*[contains(normalize-space(text()), 'General')]/parent::*", "xpath"):
            self.log.info("### General Error ....")
            self._error_logs.append("### General Error ....")

    def returnErrorLogs(self):
        # [self.log.error(i)for i in self._error_logs]
        return self._error_logs

    def clickTotalSRBtn(self):
        self.elementClick(self._total_sr_btn, "xpath")
        self.elementClick(self._total_sr_cancel_btn, "xpath")

    def enterQuotedPrice(self, quotedPrice):
        if quotedPrice:
            self.waitForElement(self._quoted_price, "xpath")
            self.elementClick(self._quoted_price, "xpath")
            self.sendKeys(quotedPrice, self._quoted_price, "xpath")

    def enterQuotedBy(self, quotedBy):
        if quotedBy:
            self.waitForElement(self._quoted_by, "xpath")
            self.elementClick(self._quoted_by, "xpath")
            self.sendKeys(quotedBy, self._quoted_by, "xpath")
            qb = self.getElement(self._quoted_by, "xpath")
            qb.send_keys(Keys.ENTER)

    def clickNoCharge(self, noCharge):
        if noCharge:
            self.elementClick(self._no_charge)
            self._nc_f = self.isElementPresent(
                "(.//*[normalize-space(text()) and normalize-space(.)='Close'])[4]/following::span[1]", "xpath")
            if not self._nc_f:
                self.log.error("### First Charge Note is Required - Not Working!!!")
            self._sr_f.append(self._nc_f)
            self.waitForElement("//textarea[@id='wayne_id_NO CHARGE NOTES']", "xpath") # _no_charge_desc = "//textarea[@id='wayne_id_NO CHARGE NOTES']"
            self.elementClick("//textarea[@id='wayne_id_NO CHARGE NOTES']", "xpath")
            self.sendKeys(noCharge, "//textarea[@id='wayne_id_NO CHARGE NOTES']", "xpath")
            self.elementClick("//*/text()[normalize-space(.)='Save']/parent::*", "xpath")
            self.elementClick("(.//*[normalize-space(text()) and normalize-space(.)='Save'])[1]/following::button[1]",
                              "xpath")
            self._nc_clicked_gsr_enabled = self.getElement(
                "//div[@id='root']/div/main/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div/button", "xpath").is_enabled()
            if self._nc_clicked_gsr_enabled:
                self.log.error("### GSR must be disabled when no charge is ACTIVE!!!")
            self._sr_f.append(not self._nc_clicked_gsr_enabled)
            print(10*"#")
            print(not self._nc_clicked_gsr_enabled)
            print(10*"#")
            self.elementClick(self._no_charge)

    def clickPricingNotes(self, pricingNotes):
        if pricingNotes:
            self.elementClick(self._pricing_notes)
            self._pn_f = self.isElementPresent(
                "(.//*[normalize-space(text()) and normalize-space(.)='Close'])[4]/following::span[1]", "xpath")
            if not self._pn_f:
                self.log.error("###First Pricing Note is Required - Not Working!!!")
            self.elementClick("//textarea[@id='wayne_id_Pricing Notes']", "xpath")
            self.sendKeys(pricingNotes, "//textarea[@id='wayne_id_Pricing Notes']", "xpath")
            self.elementClick("//*/text()[normalize-space(.)='Save']/parent::*", "xpath")
            self.elementClick("(.//*[normalize-space(text()) and normalize-space(.)='Save'])[1]/following::button[1]",
                              "xpath")

    def clickCancelled(self, cancelled):
        if cancelled:
            if self.getElement(self._general_sell_rate).is_enabled(): # self._general_sell_rate
                self.elementClick(self._general_sell_rate)
                time.sleep(2)
            _cs = False
            # self.waitForElement(self._cancelled)
            self.elementClick(self._cancelled)
            self.waitForElement("//div[normalize-space()='Are you sure to cancel this consignment?']", "xpath")
            self.elementClick("//button[@id='wayne_id_YES']", "xpath")
            self._nc_clicked_gsr_enabled2 = self.getElement(self._general_sell_rate).is_enabled()
            if self._nc_clicked_gsr_enabled2:
                self.log.error("### GSR must be disabled when Consignment is CANCELLED!!")
            self._sr_f.append(not self._nc_clicked_gsr_enabled2)
            print(10*"#")
            print(not self._nc_clicked_gsr_enabled2)
            print(10*"#")
            self._cancelled_status = self.getElement(self._status, "xpath").get_attribute("value")
            if self._cancelled_status == "CANCELLED":
                self._cs = True
            else:
                self.log.error("### STATUS didn't change to CANCELLED!!!")
            self._sr_f.append(self._cs)
            self.elementClick(self._cancelled)
            time.sleep(2)
            self.waitForElement("//div[normalize-space()='Are you sure to not cancel this consignment?']", "xpath")
            time.sleep(2)
            self.elementClick("//button[@id='wayne_id_YES']", "xpath")
            time.sleep(1)
            self.elementClick(self._general_sell_rate)

    # connote anSR quotedPrice noCharge pricingNotes cancelled
    def checkGSR(self):
        _gs = self.getElement(
            "//div[@id='root']/div/main/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div/button", "xpath").is_enabled()
        return _gs

    def enterSellRating(self):
        self.clickGenerateSR()

    def enterSellRateFields(self, quotedPrice, noCharge, quotedBy, pricingNotes, cancelled):
        self.enterQuotedPrice(quotedPrice)
        self.enterQuotedBy(quotedBy)
        self.clickPricingNotes(pricingNotes)
        self.clickNoCharge(noCharge)
        self.clickCancelled(cancelled)

    def checkSellRateFields(self):
        return self._sr_f

    '''ADDITIONAL INFORMATION'''

    def enterInsurance(self, insurance):
        if insurance:
            select_element = Select(self.getElement(self._insurance, "xpath"))
            options = select_element.options
            for option in options:
                if insurance == option.text:
                    select_element.select_by_visible_text(insurance)
                    print(option.text, insurance)

    def checkInsurance(self):
        select_element = self.getElement(self._insurance, "xpath")
        val = select_element.get_attribute("value")
        if val is not None:
            print(val)
            self.log.info("Insurance Field is Filled!!")
            return True
        else:
            self.log.info("### Insurance Field is EMPTY!!!")
            return False

    def clickAuthorityToLeave(self, atl):
        if atl:
            self.waitForElement("//div[2]/div/div/div/div/textarea", "xpath")
            self.elementClick(self._authority_to_leave, "xpath")
            self.sendKeys("//div[2]/div/div/div/div/textarea", "xpath")
            self.elementClick("//button[@id='wayne_id_Close']/span", "xpath")

    def clickDangerousGoodsAI(self, dgAI):
        if dgAI:
            self.elementClick(self._dangerous_goods_ai, "xpath")

    def clickPodUploaded(self, podUploaded):
        if podUploaded:
            self.elementClick(self._pod_uploaded, "xpath")

    def clickChristellNotes(self, christellNotes):
        if christellNotes:
            self.elementClick(self._christell_notes, "xpath")
            self.waitForElement("//div[2]/div/div/div/div/textarea", "xpath")
            self.sendKeys(christellNotes, "//div[2]/div/div/div/div/textarea", "xpath")
            self.elementClick("//button[@id='wayne_id_Add Notes']/span", "xpath")
            self.elementClick("//div[3]/div/div[3]/button/span", "xpath")

    def enterSpecialInstructionsDescription(self, si):
        if si:
            self.elementClick(self._special_instruction_ai, "xpath")
            self.sendKeys(si, self._special_instruction_ai, "xpath")

    def clickGeneralDocuments(self, genDoc):
        pass

    # insurance atl dgAI podUploaded christellNotes si

    def enterAdditionalInformation(self, insurance, atl, dgAI, podUploaded, christellNotes, si):
        if insurance is not None:
            if not self.checkInsurance():
                self.enterInsurance(insurance)
        self.clickAuthorityToLeave(atl)
        self.clickDangerousGoodsAI(dgAI)
        self.clickPodUploaded(podUploaded)
        self.clickChristellNotes(christellNotes)
        self.enterSpecialInstructionsDescription(si)

    '''FOOTERS'''

    def findTotalCharge(self):
        self.waitForElement(self._total_charge)
        tc = self.getElement(self._total_charge)
        ttlCharge = int(tc.text)
        return ttlCharge

    def findTotalCost(self):
        self.waitForElement(self._total_cost)
        tcost = self.getElement(self._total_cost)
        ttlCost = int(tcost.text)
        return ttlCost

    def findGrossMargin(self):
        self.waitForElement(self._gross_margin)
        gm = self.getElement(self._gross_margin)
        gMargin = int(gm.text)
        return gMargin

    def findGrossMarginPercentage(self):
        self.waitForElement(self._gross_margin_percentage)
        gmp = self.getElement(self._gross_margin_percentage)
        gmPercent = int(gmp.text)
        return gmPercent

    def clickCreateConsignment(self):
        self.waitForElement(self._create_consignment, "xpath")
        ccb = self.getElement(self._create_consignment, "xpath")
        if self.isElementPresent(self._create_consignment, "xpath"):
            self.elementClick(self._create_consignment, "xpath")
            time.sleep(3)
            cc = self.verifyPageTitle("Express Cargo Ltd. | Consignment Form")
            if cc:
                self.log.info("CONSIGNMENT CREATED!!!")
                return True
            else:
                self.log.error("### ERROR IN CONSIGNMENT CREATION!!!!")
                return False
        else:
            return False

    def editConsignmentNumber(self):
        print("inside editing connote number")
        con_tag = self.getElement(self._connote, "xpath")
        con_tag_value = con_tag.get_attribute("value")
        trimmed_value = con_tag_value.rstrip()
        new_value = ''.join(random.sample(trimmed_value, len(trimmed_value)))
        time.sleep(3)
        print(new_value)
        con_tag.send_keys(Keys.CONTROL + "a")
        con_tag.send_keys(new_value)
        time.sleep(1)
        self.elementClick(self._connote, "xpath")
        time.sleep(2)
        print(trimmed_value, new_value)
        cn_val = self.getElement(self._connote, "xpath").get_attribute("value")
        print(cn_val)

    def clickSaveDraft(self):
        self.elementClick(self._save_draft)
