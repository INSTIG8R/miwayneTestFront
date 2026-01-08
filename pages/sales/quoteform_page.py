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


class QuoteForm(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.alert = Alert(self.driver)
        self.action = ActionChains(self.driver)

    # Locators

    # Headers
    _account_name = "//input[@tabindex = 1002]"
    _customer_ref = "//input[@tabindex = 1006]"
    _receiver_ref = "//input[@tabindex = 1007]"
    _date_ready = "//input[@id = 'wayne_id_Date Ready']"

    _data_fetched_popup = "//div[contains(text(),'Address Info Fetched')]"

    # Sender Details

    ## ADDRESS TYPES
    _residential_at = "// li[normalize - space() = 'RESIDENTIAL']"
    _business_at = " //li[normalize-space()='BUSINESS']"
    _residential_business_at = " //li[normalize-space()='RESIDENTIAL BUSINESS']"

    _enter_addr_l = "//input[@tabindex = '2002']"
    _company_l = "//input[@tabindex='2001']"
    _addr_type_l = "//div[@tabindex='2003']"
    _lot_l = "//input[@tabindex='2004']"
    _road_l = "//input[@tabindex='2005']"
    _street_l = "//input[@tabindex='2006']"
    _suburb_l = "//input[@tabindex='2007']"
    _city_l = "//input[@tabindex='2008']"
    _state_l = "//input[@tabindex='2009']"
    _post_code_l = "//input[@tabindex='2010']"
    _forklift_l = "//input[@tabindex='2015']"
    _driver_l = "//input[@tabindex='2019']"
    _open_time_l = "//input[@tabindex='2012']"  # [0]
    _close_time_l = "//input[@tabindex='2013']"  # [0]
    # _vehicle_l = "//input[@tabindex =31]"
    _ringbeforepickupordelivery_l = "//input[@tabindex =2017]"
    _charges_l = "//input[@tabindex='2014']"
    _taillift_l = "//input[@tabindex='2016']"
    _cfs_site_l = "//input[@tabindex =2018]"
    _unmannedsite_l = "//input[@tabindex = '2020']"
    _special_instruction_l = "//textarea[@tabindex = '2021']"
    _create_addr_l = "//button[@tabindex =2024]"  ##Not Used
    ##Not Used

    _charges_lst_f = "//div[@data-tag-index=0]/span"  # [0]
    _charges_rst_f = ""

    # Receiver details

    _enter_addr_r = "//input[@tabindex = '3002']"
    _company_r = "//input[@tabindex = '3001']"
    _addr_type_r = "//div[@tabindex = '3003']"
    _lot_r = "//input[@tabindex = '3004']"
    _road_r = "//input[@tabindex = '3005']"
    _street_r = "//input[@tabindex = '3006']"
    _suburb_r = "//input[@tabindex = '3007']"
    _city_r = "//input[@tabindex = '3008']"
    _state_r = "//input[@tabindex = '3009']"
    _post_code_r = "//input[@tabindex = '3010']"
    _forklift_r = "//input[@tabindex = '3015']"
    _driver_r = "//input[@tabindex = '3019']"
    _open_time_r = "//input[@tabindex = '3012']"  # [1]
    _close_time_r = "//input[@tabindex = '3013']"  # [1]
    _taillift_r = "//input[@tabindex = '3016']"
    _ringbeforepickupordelivery_r = "//input[@tabindex = '3017']"
    _charges_r = "//input[@tabindex = '3014']"
    _cfs_site_r = "//input[@tabindex = '3018']"
    _unmannedsite_r = "//input[@tabindex = '3020']"
    _special_instruction_r = "//textarea[@tabindex = '3021']"
    _create_addr_r = "//button[@tabindex='3024']"  ##Not Used

    # Contact Details sender

    _first_name_l = "//input[@tabindex = '2025']"
    _last_name_l = "//input[@tabindex = '2026']"
    _email_l = "//input[@tabindex = '2027']"
    _phone_number_l = "//input[@tabindex = '2028']"
    _mobile_number_l = "//input[@tabindex = '2029']"
    _role_l = "//div[@tabindex = '61']"
    _create_contact_l = "//button[@tabindex='62']"

    # Contact Details receiver

    _first_name_r = "//input[@tabindex='3025']"
    _last_name_r = "//input[@tabindex='3026']"
    _email_r = "//input[@tabindex='3027']"
    _phone_number_r = "//input[@tabindex='3028']"
    _mobile_number_r = "//input[@tabindex='3029']"
    _role_r = "//select[@tabindex = '68']"
    _create_contact_r = "//button[@tabindex='69']"

    # Consignment Lines ( CAN HAVE VARIOUS LINES)

    _line_number = "//strong[text() = 1]"  # [0]
    _services1 = "//input[@tabindex='4001']"
    _weight_unit1 = "//div[@tabindex='4002']"
    _volume_unit1 = "//div[@tabindex='4003']"
    _container_number1 = "//input[@tabindex='4004']"
    _agency1 = "//input[@tabindex='4005']"
    _item1 = "//input[@tabindex='5001']"
    _commodity1 = "//input[@tabindex='5002'][@id ='wayne_id_Commodity0']"
    _description1 = "//input[@tabindex='5003'][@id ='wayne_id_Description0']"
    _quantity1 = "//input[@tabindex='5004'][@id ='wayne_id_Quantity0']"
    _weight1 = "//input[@tabindex='5005'][@id ='wayne_id_Weight0']"
    _volume1 = "//input[@tabindex='5006'][@id ='wayne_id_Volume0']"
    _length1 = "//input[@tabindex='5007'][@id ='wayne_id_Length0']"
    _width1 = "//input[@tabindex='5008'][@id='wayne_id_Width0']"
    _height1 = "//input[@tabindex='5009'][@id ='wayne_id_Height0']"
    _dg1 = "//input[@tabindex='5010']"
    _add_line_btn = "//button[@id ='wayne_id_Add line']"
    _total_lines = "wayne_id_Total lines"
    _total_item_count = "wayne_id_Total item count"
    _total_weight = "wayne_id_Total weight"
    _total_volume = "wayne_id_Total volume"

    _item2 = "//input[@tabindex='5101'][@id='wayne_id_Item1']"
    _commodity2 = "//input[@tabindex='5102'][@id='wayne_id_Commodity1']"
    _description2 = "//input[@tabindex='5103'][@id='wayne_id_Description1']"
    _quantity2 = "//input[@tabindex='5104'][@id='wayne_id_Quantity1']"
    _weight2 = "//input[@tabindex='5105'][@id='wayne_id_Weight1']"
    _volume2 = "//input[@tabindex='5106'][@id='wayne_id_Volume1']"
    _length2 = "//input[@tabindex='5107'][@id='wayne_id_Length1']"
    _width2 = "//input[@tabindex='5108'][@id='wayne_id_Width1']"
    _height2 = "//input[@tabindex='5109'][@id='wayne_id_Height1']"
    _dg2 = "//input[@tabindex='5110'][@id='wayne_id_dangerous goods ?1']"

    # delete button
    _delete_line_one = "//button[@tabindex = 88]"
    _delete_line_two = "button[@tabindex = 102]"


    # Sell Rating
    _estimate_price = "//button[normalize-space()='Estimate Price']/parent::div"
    _estimated_sell_rate = "//input[@id='wayne_id_Estimated Sell Rate']"
    _pricing_notes = "//input[@id='wayne_id_Pricing Notes?']"
    _pricing_notes_description = "wayne_id_Pricing Notes"
    _pricing_notes_desc_save_btn = "wayne_id_Save"
    _pricing_notes_desc_close_btn = "wayne_id_Close"

    # Additional Information

    _insurance = "//div[@id='wayne_id_Insurance Type']"
    _authority_to_leave = "//input[@id='wayne_id_Authority To Leave?']"
    _customer_notes = "wayne_id_Customer Notes?"
    _special_instruction_ai = "//textarea[@tabindex='6006']"
    _general_docs = "//button[@tabindex='6005']"
    _general_docs_close = "wayne_id_Close"

    # Calculations


    _create_quote = "//button[@id = 'wayne_id_Create Quote, ']"  # //button[@tabindex='151']
    _go_back = "wayne_id_Cancel Submit"

    # DEPOT REQUIRED ERROR CHECK
    _depot_required = "//p[@id='wayne_id_Depot0-helper-text']"

    # Pop Up Windows

    _check_popUp = "//h2[normalize-space() = 'Do you want to create or edit the address?']"
    _edit_cancel_btn = "//button[normalize-space() = 'Cancel']"
    _edit_address_btn = "//button[@id = 'wayne_id_Edit Address'][@tabindex =0]"
    _edit_address_btn_r = "//button[normalize-space() = 'Change Address']"
    _edit_create_address_btn = "//button[normalize-space() = 'Create Address']"
    _addr_upadted_successfully = "//span[normalize-space() ='Address updated Successfully']"
    # error logs array
    _error_logs = []


    def verifyNewQuoteTitle(self):
        print("Express Cargo Ltd. | Consignment Form")
        self.waitForElement(self._account_name, "xpath")
        time.sleep(2)
        return self.verifyPageTitle("Express Cargo Ltd. | QUOTE FORM")

    '''HEADER'''
    def enterAccountName(self, accountName):
        self.waitForElement(self._account_name, "xpath")
        an = self.getElement(self._account_name, "xpath")
        self.sendKeys(accountName, self._account_name, "xpath")
        time.sleep(2)
        an.send_keys(Keys.ARROW_DOWN)
        an.send_keys(Keys.ARROW_DOWN)
        an.send_keys(Keys.ENTER)


    def enterCustomerRef(self, customerRef):
        if customerRef:
            self.sendKeys(customerRef, self._customer_ref, "xpath")

    def enterReceiverRef(self, receiverRef):
        if receiverRef:
            self.sendKeys(receiverRef, self._receiver_ref, "xpath")

    def checkDateReady(self):
        dr = self.getElement(self._date_ready, "xpath")
        dr_val = dr.get_attribute("value")
        print(dr_val)
        if dr_val:
            return True
        else:
            return False

    def checkDataFetchedPopUp(self):
        self.waitForElement(self._data_fetched_popup, "xpath")
        print(self.getElement(self._data_fetched_popup, "xpath").text)
        if self.getElement(self._data_fetched_popup, "xpath").text == "Account Info Fetched":
            return True
        else:
            return False

    # connote accountName status dateAllocated customerRef receiverRef dateReady estDeliveryDate assignedTo priorityLevel

    def enterHeaderInformation(self, accountName='', customerRef='', receiverRef=''):
        self.enterAccountName(accountName)
        self.enterCustomerRef(customerRef)
        self.enterReceiverRef(receiverRef)
        time.sleep(2)

    '''SENDER DETAILS'''


    def enterSenderAddress(self, senderNewAddress):
        if senderNewAddress:
            sa = self.getElement(self._enter_addr_l, "xpath")
            self.sendKeys(senderNewAddress, self._enter_addr_l, "xpath")
            time.sleep(5)
            # sa.send_keys(Keys.ARROW_DOWN)
            # sa.send_keys(Keys.ARROW_DOWN)
            sa.send_keys(Keys.ENTER)

    def enterSenderCompany(self, senderCompanyName):
        # after filling the account name in HEADER values will be available due to api call
        # self.waitForElement(self._company_l, "xpath")
        # sce = self.getElement(self._company_l, "xpath")
        # self.elementClick("(//button[@title='Clear'])[5]", "xpath")
        sc = self.getElement(self._company_l, "xpath")
        self.elementClick(self._company_l, "xpath")
        # sc.clear()
        self.driver.execute_script("arguments[0].value = ''", self.getElement(self._company_l, "xpath"))
        # self.driver.execute_script("arguments[0].value = '"+senderCompanyName+"'", self.getElement(self._company_l, "xpath"))
        self.sendKeys(senderCompanyName, self._company_l, "xpath")
        time.sleep(5)
        # sc.send_keys(Keys.ARROW_DOWN)
        # sc.send_keys(Keys.ARROW_DOWN)
        sc.send_keys(Keys.ENTER)
        time.sleep(2)

    def editSenderCompany(self,senderCompanyName):
        sc = self.getElement(self._company_l, "xpath")
        sc_val = sc.get_attribute("value")
        self.elementClick(self._company_l, "xpath")
        self.driver.execute_script("arguments[0].value = ''", self.getElement(self._company_l, "xpath"))
        # self.driver.execute_script("arguments[0].value = '"+senderCompanyName+"'", self.getElement(self._company_l, "xpath"))
        self.sendKeys(senderCompanyName, self._company_l, "xpath")
        time.sleep(2)
        sc.send_keys(Keys.ARROW_DOWN)
        sc.send_keys(Keys.ARROW_DOWN)
        sc.send_keys(Keys.ENTER)
        time.sleep(2)

    def checkSenderAddressClickable(self):
        sa = self.getElement(self._company_l, "xpath")
        sa_clickable = sa.is_enabled()
        if not sa_clickable:
            return False
        else:
            return True

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
        postcodeText_l = postcode_l.text
        print(postcodeText_l)
        # print(type(postcodeText_l))
        if postcode_l.is_displayed():
            return True
        else:
            return False


    def enterSenderOpenTime(self, openTime):
        if openTime:
            self.waitForElement(self._open_time_l, "xpath")
            self.sendKeys(openTime, self._open_time_l, "xpath")

    def enterSenderClosedTime(self, closedtime):
        if closedtime:
            self.waitForElement(self._close_time_l, "xpath")
            self.sendKeys(self._close_time_l, "xpath")



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

    def editSenderDetailsCompanyNameAndCheckRequiredFields(self,senderCompanyName):
        _r1 = False
        self.sendKeys("a", self._company_l, "xpath")
        self.editPopUpWindow()
        self.enterSenderCompany(senderCompanyName=senderCompanyName)
        _r1 = self.checkSenderAddressType()
        _r1 = self.checkSenderRoad()
        _r1 = self.checkSenderStreet()
        _r1 = self.checkSenderCity()
        _r1 = self.checkSenderPostCode()
        if _r1:
            return True
        else:
            return False

    def verifiedaccount_l(self):
        va = self.getElement(self._street_l, "xpath")
        disabled_attribute = va.get_attribute("disabled")
        if disabled_attribute == "true" or disabled_attribute == "disabled":
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
    def enterSenderDetails(self, senderNewAddress='', senderCompanyName='', lot='', openTime='',
                           closedtime='', specialInstructions='', charges=''):
        self.enterSenderAddress(senderNewAddress)
        self.enterSenderCompany(senderCompanyName)
        self.enterSenderLot(lot)
        self.enterSenderOpenTime(openTime)
        self.enterSenderClosedTime(closedtime)
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
        rc = self.getElement(self._company_r, "xpath")
        self.driver.execute_script("arguments[0].value = ''", self.getElement(self._company_r, "xpath"))
        self.sendKeys(senderCompanyName, self._company_r, "xpath")
        time.sleep(5)
        # rc.send_keys(Keys.ARROW_DOWN)
        # rc.send_keys(Keys.ARROW_DOWN)
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


    def enterReceiverOpenTime(self, openTime):
        if openTime:
            self.waitForElement(self._open_time_r, "xpath")
            self.sendKeys(openTime, self._open_time_r, "xpath")

    def enterReceiverClosedTime(self, closedtime):
        if closedtime:
            self.waitForElement(self._close_time_r, "xpath")
            self.sendKeys(self._close_time_r, "xpath")


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
        self.enterReceiverOpenTime(openTime)
        self.enterReceiverClosedTime(closedtime)
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

    def enterVolumeUnit_1(self, dunit):  # select type
        if dunit:
            self.waitForElement(self._volume_unit1, "xpath")
            self.sendKeys(dunit, self._volume_unit1, "xpath")

    def enterItem_1_enterCommodity_1 (self, item, commodity): #### DO NOOOT CHANGE THE CODE FLOW> ITS WORKING!!!!
        self.waitForElement(self._item1, "xpath")
        it1 = self.getElement(self._item1, "xpath")
        self.elementClick(self._item1, "xpath")
        self.sendKeys(item, self._item1, "xpath")
        # self.driver.execute_script("arguments[0].value = '" + item + "'", it1)
        # it1.send_keys(Keys.ARROW_DOWN)
        # it1.send_keys(Keys.ARROW_DOWN)
        # it1.send_keys(Keys.ENTER)
        self.action.move_to_element(it1).send_keys(Keys.RETURN).perform()
        time.sleep(4)
        it_val = self.getElement(self._item1, "xpath").get_attribute("value")
        if it_val is '':
            print("Item not yet selected")
            return
        cm1 = self.getElement(self._commodity1, "xpath")
        self.elementClick(self._commodity1, "xpath")
        self.sendKeys(commodity, self._commodity1, "xpath")
        time.sleep(2)
        cm1.send_keys(Keys.ARROW_DOWN)
        cm1.send_keys(Keys.ARROW_DOWN)
        cm1.send_keys(Keys.ENTER)

    def enterCommodity_1(self, commodity):
        self.waitForElement(self._item1, "xpath")
        it_val = self.getElement(self._item1, "xpath").get_attribute("value")
        if it_val is '':
            print("Item not yet selected")
            return
        cm1 = self.getElement(self._commodity1, "xpath")
        self.elementClick(self._commodity1, "xpath")
        self.sendKeys(commodity, self._commodity1, "xpath")
        time.sleep(2)
        cm1.send_keys(Keys.ARROW_DOWN)
        cm1.send_keys(Keys.ARROW_DOWN)
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
        self.elementClick("//div/p[normalize-space() = 'Consignment Lines']", "xpath")

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
            it2 = self.getElement(self._item2, "xpath")
            self.sendKeys(item, self._item2, "xpath")
            time.sleep(2)
            it2.send_keys(Keys.ARROW_DOWN)
            it2.send_keys(Keys.ARROW_DOWN)
            it2.send_keys(Keys.ENTER)

    def enterCommodity_2(self, commodity):
        if commodity:
            self.waitForElement(self._commodity2, "xpath")
            cmd2 = self.getElement(self._commodity2, "xpath")
            self.elementClick(self._commodity2, "xpath")
            self.sendKeys(commodity, self._commodity2, "xpath")
            time.sleep(2)
            cmd2.send_keys(Keys.ARROW_DOWN)
            cmd2.send_keys(Keys.ARROW_DOWN)
            cmd2.send_keys(Keys.ENTER)

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
        reg_res = re.findall(r'[\d\.\d]+', tw.text)
        print(reg_res[0])
        res = round(float(reg_res[0]), 3)
        return res

    def findTotalVolume(self): #'[\d\.\d]+'
        time.sleep(3)
        self.elementClick(self._line_number, "xpath")
        self.waitForElement(self._total_volume)
        tv = self.getElement(self._total_volume)
        reg_res = re.findall(r'[\d\.\d]+', tv.text)
        print(reg_res[0])
        res = round(float(reg_res[0]), 3)
        return res

    def enterConsignmentLine_1(self, services1, item1, commodity1, quantity1, weight1,
                               volume1):  # , weightUnit1, dunit1, containerNumber1, agency1, description1, length1, width1, height1, dg1
        self.enterServices_1(services1)
        # self.enterWeightUnit_1(weightUnit1)
        # self.enterVolumeUnit_1(dunit1)
        self.enterItem_1_enterCommodity_1(item1, commodity1)
        time.sleep(2)
        # self.enterCommodity_1(commodity1)
        time.sleep(2)
        # self.enterDescription_1(description1)
        self.enterQuantity_1(quantity1)
        self.enterWeight_1(weight1)
        enabled = self.checkEstimatePriceBtnDisabled()
        self.enterVolume_1(volume1)
        return enabled
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
        if it1.is_displayed() and len(addrtypeText_r) > 0:
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
        if cm1.is_displayed() and len(addrtypeText_r) > 0:
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
        if qu1.is_displayed() and len(addrtypeText_r)>0:
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
        self.waitForElement(self._volume_unit1, "xpath")
        vu = self.getElement(self._volume_unit1, "xpath")
        vu_input = vu.find_element(By.XPATH, "following-sibling::*[1]")
        vu_val = vu_input.get_attribute("value")
        if vu_val == "MM":
            return True
        else:
            self.log.error("### Dimension Unit is Not Correct!!!")
            return False

    def checkEstimatePriceBtnDisabled(self):
        ep = self.getElement("//button[normalize-space()='Estimate Price']", "xpath")
        if ep.is_enabled():
            return True
        else:
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

    def calctotalItem(self):
        pass

    def calctotalweight(self):
        sum = 0.00
        wt = self.getElement(self._weight1, "xpath").get_attribute("value")
        qu = self.getElement(self._quantity1, "xpath").get_attribute("value")
        wt = float(wt)
        wt_f = "{:.2f}".format(wt)
        sum = sum + round(float(wt_f), 2)
        sum = sum * int(qu)

        print(int(qu))
        if self.isElementPresent(self._weight2, "xpath"):
            wt2 = self.getElement(self._weight2, "xpath").get_attribute("value")
            Wt2 = round(float(wt2), 2)
            qu2 = self.getElement(self._quantity2, "xpath").get_attribute("value")
            sum = round(sum + (Wt2 * int(qu2)), 2)
            print(Wt2, int(qu2))
        sum = round(sum, 2)
        print(sum)
        return sum

    def calctotalvolume(self):
        v_sum = 0.00
        rr = 0.00
        vol = self.getElement(self._volume1, "xpath").get_attribute("value")
        qu = self.getElement(self._quantity1, "xpath").get_attribute("value")
        res1 = v_sum + round(float(vol), 2)
        sum = res1 * int(qu)
        sum = round(sum, 2)
        print("Sum ", sum)
        if self.isElementPresent(self._weight2, "xpath"):
            vl = self.getElement(self._volume2, "xpath").get_attribute("value")
            vol2 = round(float(vl), 2)
            qu2 = self.getElement(self._quantity2, "xpath").get_attribute("value")
            rr = round(vol2 * int(qu2), 2)
            print("rr ", rr)
        res = sum + rr
        res = round(res, 2)
        print("res", res)
        time.sleep(2)
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


    '''SELL RATING'''

    def checkSRGenerated(self):
        self.waitForElement(self._estimate_price, "xpath")
        if self.getElement("//button[normalize-space()='Estimate Price']", "xpath").is_enabled():
            self.log.info("### Sell Rate Not generated!!!")
            self.enterSellRating()
            return False
        else:
            tsr = self.getElement(self._estimated_sell_rate, "xpath").get_attribute("value")
            print(tsr)
            if float(tsr) == 0.00: # or tsr is None
                self.log.info("### Estimated Rate value is 0.0!!!")
                print(tsr)
                return False
            else:
                # print(tsr)
                self.log.info("Rate Estimated!!!")
                print(tsr)
                val2 = True
                return val2

    def clickGenerateSR(self): #//div[@id='11']/div[normalize-space()='Rate calculated successfully']
        self.waitForElement(self._estimate_price, "xpath")
        if self.getElement(self._estimate_price, "xpath").is_enabled():
            self.elementClick(self._estimate_price, "xpath")
        if self.isElementPresent("//*/text()[normalize-space(.)='Rate calculated successfully']/parent::*", "xpath"):
            self.log.info("Price Estimated!!!")
        else:
            self.log.error("### Price Not Estimated!!!")
            self._error_logs.append("### Price Not Estimated!!!")
        # if self.isElementPresent("//*[contains(normalize-space(text()), 'No location found')]/parent::*", "xpath"):
        #     self.log.info("### No Location Found Error ....")
        #     self._error_logs.append("### No Location Found Error ....")
        # if self.isElementPresent("//*[contains(normalize-space(text()), 'Customer')]/parent::*", "xpath"):
        #     self.log.info("### Customer Error ....")
        #     self._error_logs.append("### Customer Error ....")
        # if self.isElementPresent("//*[contains(normalize-space(text()), 'General')]/parent::*", "xpath"):
        #     self.log.info("### General Error ....")
        #     self._error_logs.append("### General Error ....")

        if self.isElementPresent("//div[@id='16']", "xpath"):
            self.log.info("### No Location Found Error ....")
            self._error_logs.append("### No Location Found Error ....")
        if self.isElementPresent("//div[@id='21']", "xpath"):
            self.log.info("### Customer Metro Error ....")
            self._error_logs.append("### Customer Metro Error ....")
        if self.isElementPresent("//div[@id='20']", "xpath"):
            self.log.info("### Customer Sell Error ....")
            self._error_logs.append("### Customer Sell Error ....")
        if self.isElementPresent("//div[@id='19']", "xpath"):
            self.log.info("### Customer Schedule Error ....")
            self._error_logs.append("### Customer Schedule Error ....")
        if self.isElementPresent("//div[@id='22']", "xpath"):
            self.log.info("### General Schedule Error ....")
            self._error_logs.append("### General Schedule Error ....")

    def returnErrorLogs(self):
        # [self.log.error(i)for i in self._error_logs]
        return self._error_logs


    def clickPricingNotes(self, pricingNotes):
        if pricingNotes:
            self.elementClick(self._pricing_notes, "xpath")
            # enabled = self.getElement("//div[3]/div/div/div/div/div/div/div[2]/div[2]/button", "xpath").is_enabled()
            self._pn_f = self.isElementPresent(
                "(//span[normalize-space() = 'Atleast 1 Pricing Notes Required']", "xpath")
            if not self._pn_f:
                self.log.error("###First Pricing Note is Required - Not Working!!!")
            self.elementClick("//textarea[@id='wayne_id_Pricing Notes']", "xpath")
            self.sendKeys(pricingNotes, "//textarea[@id='wayne_id_Pricing Notes']", "xpath")
            self.elementClick("//*/text()[normalize-space(.)='Save']/parent::*", "xpath")
            self.elementClick("(.//*[normalize-space(text()) and normalize-space(.)='Save'])[1]/following::div[1]/button",
                              "xpath")

    # connote anSR quotedPrice noCharge pricingNotes cancelled
    def checkGSR(self):
        _gs = self.getElement(
            "//div[@id='root']/div/main/div[2]/div[3]/div[2]/div/div[2]/div/div[2]/div/button", "xpath").is_enabled()
        return _gs

    def enterSellRating(self):
        self.clickGenerateSR()

    def enterSellRateFields(self, pricingNotes):
        self.clickPricingNotes(pricingNotes)

    def checkSellRateFields(self):
        self.waitForElement("(.//*[normalize-space(text()) and normalize-space(.)='Estimated Sell Rate'])[2]/following::*[name()='svg'][2]", "xpath")
        self.elementClick("(.//*[normalize-space(text()) and normalize-space(.)='Estimated Sell Rate'])[2]/following::*[name()='svg'][2]", "xpath")
        data_stored = self.isElementPresent("(.//*[normalize-space(text()) and normalize-space(.)='Date Created'])[1]/following::td[1]", "xpath")
        self.elementClick("(.//*[normalize-space(text()) and normalize-space(.)='Save'])[1]/following::div[1]/button", "xpath")
        if data_stored:
            return True
        else:
            return False

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
            self.log.error("### Insurance Field is EMPTY!!!")
            return False

    def clickAuthorityToLeave(self, atl):
        if atl:
            self.waitForElement("//div[2]/div/div/div/div/textarea", "xpath")
            self.elementClick(self._authority_to_leave, "xpath")
            time.sleep(1)
            reqd = self.isElementPresent("//span[normalize-space()='Atleast 1 Authority To Leave Notes Required']", "xpath")
            # enabled_v = self.getElement(
            #     "(.//*[normalize-space(text()) and normalize-space(.)='Atleast 1 Authority To Leave Notes Required'])[1]/preceding::div[1]", "xpath")
            # enabled = enabled_v.is_enabled()
            if not reqd:
                self.log.error("###Authority To Leave first note is Required - Not Working!!!")
            self.waitForElement("//div[3]/div/div/div/div/div/div/div/div/div/div/textarea", "xpath")
            self.elementClick("//div[3]/div/div/div/div/div/div/div/div/div/div/textarea", "xpath")
            self.sendKeys(atl, "//div[3]/div/div/div/div/div/div/div/div/div/div/textarea", "xpath")
            self.elementClick("//*/text()[normalize-space(.)='Save']/parent::*", "xpath")
            self.elementClick("(.//*[normalize-space(text()) and normalize-space(.)='Save'])[1]/following::div[1]/button", "xpath")
    def checkAuthorityToLeave(self):
        self.waitForElement("//button[@tabindex='92']", "xpath")
        self.elementClick("//button[@tabindex='92']", "xpath")
        # ele_pre = self.isElementPresent("(.//*[normalize-space(text()) and normalize-space(.)='Date Created'])[1]/following::td[1]/parent::*", "xpath")
        ele = self.getElement("(.//*[normalize-space(text()) and normalize-space(.)='Date Created'])[1]/following::td[1]", "xpath")
        ele_val = ele.text
        print(ele_val)
        if len(ele_val) > 0:
            self.log.info("Authority to Leave Note is present!!!")

            return True
        else:
            self.log.error("### Authority to Leave Note is NOT STORED!!!")
            return False

    def clickCustomerNotes(self, cn):
        if cn:
            self.waitForElement("//div[2]/div/div/div/div/textarea", "xpath")
            self.elementClick(self._customer_notes)
            time.sleep(1)
            reqd = self.isElementPresent("//div[normalize-space()='Atleast 1 Customer Notes Required']", "xpath")
            # enabled = self.getElement(
            #     "//div[3]/div/div/div/div/div/div/div[2]/div[2]/button", "xpath").is_enabled()
            if not reqd :
                self.log.error("###Customer Notes:  first note is Required - Not Working!!!")
            self.elementClick("//div[3]/div/div/div/div/div/div/div/div/div/div/textarea", "xpath")
            self.sendKeys(cn, "//div[3]/div/div/div/div/div/div/div/div/div/div/textarea", "xpath")
            self.elementClick("//*/text()[normalize-space(.)='Save']/parent::*", "xpath")
            self.elementClick("(.//*[normalize-space(text()) and normalize-space(.)='Save'])[1]/following::div[1]/button", "xpath")

    def checkCustomerNotes(self):
        self.waitForElement("//button[@tabindex='96']", "xpath")
        self.elementClick("//button[@tabindex='96']", "xpath")
        ele_pre = self.isElementPresent("(.//*[normalize-space(text()) and normalize-space(.)='Date Created'])[1]/following::td[1]/parent::*", "xpath")
        if ele_pre:
            self.log.info("Customer Notes stored!!")
            return True
        else:
            self.log.error("### Customer Notes Not Stored!!!")
            return False

    def enterSpecialInstructionsDescription(self, si):
        if si:
            self.elementClick(self._special_instruction_ai, "xpath")
            self.sendKeys(si, self._special_instruction_ai, "xpath")

    def checkSpecialInstructionDescription(self):
        pass
    def clickGeneralDocuments(self, genDoc):
        pass

    # insurance atl dgAI podUploaded christellNotes si

    def enterAdditionalInformation(self, atl, cn):
        self.clickAuthorityToLeave(atl)
        self.clickCustomerNotes(cn)
        # self.enterSpecialInstructionsDescription(si)

    def checkAdditionalInformation(self):
        res = []
        res.append(self.checkAuthorityToLeave())
        res.append(self.checkCustomerNotes())
        # res.append(self.checkSpecialInstructionDescription())
        if False in res:
            return False
        else:
            return True

    '''FOOTERS'''


    def clickCreateQuote(self):
        self.waitForElement(self._create_quote, "xpath")
        ccb = self.getElement(self._create_quote, "xpath").is_enabled()
        if ccb:
            self.elementClick(self._create_quote, "xpath")
            time.sleep(5)
            cc = self.verifyPageTitle("Express Cargo Ltd. | ESTIMATED QUOTE")
            if cc:
                self.log.info("QUOTE CREATED!!!")
                return True
            else:
                self.log.error("### ERROR IN QUOTE CREATION!!!!")
                return False
        else:
            return False

    ''' Scroll Window'''
    def scrollWindowDown(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


