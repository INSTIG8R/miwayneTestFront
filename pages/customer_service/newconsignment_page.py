import re
import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains


class NewConsignmentPage(BasePage):
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

    _data_fetched_popup = "//span[normalize-space()='Account Data Fetched']"

    # Sender Details

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
    _create_addr_l = "//button[@tabindex='35'][@id = 'wayne_id_Create Address']"  ##Not Used



## checked upto this should access


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
    _create_addr_r = "//button[@tabindex='60']/span[normalize-space()='EDIT ADDRESS']" ##Not Used

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
    _item1 = "//input[@tabindex='75'][@id ='wayne_id_Item']"
    _commodity1 = "//input[@tabindex='76'][@id ='wayne_id_Commodity']"
    _description1 = "//input[@tabindex='77'][@id ='wayne_id_Description']"
    _quantity1 = "//input[@tabindex='78'][@id ='wayne_id_Quantity']"
    _weight1 = "//input[@tabindex='79'][@id ='wayne_id_Weight']"
    _volume1 = "//input[@tabindex='80'][@id ='wayne_id_Volume']"
    _length1 = "//input[@tabindex='81'][@id ='wayne_id_Length']"
    _width1 = "//input[@tabindex='82'][@id='wayne_id_Width']"
    _height1 = "//input[@tabindex='83'][@id ='wayne_id_Height']"
    _dg1 = "//input[@tabindex='84']"
    _add_line_btn = "wayne_id_Add line"
    _total_lines = "wayne_id_Total lines"
    _total_item_count = "wayne_id_Total item count"
    _total_weight = "wayne_id_Total weight"
    _total_volume = "wayne_id_Total volume"

    _item2 = "//input[@tabindex='89'][@id='wayne_id_Item']"
    _commodity2 = "//input[@tabindex='90'][@id='wayne_id_Commodity']"
    _description2 = "//input[@tabindex='91'][@id='wayne_id_Description']"
    _quantity2 = "//input[@tabindex='92'][@id='wayne_id_Quantity']"
    _weight2 = "//input[@tabindex='93'][@id='wayne_id_Weight']"
    _volume2 = "//input[@tabindex='94'][@id='wayne_id_Volume']"
    _length2 = "//input[@tabindex='95'][@id='wayne_id_Length']"
    _width2 = "//input[@tabindex='96'][@id='wayne_id_Width']"
    _height2 = "//input[@tabindex='97'][@id='wayne_id_Height']"
    _dg2 = "//input[@tabindex='98'][@id='wayne_id_DANGEROUS GOODS?']"

    # delete button
    _delete_line_one = "//button[@tabindex = 88]"
    _delete_line_two = "button[@tabindex = 102]"

    _date1 = "//input[@tabindex = 112]"
    _carrier1 = "//input[@tabindex='113'][@id='wayne_id_Carrier0']" # //div[@id='root']/div/main/div[2]/div[3]/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/input"
    _depot1 = "//input[@tabindex = 114][@id='wayne_id_Depot0']" #  //div[@id='root']/div/main/div[2]/div[3]/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div[3]/div/div/div/input
    _type1 = "//div[@tabindex = 115][@id='wayne_id_type0']" #  //div[@id='root']/div/main/div[2]/div[3]/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div[4]/div/div/select
    _from1 = "//input[@tabindex = 116][@id='wayne_id_from0']" #  //div[@id='root']/div/main/div[2]/div[3]/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div[5]/div/div/div/input
    _to1 = "//input[@tabindex = 117][@id='wayne_id_to0']" #   //div[@id='root']/div/main/div[2]/div[3]/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div[6]/div/div/div/input
    _carrier_ref1 = "//input[@tabindex = 118][@id='wayne_id_carrier Reference0']" #  //div[2]/div/div[2]/div/div/div[7]/div/div/input
    _carrier_invoice1 = "//input[@tabindex = 119][@id='wayne_id_carrier invoice0']" #  //div[2]/div/div[2]/div/div/div[8]/div/div/input
    _cost1 = "//input[@tabindex = 120][@id='wayne_id_cost0']" #   //div[9]/div/div/div/div/input
    _cost_more1 = "//span[@tabindex = 121][@id='Legging Notes0']" #  //div[9]/div/div[2]/button

    _cost_more1_desc = "//div[2]/div/div/div/div/textarea" # //textarea[@tabindex = 121]
    _cost_more1_cancel_btn="//button[@id='wayne_id_Close']/span" # wayne_id_CLOSE
    _add_leg_btn = "wayne_id_Add leg"

    _total_legs = "wayne_id_Total legs"
    _total_legging_cost = "wayne_id_Total cost"

    # 2nd leg
    _date2 = "//input[@id = 'wayne_id_Collection Date']"
    _carrier2 = "//div[@id='root']/div/main/div[2]/div[3]/div[2]/div/div/div/div/div[3]/div/div[2]/div/div/div[2]/div/div/div/input" #  //input[@tabindex = 126]
    _depot2 = "//div[@id='root']/div/main/div[2]/div[3]/div[2]/div/div/div/div/div[3]/div/div[2]/div/div/div[3]/div/div/div/input" #  //input[@tabindex = 127]
    _type2 = "//div[@id='root']/div/main/div[2]/div[3]/div[2]/div/div/div/div/div[3]/div/div[2]/div/div/div[4]/div/div/select" #  //div[@tabindex = 128]
    _from2 = "//div[@id='root']/div/main/div[2]/div[3]/div[2]/div/div/div/div/div[3]/div/div[2]/div/div/div[5]/div/div/div/input" #  //input[@tabindex = 129]
    _to2 = "//div[@id='root']/div/main/div[2]/div[3]/div[2]/div/div/div/div/div[3]/div/div[2]/div/div/div[6]/div/div/div/input" #  //input[@tabindex = 130]
    _carrier_ref2 = "//div[@id='root']/div/main/div[2]/div[3]/div[2]/div/div/div/div/div[3]/div/div[2]/div/div/div[7]/div/div/input" #  //input[@tabindex = 131]
    _carrier_invoice2 = "//div[@id='root']/div/main/div[2]/div[3]/div[2]/div/div/div/div/div[3]/div/div[2]/div/div/div[8]/div/div/input" #  //input[@tabindex = 132]
    _cost2 = "//div[@id='root']/div/main/div[2]/div[3]/div[2]/div/div/div/div/div[3]/div/div[2]/div/div/div[9]/div/div/div/div/input" #  //input[@tabindex = 133]
    _cost_more2 = "//div[@id='root']/div/main/div[2]/div[3]/div[2]/div/div/div/div/div[3]/div/div[2]/div/div/div[9]/div//button" #  //span[@tabindex = 134]
    _cost_more2_desc = "//div[3]/div[3]/div/div[2]/div/div/div/div/textarea"   # //textarea[@tabindex = 134]
    _cost_more2_cancel_btn = "//div[3]/div[3]/div/div[3]/button" # wayne_id_CLOSE

    # Sell Rating
    _general_sell_rate = "wayne_id_Generate Sell Rate"
    _total_sell_rate = "//input[@id='wayne_id_Total sell rate']"
    _connote_sr = "wayne_id_CONNOTE"
    _account_name_sr = "//p[@id ='BELGOTEX NZ LTD']"
    _total_sr_btn = "//button[@tabindex='141']"
    _total_sr_cancel_btn = "//button[@tabindex =0]"
    _quoted_price = "//input[@tabindex='142'][@id='wayne_id_Quoted price']"
    _quoted_by = "//input[@tabindex='143'][@id='wayne_id_Quoted By']"
    _no_charge = "wayne_id_No charge?"
    _pricing_notes = "wayne_id_Pricing Notes?"
    _pricing_notes_description = "wayne_id_Pricing Notes"
    _pricing_notes_desc_save_btn = "wayne_id_Save"
    _pricing_notes_desc_close_btn = "wayne_id_Close"
    _cancelled = "wayne_id_cancelled?"

    # Additional Information

    _insurance = "//div[@id='wayne_id_Insurance Type']"
    _authority_to_leave = "wayne_id_Authority To Leave?"
    _dangerous_goods_ai = "//input[@tabindex='112']" #not used
    _pod_uploaded = "//input[@tabindex='107']"
    _christell_notes = "wayne_id_Christel Notes"  # might cause issue. check
    _special_instruction_ai = "//textarea[@tabindex='111']"
    _general_docs = "//button[@tabindex='109']"
    _general_docs_close = "wayne_id_Close"

    # Calculations

    _total_charge = "wayne_id_Total Sell Charge:"
    _total_cost = "wayne_id_Total Cost:"
    _gross_margin = "wayne_id_Gross Margin($): "
    _gross_margin_percentage = "wayne_id_Gross Margin(%): "

    # Footer buttons

    _create_consignment = "//div[4]/div/div/div/button/span[normalize-space()='Create Consignment']" #//button[@tabindex='151']
    _go_back = "wayne_id_Cancel Submit" #//button[@tabindex='152']
    _save_draft = "wayne_id_Save Draft" #//button[@tabindex='153']

    # Pop Up Windows

    _check_popUp = "//h2[normalize-space() = 'Do you want to create or edit the address?']"
    _edit_cancel_btn = "//button[normalize-space() = 'Cancel']"
    _edit_address_btn = "//button[normalize-space() = 'Edit Address']"
    _edit_create_address_btn = "//button[normalize-space() = 'Create Address']"
    _addr_upadted_successfully = "//span[normalize-space() ='Address updated Successfully']"

    def verifyNewConsignmentTitle(self):
        print('#' * 100)
        print("Express Cargo Ltd. | New Consignment")
        print('#' * 100)
        self.waitForElement(self._connote, "xpath")
        return self.verifyPageTitle("Express Cargo Ltd. | New Consignment")

    '''HEADER'''

    def enterConnote(self, connote):
        # ToDo:: jumble up the connote to make unique connotes
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
        if self.getElement(self._data_fetched_popup, "xpath").text == "Account Data Fetched":
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

    '''SENDER DETAILS'''

    # all xpath except CHARGES --- address types are select forms

    def enterSenderAddress(self, senderNewAddress):
        if senderNewAddress:
            self.sendKeys(senderNewAddress, self._enter_addr_l, "xpath")
            sa = self.getElement(self._enter_addr_l, "xpath")
            sa.send_keys(Keys.ENTER)

    def enterSenderCompany(self, senderCompanyName):
        # after filling the account name in HEADER values will be available due to api call
        # self.waitForElement(self._company_l, "xpath")
        # sce = self.getElement(self._company_l, "xpath")
        # self.elementClick("(//button[@title='Clear'])[5]", "xpath")
        self.elementClick(self._company_l, "xpath")
        self.driver.execute_script("arguments[0].value = ''", self.getElement(self._company_l, "xpath"))
        self.sendKeys(senderCompanyName, self._company_l, "xpath")
        sc = self.getElement(self._company_l, "xpath")
        sc.send_keys(Keys.ENTER)

    def checkSenderAddressType(self):  # return len of string which will be used to check if values are present or not
        # auto filled after filling Sender Company
        self.waitForElement(self._addr_type_l, "xpath")
        addrtype_l = self.getElement(self._addr_type_l, "xpath")
        addrtypeText_l = addrtype_l.get_attribute("value")
        _sender_ini_adrType = addrtypeText_l
        print(type(addrtypeText_l))
        if len(addrtypeText_l) > 0:
            return True
        else:
            return False

    def enterSenderAddressType(self, addressType):  # index
        if addressType != '':
            self.waitForElement(self._addr_type_l, "xpath")
            # self.getElement(self._addr_type_l, "xpath").clear()
            select_element = Select(self.getElement(self._addr_type_l, "xpath"))
            # select_element.select_by_index(0) # clear the field
            options = select_element.options
            for option in options:
                if option.text == addressType:
                    select_element.select_by_visible_text(addressType)
                    print(option.text)
            self.editPopUpWindow()
            # time.sleep(5)

    def enterSenderLot(self, lot):
        self.sendKeys(lot, self._lot_l)

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

    def checkSenderStreet(self):  # return len of string which will be used to check if values are present or not
        # auto filled after filling Sender Company
        self.waitForElement(self._street_l, "xpath")
        street_l = self.getElement(self._street_l, "xpath")
        if street_l.is_displayed():
            streetText_l = street_l.get_attribute("value")
            _sender_ini_street = streetText_l
            print(streetText_l)
            if type(streetText_l):
                return True
            else:
                return False
        else:
            return False

    def checkSenderSuburb(self):  # return len of string which will be used to check if values are present or not
        # auto filled after filling Sender Company
        self.waitForElement(self._suburb_l, "xpath")
        suburb_l = self.getElement(self._suburb_l, "xpath")
        suburbText_l = suburb_l.get_attribute("value")
        print(suburbText_l)
        if suburb_l.is_displayed():
            return True
        else:
            return False

    def checkSenderCity(self):  # return len of string which will be used to check if values are present or not
        # auto filled after filling Sender Company
        self.waitForElement(self._city_l, "xpath")
        city_l = self.getElement(self._city_l, "xpath")
        cityText_l = city_l.get_attribute("value")
        print(cityText_l)
        if city_l.is_displayed():
            return True
        else:
            return False

    def checkSenderState(self):  # return len of string which will be used to check if values are present or not
        # auto filled after filling Sender Company
        self.waitForElement(self._state_l, "xpath")
        state_l = self.getElement(self._state_l, "xpath")
        stateText_l = state_l.get_attribute("value")
        print(stateText_l)
        if state_l.is_displayed():
            return True
        else:
            return False

    def checkSenderPostCode(self):  # return len of string which will be used to check if values are present or not
        # auto filled after filling Sender Company
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

    # def checkSenderSpecialInstructions(self): # expected error
    #     si = self.getElement(self._special_instruction_l, "xpath").text
    #     if si != "":
    #         return True

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

    def enterSenderRoad(self, road):
        if road:
            self.waitForElement(self._road_l, "xpath")
            # self.elementClick("(//button[@title='Clear'])[5]", "xpath")
            road_element = self.getElement(self._road_l, "xpath")
            road_element.click()  # to focus on the input field
            # self.elementClick(self._road_l, "xpath")
            # time.sleep(2)
            # road_element.clear()
            self.driver.execute_script("arguments[0].value = ''", road_element)
            # print(self.getElement(self._road_l, "xpath").get_attribute("value"))
            self.sendKeys(road, self._road_l, "xpath")
            print(self.getElement(self._road_l, "xpath").get_attribute("value"))

    def enterSenderStreet(self, street):
        if street:
            self.waitForElement(self._street_l, "xpath")
            street_element = self.getElement(self._street_l, "xpath")
            street_element.click()  # to focus on the input field
            # self.elementClick(self._street_l, "xpath")
            # time.sleep(2)
            # street_element.clear()
            self.driver.execute_script("arguments[0].value = ''", street_element)
            self.sendKeys(street, self._street_l, "xpath")
            print(self.getElement(self._street_l, "xpath").get_attribute("value"))

    def enterSenderSuburb(self, suburb):
        if suburb:
            self.waitForElement(self.getElement(self._suburb_l, "xpath"))
            suburb_element = self.getElement(self._suburb_l, "xpath")
            suburb_element.click()  # to focus on the input field
            # time.sleep(2)
            # suburb_element.clear()
            self.driver.execute_script("arguments[0].value = ''", suburb_element)
            self.sendKeys(suburb, self._suburb_l, "xpath")
            print(self.getElement(self._suburb_l, "xpath").get_attribute("value"))

    def enterSenderCity(self, city):
        if city:
            self.waitForElement(self._city_l, "xpath")
            city_element = self.getElement(self._city_l, "xpath")
            city_element.click()  # to focus on the input field
            # self.elementClick(self._city_l, "xpath")
            # time.sleep(2)
            # city_element.clear()
            self.driver.execute_script("arguments[0].value = ''", city_element)
            self.sendKeys(city, self._city_l, "xpath")
            print(self.getElement(self._city_l, "xpath").get_attribute("value"))

    def enterSenderState(self, state):
        if state:
            self.waitForElement(self._state_l, "xpath")
            state_element = self.getElement(self._state_l, "xpath")
            state_element.click()  # to focus on the input field
            # self.waitForElement(self._state_l, "xpath")
            # self.elementClick(self._state_l, "xpath")
            # time.sleep(2)
            # state_element.clear()
            self.driver.execute_script("arguments[0].value = ''", state_element)
            self.sendKeys(state, self._state_l, "xpath")
            print(self.getElement(self._state_l, "xpath").get_attribute("value"))

    def enterSenderPostCode(self, postcode):
        if postcode:
            self.waitForElement(self._post_code_l, "xpath")
            postcode_element = self.getElement(self._post_code_l, "xpath")
            postcode_element.click()  # to focus on the input field
            # self.elementClick(self._post_code_l, "xpath")
            # time.sleep(2)
            # postcode_element.clear()
            self.driver.execute_script("arguments[0].value = ''", postcode_element)
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
        # self.sendKeys(suburb, self._suburb_l, "xpath")
        # _r1 = self.cancelPopUpWindow()
        self.sendKeys(city, self._city_l, "xpath")
        _r1 = self.cancelPopUpWindow()
        # self.sendKeys(state, self._state_l, "xpath")
        # _r1 = self.cancelPopUpWindow()
        self.sendKeys(postcode, self._post_code_l, "xpath")
        # self.getElement(self._post_code_l, "xpath").send_keys(Keys.SPACE)
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
        # self.sendKeys(suburb, self._suburb_r, "xpath")
        # _r1 = self.cancelPopUpWindow()
        self.sendKeys(city, self._city_r, "xpath")
        _r1 = self.cancelPopUpWindow()
        # self.sendKeys(state, self._state_r, "xpath")
        # _r1 = self.cancelPopUpWindow()
        self.sendKeys(postcode, self._post_code_r, "xpath")
        # self.getElement(self._post_code_r, "xpath").send_keys(Keys.SPACE)
        _r1 = self.cancelPopUpWindow()
        return _r1

    def editSenderDetailsCompanyName(self, senderCompanyName):
        _r1 = False
        self.sendKeys("a", self._company_l, "xpath")
        self.editPopUpWindow()
        self.enterSenderCompany(senderCompanyName=senderCompanyName)
        # print(self.getElement(self._company_l, "xpath").get_attribute("values"))
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
        # _r2 = False
        self.enterSenderAddressType(addressType=addressType)  # select type

        time.sleep(3)
        # _r1 = self.editPopUpWindow()
        # _r1 = self.checkSenderRoad()
        self.sendKeys("a", self._road_l, "xpath")
        _r1 = self.editPopUpWindow()
        if not _r1:
            self.log.info("### Road Field Error")
        self.enterSenderRoad(road=road)
        # time.sleep(3)
        # self.sendKeys("a", self._street_l, "xpath")
        # _r1 = self.editPopUpWindow()
        _r1 = self.checkSenderStreet()
        if not _r1:
            self.log.info("### Street Field Error")
        self.enterSenderStreet(street=street)
        # time.sleep(3)
        # # self.sendKeys("a", self._city_l, "xpath")
        # #_r1 = self.editPopUpWindow()
        _r1 = self.checkSenderCity()
        if not _r1:
            self.log.info("### City Field Error")
        self.enterSenderCity(city=city)
        # time.sleep(3)
        # # #self.sendKeys("a", self._state_l, "xpath")
        _r1 = self.checkSenderState()
        if not _r1:
            self.log.info("### State Field Error")
        self.enterSenderState(state=state)
        # time.sleep(3)
        # # #self.sendKeys("a", self._post_code_l, "xpath")
        _r1 = self.checkSenderPostCode()
        if not _r1:
            self.log.info("### PostCode Field Error")
        self.enterSenderPostCode(postcode=postcode)
        # #time.sleep(3)

        # if self.isElementPresent("//button[@tabindex='-1']/span[normalize-space()='EDIT ADDRESS']", "xpath"):
        #     print("Edit Address Button Blurred!!")
        self.waitForElement(self._create_addr_l, "xpath")
        cab = self.getElement(self._create_addr_l, "xpath")

        if cab is None:
            self.log.info("### CREATE ADDRESS BUTTON NOT FOUND!!!")
        if cab is not None and cab.is_enabled():
            self.elementClick(self._create_addr_l, "xpath")
            #     _r2 = True
            _es = self.isElementPresent("//span[normalize-space()='Address updated Successfully']", "xpath")

        if not _es:
            self.log.info("### Receiver Address Not Edited!!!")
        # print(_r2)
        # time.sleep(4)
        if _r1 and _es:  # and _r2
            return True
        else:
            return False

    def editReceiverDetailsCompanyName(self, receiverCompanyName):
        _r1 = False
        self.sendKeys("as", self._company_r, "xpath")
        self.editPopUpWindow()
        self.enterReceiverCompany(receiverCompanyName)
        # print(self.getElement(self._company_r, "xpath").get_attribute("values"))
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
        self.enterReceiverAddressType(addressType=addressType)  # select type
        #time.sleep(3)

        # _r1 = self.editPopUpWindow()
        # _r1 = self.checkSenderRoad()
        self.sendKeys("a", self._road_r, "xpath")
        _r1 = self.editPopUpWindow()
        if not _r1:
            self.log.error("### Road Field Error")
        self.enterReceiverRoad(road=road)
        # # # time.sleep(3)
        # # # self.sendKeys("a", self._street_l, "xpath")
        # # # _r1 = self.editPopUpWindow()
        _r1 = self.checkReceiverStreet()
        if not _r1:
            self.log.error("### Street Field Error")
        self.enterReceiverStreet(street=street)
        # # # time.sleep(3)
        # # # # self.sendKeys("a", self._city_l, "xpath")
        # # # #_r1 = self.editPopUpWindow()
        _r1 = self.checkReceiverCity()
        if not _r1:
            self.log.error("### City Field Error")
        self.enterReceiverCity(city=city)
        # # # time.sleep(3)
        # # # # #self.sendKeys("a", self._state_l, "xpath")
        _r1 = self.checkReceiverState()
        if not _r1:
            self.log.error("### State Field Error")
        self.enterReceiverState(state=state)
        # # # time.sleep(3)
        # # # # #self.sendKeys("a", self._post_code_l, "xpath")
        _r1 = self.checkReceiverPostCode()
        if not _r1:
            self.log.error("### PostCode Field Error")
        self.enterReceiverPostCode(postcode=postcode)
        # #
        self.waitForElement(self._create_addr_r, "xpath")
        cab = self.getElement(self._create_addr_r, "xpath")

        if cab is None:
            self.log.error("### CREATE ADDRESS BUTTON NOT FOUND!!!")
        if cab is not None and cab.is_enabled():
            self.elementClick(self._create_addr_r, "xpath")
            _es = self.isElementPresent("//span[normalize-space()='Address updated Successfully']", "xpath")
            #     _r2 = True
        if not _es:
            self.log.error("### Receiver Address Not Edited!!!")
        # print(_r2)
        # time.sleep(4)
        if _r1 and _es :  #
            return True
        else:
            return False

    # addrTy, Road, Street, City, State, PostCode
    def enterSenderDetails(self, senderNewAddress='', senderCompanyName='', lot='', forkLift='', driver='', openTime='',
                           closedtime='', vehicle="",
                           vehicleType='', specialInstructions='', charges=''):
        self.enterSenderAddress(senderNewAddress)
        self.enterSenderCompany(senderCompanyName)
        self.enterSenderLot(lot)
        self.clickSenderForkLift(forkLift)
        self.clickSenderDriver(driver)
        self.enterSenderOpenTime(openTime)
        self.enterSenderClosedTime(closedtime)
        self.enterSenderVehicle(vehicle)
        self.enterSenderVehicleType(vehicleType)
        self.enterSenderSpecialInstructions(specialInstructions)
        self.enterSenderCharges(charges)
        self.createAddressSender()

    '''RECEIVER DETAILS'''

    # all xpath except charges --- address types are select forms
    def enterReceiverRoad(self, road):
        if road:
            self.waitForElement(self._road_r, "xpath")
            # self.elementClick("(//button[@title='Clear'])[5]", "xpath")
            road_element = self.getElement(self._road_r, "xpath")
            #road_element.click()  # to focus on the input field
            # road_element.clear()
            self.elementClick(self._road_r, "xpath")
            self.driver.execute_script("arguments[0].value = ''", road_element)
            self.sendKeys(road, self._road_r, "xpath")
            print(self.getElement(self._road_r, "xpath").get_attribute("value"))

    def enterReceiverStreet(self, street):
        if street:
            self.waitForElement(self._street_r, "xpath")
            street_element = self.getElement(self._street_r, "xpath")
            # street_element.click()  # to focus on the input field
            # street_element.clear()
            self.elementClick(self._street_r, "xpath")
            self.driver.execute_script("arguments[0].value = ''", street_element)
            self.sendKeys(street, self._street_r, "xpath")
            print(self.getElement(self._street_r, "xpath").get_attribute("value"))

    def enterReceiverCompany(self, receiverCompanyName):
        # after filling the account name in HEADER values will be available due to api call
        self.elementClick(self._company_r, "xpath")
        self.driver.execute_script("arguments[0].value = ''", self.getElement(self._company_r, "xpath"))
        self.sendKeys(receiverCompanyName, self._company_r, "xpath")
        sc = self.getElement(self._company_r, "xpath")
        sc.send_keys(Keys.ENTER)

    def enterReceiverCity(self, city):
        if city:
            self.waitForElement(self._city_r, "xpath")
            city_element = self.getElement(self._city_r, "xpath")
            #city_element.click()  # to focus on the input field
            #time.sleep(4)
            self.elementClick(self._city_r, "xpath")
            # city_element.clear()
            self.driver.execute_script("arguments[0].value = ''", city_element)
            self.sendKeys(city, self._city_r, "xpath")
            print(self.getElement(self._city_r, "xpath").get_attribute("value"))

    def enterReceiverState(self, state):
        if state:
            self.waitForElement(self._state_r, "xpath")
            state_element = self.getElement(self._state_r, "xpath")
            #state_element.click()  # to focus on the input field
            #time.sleep(3)
            self.elementClick(self._state_r, "xpath")
            # state_element.clear()
            self.driver.execute_script("arguments[0].value = ''", state_element)
            self.sendKeys(state, self._state_r, "xpath")
            print(self.getElement(self._state_r, "xpath").get_attribute("value"))

    def enterReceiverPostCode(self, postcode):
        if postcode:
            self.waitForElement(self._post_code_r, "xpath")
            postcode_element = self.getElement(self._post_code_r, "xpath")
            #postcode_element.click()  # to focus on the input field
            #time.sleep(3)
            self.elementClick(self._post_code_r, "xpath")
            # postcode_element.clear()
            self.driver.execute_script("arguments[0].value = ''", postcode_element)
            self.sendKeys(postcode, self._post_code_r, "xpath")
            print(self.getElement(self._post_code_r, "xpath").get_attribute("value"))

    def enterReceiverAddress(self, receiverNewAddress):
        if receiverNewAddress:
            self.sendKeys(receiverNewAddress, self._enter_addr_r, "xpath")
            ra = self.getElement(self._enter_addr_r, "xpath")
            ra.send_keys(Keys.ENTER)

    def enterReceiverDetailsCompanyName(self, senderCompanyName):
        # after filling the account name in HEADER values will be available due to api call
        self.waitForElement(self._company_r, "xpath")
        self.sendKeys(senderCompanyName, self._company_r, "xpath")
        rc = self.getElement(self._company_r, "xpath")
        rc.send_keys(Keys.ENTER)

    def checkReceiverAddressType(self):  # return len of string which will be used to check if values are present or not
        # auto filled after filling Sender Company
        self.waitForElement(self._addr_type_r, "xpath")
        addrtype_r = self.getElement(self._addr_type_r, "xpath")
        addrtypeText_r = addrtype_r.get_attribute("value")
        if addrtype_r.is_displayed():
            return True
        else:
            return False

    def enterReceiverAddressType(self, addressType):
        if addressType:
            self.waitForElement(self._addr_type_r, "xpath")
            select_element = Select(self.getElement(self._addr_type_r, "xpath"))
            options = select_element.options
            for option in options:
                if option.text == addressType:
                    select_element.select_by_visible_text(addressType)
                    print(option.text, addressType)
            self.editPopUpWindow()

    def enterReceiverLot(self, lot):
        self.sendKeys(lot, self._lot_r)

    def checkReceiverRoad(self):  # return len of string which will be used to check if vgalues are present or not
        # auto filled after filling Sender Company
        self.waitForElement(self._road_r, "xpath")
        road_r = self.getElement(self._road_r, "xpath")
        roadText_r = road_r.get_attribute("value")
        if road_r.is_displayed():
            return True
        else:
            return False

    def checkReceiverStreet(self):  # return len of string which will be used to check if values are present or not
        # auto filled after filling Sender Company
        self.waitForElement(self._street_r, "xpath")
        street_r = self.getElement(self._street_r, "xpath")
        streetText_r = street_r.get_attribute("value")
        if street_r.is_displayed():
            return True
        else:
            return False

    def checkReceiverSuburb(self):  # return len of string which will be used to check if values are present or not
        # auto filled after filling Sender Company
        self.waitForElement(self._suburb_r, "xpath")
        suburb_r = self.getElement(self._suburb_r, "xpath")
        suburbText_r = suburb_r.get_attribute("value")
        if suburb_r.is_displayed():
            return True
        else:
            return False

    def checkReceiverCity(self):  # return len of string which will be used to check if values are present or not
        # auto filled after filling Sender Company
        self.waitForElement(self._city_r, "xpath")
        city_r = self.getElement(self._city_r, "xpath")
        cityText_r = city_r.get_attribute("value")
        if city_r.is_displayed():
            return True
        else:
            return False

    def checkReceiverState(self):  # return len of string which will be used to check if values are present or not
        # auto filled after filling Sender Company
        self.waitForElement(self._state_r, "xpath")
        state_r = self.getElement(self._state_r, "xpath")
        stateText_r = state_r.get_attribute("value")
        if state_r.is_displayed():
            return True
        else:
            return False

    def checkReceiverPostCode(self):  # return len of string which will be used to check if values are present or not
        # auto filled after filling Sender Company
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
            # ch = self.getElement(self._charges_r, "xpath")
            # ch.send_keys(Keys.ENTER)

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
        self.createAddressReceiver()

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

    def enterServices_1(self, services): # input type- aria descendant,, USE KEYS ARROW DOWN, need to change code for that
        self.waitForElement(self._services1, "xpath")
        self.elementClick(self._services1, "xpath")
        self.sendKeys(services, self._services1, "xpath")
        #self.action.send_keys(Keys.ARROW_DOWN)
        serv = self.getElement(self._services1, "xpath")
        serv.send_keys(Keys.ENTER)


    def enterWeightUnit_1(self, weightUnit):  # select type
        if weightUnit:
            self.waitForElement(self._weight_unit1, "xpath")
            self.sendKeys(weightUnit, self._weight_unit1, "xpath")
            # wt = self.getElement(self._weight_unit1, "xpath")
            # wt.send_keys(Keys.ENTER)

    def enterDimensionUnit_1(self, dunit):  # select type
        if dunit:
            self.waitForElement(self._dimension_unit1, "xpath")
            self.sendKeys(dunit, self._dimension_unit1, "xpath")
            # du = self.getElement(self._dimension_unit1, "xpath")
            # du.send_keys(Keys.ENTER)

    def enterContainerNumber_1(self, containerNumber):
        if containerNumber:
            self.waitForElement(self._container_number1, "xpath")
            self.sendKeys(containerNumber, self._container_number1, "xpath")
            # cn = self.getElement(self._container_number1, "xpath")
            # cn.send_keys(Keys.ENTER)

    def enterAgency_1(self, agency):
        pass

    def enterItem_1(self, item):
        self.waitForElement(self._item1, "xpath")
        self.sendKeys(item, self._item1, "xpath")
        it1 = self.getElement(self._item1, "xpath")
        it1.send_keys(Keys.ENTER)

    def enterCommodity_1(self, commodity):
        # services option must be filled first for data to load
        # self.waitForElement(self._commodity1, "xpath")
        self.elementClick(self._commodity1, "xpath")
        self.sendKeys(commodity, self._commodity1, "xpath")
        cm1 = self.getElement(self._commodity1, "xpath")
        cm1.send_keys(Keys.ENTER)

    def enterDescription_1(self, description):
        if description:
            self.waitForElement(self._description1, "xpath")
            self.sendKeys(description, self._description1, "xpath")
            # des1 = self.getElement(self._services1, "xpath")
            # des1.send_keys(Keys.ENTER)

    def enterQuantity_1(self, quantity):
        self.waitForElement(self._quantity1, "xpath")
        self.sendKeys(quantity, self._quantity1, "xpath")
        # qu1 = self.getElement(self._quantity1, "xpath")
        # qu1.send_keys(Keys.ENTER)

    def enterWeight_1(self, weight):
        self.waitForElement(self._weight1, "xpath")
        self.sendKeys(weight, self._weight1, "xpath")
        # wt1 = self.getElement(self._weight1, "xpath")
        # wt1.send_keys(Keys.ENTER)

    def enterVolume_1(self, volume):
        self.waitForElement(self._volume1, "xpath")
        self.sendKeys(volume, self._volume1, "xpath")
        # vol1 = self.getElement(self._volume1, "xpath")
        # vol1.send_keys(Keys.ENTER)

    def enterLength_1(self, length):
        if length:
            self.waitForElement(self._length1, "xpath")
            self.sendKeys(length, self._length1, "xpath")
            # l1 = self.getElement(self._length1, "xpath")
            # l1.send_keys(Keys.ENTER)

    def enterWidth_1(self, width):
        if width:
            self.waitForElement(self._width1, "xpath")
            self.sendKeys(width, self._width1, "xpath")
            # wd1 = self.getElement(self._width1, "xpath")
            # wd1.send_keys(Keys.ENTER)

    def enterHeight_1(self, height):
        if height:
            self.waitForElement(self._height1, "xpath")
            self.sendKeys(height, self._height1, "xpath")
            # h1 = self.getElement(self._height1, "xpath")
            # h1.send_keys(Keys.ENTER)

    def clickDangerousGoods_1(self, dg):
        if dg:
            self.waitForElement(self._dg1, "xpath")
            self.elementClick(self._dg1)

    def clickAddLine(self):
        self.elementClick(self._add_line_btn)

    def enterItem_2(self, item):
        self.waitForElement(self._item2, "xpath")
        self.sendKeys(item, self._item2, "xpath")
        it2 = self.getElement(self._item2, "xpath")
        it2.send_keys(Keys.ENTER)

    def enterCommodity_2(self, commodity):
        # services option must be filled first for data to load
        self.waitForElement(self._commodity2, "xpath")
        self.elementClick(self._commodity2, "xpath")
        self.sendKeys(commodity, self._commodity2, "xpath")
        cmd2 = self.getElement(self._commodity2, "xpath")
        cmd2.send_keys(Keys.ENTER)

    def enterDescription_2(self, description):
        if description:
            self.sendKeys(description, self._description2, "xpath")
            # des2 = self.getElement(self._description2, "xpath")
            # des2.send_keys(Keys.ENTER)

    def enterQuantity_2(self, quantity):
        self.waitForElement(self._quantity2, "xpath")
        self.sendKeys(quantity, self._quantity2, "xpath")
        # qu2 = self.getElement(self._quantity2, "xpath")
        # qu2.send_keys(Keys.ENTER)

    def enterWeight_2(self, weight):
        self.waitForElement(self._weight2, "xpath")
        self.sendKeys(weight, self._weight2, "xpath")
        # wt2 = self.getElement(self._weight2, "xpath")
        # wt2.send_keys(Keys.ENTER)

    def enterVolume_2(self, volume):
        self.waitForElement(self._volume2, "xpath")
        self.sendKeys(volume, self._volume2, "xpath")
        # vl2 = self.getElement(self._volume2, "xpath")
        # vl2.send_keys(Keys.ENTER)

    def enterLength_2(self, length):
        if length:
            self.waitForElement(self._length2, "xpath")
            self.sendKeys(length, self._length2, "xpath")
            # l2 = self.getElement(self._length2, "xpath")
            # l2.send_keys(Keys.ENTER)

    def enterWidth_2(self, width):
        if width:
            self.waitForElement(self._width2, "xpath")
            self.sendKeys(width, self._width2, "xpath")
            # wd2 = self.getElement(self._width2, "xpath")
            # wd2.send_keys(Keys.ENTER)

    def enterHeight_2(self, height):
        if height:
            self.waitForElement(self._height2, "xpath")
            self.sendKeys(height, self._height2, "xpath")
            # ht2 = self.getElement(self._height2, "xpath")
            # ht2.send_keys(Keys.ENTER)

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
        #totalweight =float(tw.text)
        reg_res = re.findall(r'[\d\.\d]+', tw.text)
        print(reg_res[0])
        res = round(float(reg_res[0]), 1)
        return res

    def findTotalVolume(self):
        self.waitForElement(self._total_volume)
        tv = self.getElement(self._total_volume)
        #totalvolume = float(tv.text)
        reg_res = re.findall(r'[\d\.\d]+', tv.text)
        #res = float(reg_res)
        print(reg_res[0])
        res = round(float(reg_res[0]), 1)
        return res

    def enterConsignmentLine_1(self, services1, item1, commodity1, quantity1, weight1, volume1):  # , weightUnit1, dunit1, containerNumber1, agency1, description1, length1, width1, height1, dg1
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

    def checkRequiredFieldsCL(self):
        _res = True
        _res = self.checkServicesField()
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
        sum = sum + round(float(wt), 1)
        sum = sum * int(qu)

        print(int(qu))
        if self.isElementPresent(self._weight2, "xpath"):
            wt2 = self.getElement(self._weight2, "xpath").get_attribute("value")
            Wt2 = round(float(wt2), 1)
            qu2 = self.getElement(self._quantity2, "xpath").get_attribute("value")
            sum = round(sum + (Wt2 * int(qu2)), 1)
            print(Wt2, int(qu2))
        sum = round(sum, 1)
        print(sum)
        return sum

    def calctotalvolume(self):
        sum = 0.000
        vol = self.getElement(self._volume1, "xpath").get_attribute("value")
        qu = self.getElement(self._quantity1, "xpath").get_attribute("value")
        sum = sum + round(float(vol), 1)
        sum = sum * int(qu)

        print(int(qu))
        if self.isElementPresent(self._volume2, "xpath"):
            vl = self.getElement(self._volume2, "xpath").get_attribute("value")
            vol2 = round(float(vl), 1)
            qu2 = self.getElement(self._quantity2, "xpath").get_attribute("value")
            sum = round(sum + (vol2 * int(qu2)), 1)
            print(vol2, int(qu2))
        sum = round(sum, 1)
        print(sum)
        return sum

    def totalWeightVerification(self):
        expectedVal = self.calctotalweight()
        actualVal = self.findTotalWeight()
        print(expectedVal, actualVal)
        verval = self.verifyValues(actualVal, expectedVal)
        return verval

    def totalVolumeVerification(self):
        expectedVal = self.calctotalvolume()
        actualVal = self.findTotalVolume()
        print(expectedVal, actualVal)
        verval = self.verifyValues(actualVal, expectedVal)
        return verval

    'LEGGING'

    def enterDate(self, date):
        if date:
            self.waitForElement(self._date1, "xpath")
            self.sendKeys(self._date1, "xpath")

    def enterCarrier1(self, carrier):
        # self.driver.execute_script("window.scrollBy(0, -40);")
        #element = self.getElement(self._carrier1, "xpath")
        self.waitForElement("//div[@id='root']/div/main/div[2]/div[3]/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/input", "xpath")
        self.sendKeys(carrier, "//div[@id='root']/div/main/div[2]/div[3]/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/input", "xpath")
        it1 = self.getElement("//div[@id='root']/div/main/div[2]/div[3]/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/input", "xpath")
        it1.send_keys(Keys.ENTER)

        ##
        # self.waitForElement("//input[@tabindex='117'][@id='wayne_id_Carrier']", "xpath")
        # ca1 = self.getElement("//input[@tabindex='117'][@id='wayne_id_Carrier']", "xpath")
        # if ca1 is not None:
        #     self.sendKeys(carrier, self._carrier1, "xpath")
        #     ca1.send_keys(Keys.ENTER)
        # else:
        #     print("Element not found:", self._carrier1)

    def enterCarrier2(self, carrier):
        self.waitForElement(self._carrier2, "xpath")
        self.sendKeys(carrier, self._carrier2, "xpath")
        ca2 = self.getElement(self._carrier2, "xpath")
        ca2.send_keys(Keys.ENTER)

    def enterDepot1(self, depot):
        if depot:
            self.waitForElement(self._depot1, "xpath")
            self.elementClick(self._depot1, "xpath")
            self.sendKeys(depot, self._depot1, "xpath")
            de1 = self.getElement(self._depot1, "xpath")
            de1.send_keys(Keys.ENTER)

    def enterDepot2(self, depot):
        if depot:
            self.waitForElement(self._depot2, "xpath")
            self.elementClick(self._depot2, "xpath")
            self.sendKeys(depot, self._depot2, "xpath")
            de2 = self.getElement(self._depot2, "xpath")
            de2.send_keys(Keys.ENTER)

    def enterType1(self, type):  # select type
        self.waitForElement(self._type1, "xpath")
        select_element = Select(self.getElement(self._type1, "xpath"))
        options = select_element.options
        for option in options:
            if option.text == type:
                select_element.select_by_visible_text(type)
                print(option.text, type)

    def enterType2(self, type):  # select type
        self.waitForElement(self._type2, "xpath")
        select_element = Select(self.getElement(self._type2, "xpath"))
        options = select_element.options
        for option in options:
            if option.text == type:
                select_element.select_by_visible_text(type)
                print(option.text, type)

    def enterFrom1(self, frm):
        self.waitForElement(self._from1, "xpath")
        self.sendKeys(frm, self._from1, "xpath")
        fr1 = self.getElement(self._from1, "xpath")
        fr1.send_keys(Keys.ENTER)

    def enterFrom2(self, frm):
        self.waitForElement(self._from2, "xpath")
        self.sendKeys(frm, self._from2, "xpath")
        fr1 = self.getElement(self._from2, "xpath")
        fr1.send_keys(Keys.ENTER)

    def enterTo1(self, to): # returning when the source and destination locations are same in LEGGING 1
        self.waitForElement(self._to1, "xpath")
        self.sendKeys(to, self._to1, "xpath")
        frm = self.getElement(self._from1, "xpath").get_attribute("value")
        if frm == to:
            self.log.error("### Source and Destination can't be same!!!")
            return
        to1 = self.getElement(self._to1, "xpath")
        to1.send_keys(Keys.ENTER)

    def enterTo2(self, to):
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
            self.waitForElement(self._carrier_ref1)
            self.sendKeys(carrRef, self._carrier_ref1, "xpath")
            cr1 = self.getElement(self._carrier_ref1, "xpath")
            cr1.send_keys(Keys.ENTER)

    def enterCarrierRef2(self, carrRef):
        if carrRef:
            self.waitForElement(self._carrier_ref2)
            self.sendKeys(carrRef, self._carrier_ref2, "xpath")
            cr1 = self.getElement(self._carrier_ref2, "xpath")
            cr1.send_keys(Keys.ENTER)

    def entercarrierInvoice1(self, carrInv):
        if carrInv:
            self.waitForElement(self._carrier_invoice1, "xpath")
            self.sendKeys(carrInv, self._carrier_invoice1, "xpath")
            ci1 = self.getElement(self._carrier_invoice1, "xpath")
            ci1.send_keys(Keys.ENTER)

    def entercarrierInvoice2(self, carrInv):
        if carrInv:
            self.waitForElement(self._carrier_invoice2, "xpath")
            self.sendKeys(carrInv, self._carrier_invoice2, "xpath")
            ci1 = self.getElement(self._carrier_invoice2, "xpath")
            ci1.send_keys(Keys.ENTER)

    def enterCost1(self, cost):
        if cost:
            self.waitForElement(self._cost1, "xpath")
            self.sendKeys(cost, self._cost1, "xpath")
            co1 = self.getElement(self._cost1, "xpath")
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
            print(self.getElement(self._cost_more1_desc, "xpath").get_attribute("value"))
            self.elementClick(self._cost_more1_cancel_btn, "xpath")

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
    def enterLegging_1(self, carrier1,  type1, depot1, frm1, to1, cost1, cn1): # date1,  carrRef1, carrInv1
        #self.enterDate(date1)
        self.enterCarrier1(carrier1)
        self.enterDepot1(depot1)
        self.enterType1(type1)
        self.enterFrom1(frm1)
        self.enterTo1(to1)
        # self.enterCarrierRef1(carrRef1)
        # self.entercarrierInvoice1(carrInv1)
        self.enterCost1(cost1)
        self.enterCostMore1(cn1)

    def enterLegging_2(self, carrier2, depot2, type2, frm2, to2, cost2, cn2):
        self.clickAddLeg()
        # self.enterDate(date2)
        self.enterCarrier2(carrier2)
        self.enterDepot2(depot2)
        self.enterType2(type2)
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
        _res = self.checkCost1()
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
        if cm1==cm2:
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
        reg_res = re.findall(r'[\d\.\d]+', tl.text)
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
        print(sum)
        return sum


    def findTotalLeggingCost(self):
        self.waitForElement(self._total_legging_cost)
        tlc = self.getElement(self._total_legging_cost)
        reg_res = re.findall(r'[\d\.\d]+', tlc.text)
        print(reg_res[0])
        res = round(float(reg_res[0]), 2)
        return res

    def verifyTotalLeggingCost(self):
        expectedVal = self.calctotalleggingcost()
        actualVal = self.findTotalLeggingCost()
        print(expectedVal, actualVal)
        verval = self.verifyValues(actualVal, expectedVal)
        return verval

    '''SELL RATING'''

    def checkSRGenerated(self):
        self.waitForElement(self._general_sell_rate)
        if self.getElement(self._general_sell_rate).is_enabled():
            self.log.info("### Sell Rate Not generated!!!")
            return False
        else:
            tsr = self.getElement(self._total_sell_rate, "xpath").get_attribute("value")
            print(tsr)
            if float(tsr) == 0.0:
                self.log.info("### Sell Rate NOT GENERATED!!!")
                val1 = False
                print(val1)
                return val1
            else:
                print(float(tsr))
                self.log.info("Sell Rate generated!!!")
                val2 = True
                return val2

    def clickGenerateSR(self):
        self.waitForElement(self._general_sell_rate)
        self.elementClick(self._general_sell_rate)
        if self.getElement(self._general_sell_rate).is_enabled():
            self.elementClick(self._general_sell_rate)
        if self.isElementPresent("//span[normalize-space()='Rate calculated sucessfully']", "xpath"):
            self.log.info("Sell Rate Generated!!!")
        else:
            self.log.error("### Sell Rate Not Generated!!!")


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
            self.waitForElement(self._no_charge)
            self.elementClick(self._no_charge)
            self.waitForElement("//div[2]/div/div/div/div/textarea", "xpath")
            self.elementClick("//div[2]/div/div/div/div/textarea", "xpath")
            self.sendKeys(noCharge, "//div[2]/div/div/div/div/textarea", "xpath")
            self.elementClick("//div[3]/div/div[3]/button/span", "xpath")

    def clickPricingNotes(self, pricingNotes):
        if pricingNotes:
            self.elementClick(self._pricing_notes)
            self.elementClick("//div[2]/div/div/div/div/textarea", "xpath")
            self.sendKeys(pricingNotes, "//div[2]/div/div/div/div/textarea", "xpath")
            self.elementClick("//div[2]/div/div[2]/button/span", "xpath")
            self.elementClick("//div[3]/div/div[3]/button/span", "xpath")

    def clickCancelled(self, cancelled):
        if cancelled:
            self.waitForElement(self._cancelled)
            self.elementClick(self._cancelled)
            self.waitForElement("//h2[normalize-space()='Are you sure To cancel this consignment?']", "xpath")
            self.elementClick("//div[3]/button[2]/span", "xpath")

    def checkConsignmentCancelled(self):
        if self.getElement(self._cancelled).is_selected():
            self.log.info("### Consignment Cancelled!!!")
        else:
            self.log.info("Consignment Active!!!")

    # connote anSR quotedPrice noCharge pricingNotes cancelled

    def enterSellRating(self, quotedPrice, noCharge, quotedBy, pricingNotes, cancelled):
        self.clickGenerateSR()
        self.enterQuotedPrice(quotedPrice)
        self.clickNoCharge(noCharge)
        self.enterQuotedBy(quotedBy)
        self.clickPricingNotes(pricingNotes)
        self.clickCancelled(cancelled)

    '''ADDITIONAL INFORMATION'''

    # general docs ->id all else xpath; insurance is select type

    def enterInsurance(self, insurance):
        if insurance:
            select_element = Select(self.getElement(self._insurance, "xpath"))
            options = select_element.options
            for option in options:
                if insurance==option.text:
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
        self.driver.execute_script("window.scrollBy(0, 500);")
        self.waitForElement(self._create_consignment, "xpath")
        ccb = self.getElement(self._create_consignment, "xpath")

        if self.isElementPresent(self._create_consignment, "xpath"):
            #self.driver.execute_script("arguments[0].click();", ccb)
            self.waitForElement(self._create_consignment, "xpath")
            # ele = self.getElement(self._create_consignment, "xpath")
            # self.action.move_to_element(ele).click().perform()
            self.elementClick(self._create_consignment, "xpath")
            time.sleep(3)
            cc = self.verifyPageTitle("Express Cargo Ltd. | Dashboard")
            if cc:
                self.log.info("CONSIGNMENT CREATED!!!")
                return True
            else:
                self.log.error("### ERROR IN CONSIGNMENT CREATION!!!!")
                return False

            # if :
            #     self.log.info("CONSIGNMENT CREATED!!!")
            #     return True
            # else:
            #     self.log.error("### ERROR IN CONSIGNMENT CREATION!!!!")
            #     time.sleep(7)
            #     return False
        else:
            return False
        #self.waitForElement("//span[@normalize-space()='Consignment created successfully']", "xpath")


    def clickGoBack(self):
        pass

    def clickSaveDraft(self):
        self.elementClick(self._save_draft)
