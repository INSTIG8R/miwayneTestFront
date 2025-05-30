import re
import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver import Keys
from datetime import datetime

from selenium.webdriver.support.select import Select


class CustomerMetroSRSchedulePage(BasePage):
    log = cl.customLogger(logging.DEBUG)
    filter_field = []
    filter_field_val = None
    mapps = {
        "accountName": 2,
        "origin": 3,
        "destination": 4,
        "service": 7,
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _account_name = "//input[@id='wayne_id_account name']"
    _origin = "//input[@id='wayne_id_ORIGIN']"
    _destination = "//input[@id='wayne_id_DESTINATION']"
    _service_type = "//input[@id='wayne_id_SERVICE TYPE']"
    _applied_charge = "//input[@id = 'wwayne_id_APPLIED CHARGES']"
    _effective_date = "//input[@id='wayne_id_EFFECTIVE DATE']"
    _gri_applied = "//div[@id='wayne_id_GRI APPLIED']"
    _inactive_schedule = "//input[@id='wayne_id_INACTIVE SCHEDULES']"

    _find_btn = "//div/button[@id='wayne_id_Find, ']"
    _clear_filter_btn = "//div/button[@id='wayne_id_Clear, ']"

    _create_new_btn = "(.//*[normalize-space(text()) and normalize-space(.)='Clear'])[1]/following::*[name()='svg'][1]"
    _insideform_goback_btn = "wayne_id_Go back, "
    _edit_btn = "(.//*[normalize-space(text()) and normalize-space(.)='Sell Rate'])[1]/following::*[name()='svg'][4]"

    # footers
    # _page_size = "//div[@tabindex='0'][@id='wayne_id_Page Size']"
    _page_total = "//p[@id = 'wayne_id_Current Count']"
    _total_count = "wayne_id_TOTAL Count"

    def verifyCustomerMetroSRScheduleTitle(self):
        self.driver.execute_script("document.body.style.zoom='70%'")
        return self.verifyPageTitle("Express Cargo Ltd. | Customer Metro Sell Rate Schedule")

    def enterAccountName(self, accountName):
        if not accountName:
            return

        self.filter_field.append("accountName")
        self.filter_field_val = accountName

        try:
            self.waitForElement(self._account_name, "xpath")  # wait function should ensure it's present
            an = self.getElement(self._account_name, "xpath")
            if an is None:
                print("Element not found: account name input field.")
                return

            self.elementClick(self._account_name, "xpath")
            self.sendKeys(accountName, self._account_name, "xpath")

            # Use ARROW navigation after short delay
            time.sleep(2)
            an.send_keys(Keys.ARROW_DOWN)
            an.send_keys(Keys.ARROW_DOWN)
            an.send_keys(Keys.ENTER)

        except Exception as e:
            print(f"Error in enterAccountName: {e}")

    def clickService(self, service):
        if not service:
            return
        self.filter_field.append("service")
        self.filter_field_val = service
        self.waitForElement(self._service_type, "xpath")
        sel = self.getElement(self._service_type, "xpath")
        self.elementClick(self._service_type, "xpath")
        self.sendKeys(service, self._service_type, "xpath")
        time.sleep(2)
        sel.send_keys(Keys.ARROW_DOWN)
        sel.send_keys(Keys.ARROW_DOWN)
        sel.send_keys(Keys.ENTER)

    def enterEffectiveDate(self, effectiveDate):
        if not effectiveDate:
            return
        self.filter_field.append("effective_date")
        self.filter_field_val = effectiveDate
        self.waitForElement(self._effective_date, "xpath")
        self.elementClick(self._effective_date, "xpath")
        self.sendKeys(effectiveDate, self._effective_date, "xpath")
        time.sleep(3)
        ca = self.getElement(self._effective_date, "xpath")
        ca.send_keys(Keys.ENTER)

    def find(self):
        self.waitForElement(self._find_btn, "xpath")
        self.elementClick(self._find_btn, "xpath")

    def enterOrigin(self, origin):
        if not origin:
            return
        self.filter_field.append("origin")
        self.filter_field_val = origin
        self.waitForElement(self._origin, "xpath")
        self.elementClick(self._origin, "xpath")
        self.sendKeys(origin, self._origin, "xpath")
        time.sleep(3)
        pc = self.getElement(self._origin, "xpath")
        pc.send_keys(Keys.ENTER)

    def enterDestination(self, destination):
        if not destination:
            return
        self.filter_field.append("destination")
        self.filter_field_val = destination
        self.waitForElement(self._destination, "xpath")
        self.elementClick(self._destination, "xpath")
        self.sendKeys(destination, self._destination, "xpath")
        time.sleep(3)
        dc = self.getElement(self._destination, "xpath")
        dc.send_keys(Keys.ENTER)

    # //*/text()[normalize-space(.)='YES']/parent::*
    def enterGRIApplied(self, gri):
        if not gri:
            return
        self.filter_field_val = "gri"
        if gri is "YES":
            self.elementClick("//*/text()[normalize-space(.)='YES']/parent::*", "xpath")
        elif gri is "NO":
            self.elementClick("//*/text()[normalize-space(.)='NO']/parent::*", "xpath")

    def clearFilter(self):
        if self.getElement(self._clear_filter_btn, "xpath").is_enabled():
            self.elementClick(self._clear_filter_btn, "xpath")

    def clickInactiveSchedule(self, activity):
        if not activity:
            return
        self.filter_field_val = "activity"
        self.elementClick(self._inactive_schedule, "xpath")

    def find_schedule(self, accountName='', origin='', destination='', service='', gri='',
                      activity='', ):
        # remove filters first
        working = True
        self.waitForElement(self._clear_filter_btn, "xpath")
        if self.isElementPresent(self._clear_filter_btn, "xpath"):
            self.clearFilter()
        self.enterAccountName(accountName)
        self.enterOrigin(origin)
        self.enterDestination(destination)
        self.clickService(service)
        # self.enterEffectiveDate(effectiveDate)
        self.enterGRIApplied(gri)
        self.clickInactiveSchedule(activity)
        time.sleep(2)
        # self.find()
        # print("********************************")
        # print(self.filter_field)
        if len(self.filter_field) == 0:
            return True
        # print(self.filter_field[-1])
        # print("********************************")

        if self.filter_field:
            last_field = self.filter_field[-1]
            mapped_value = self.mapps.get(last_field)

            if mapped_value is not None:
                working = self.findMatch(mapped_value)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return working

    def scrollTableHorizontally(self):
        hScrollTable = self.getElement("//div[@id='root']/div/main/div/div[2]/div[2]/div/table", "xpath")
        self.driver.execute_script("arguments[0].scrollLeft = 1000;", hScrollTable)

    def findMatch(self, col):  # (2,12)
        self.waitForElement(self._total_count)
        # print(col, self.filter_field_val)
        col_values = []
        if self.filter_field_val == "gri" or self.filter_field_val == "activity":
            return True
        if int(col) > 7:
            self.scrollTableHorizontally()
        first_row = self.getElement(
            "//div[@id='root']/div/main/div[2]/div[2]/div[2]/div/table/tbody/tr/td[" + str(col) + "]", "xpath")
        col_values.append(first_row.text)
        sevnth_row = self.getElement(
            "//div[@id='root']/div/main/div[2]/div[2]/div[2]/div/table/tbody/tr[7]/td[" + str(col) + "]", "xpath")
        col_values.append(sevnth_row.text)
        fiftnth_row = self.getElement(
            "//div[@id='root']/div/main/div[2]/div[2]/div[2]/div/table/tbody/tr[15]/td[" + str(col) + "]", "xpath")
        col_values.append(fiftnth_row.text)
        # print(col_values)

        twntith_row = self.getElement(
            "//div[@id='root']/div/main/div[2]/div[2]/div[2]/div/table/tbody/tr[20]/td[" + str(col) + "]", "xpath")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", twntith_row)
        twntith_row_val = twntith_row.get_attribute("innerHTML")
        # print(twntith_row_val)
        col_values.append(twntith_row_val)

        print(col_values, self.filter_field_val)

        def is_date(string):
            try:
                datetime.strptime(string.strip(), "%d/%m/%Y")
                return True
            except ValueError:
                return False

        for itm in col_values:
            print(itm)
            if is_date(itm) and is_date(self.filter_field_val):
                itm_date = datetime.strptime(itm.strip(), "%d/%m/%Y")
                filter_date = datetime.strptime(self.filter_field_val.strip(), "%d/%m/%Y")
                print(itm_date, filter_date)
                if itm_date < filter_date:
                    return False
            else:
                if itm.upper() != self.filter_field_val:
                    return False
        return True

    def infonotpresent(self):
        presence = self.isElementPresent("//td[normalize-space()='No records to display']", "xpath")
        return presence


# -------      EDITING         ----------
# AccountCommodity Schedule updated successfully, toast

    def edit(self):
# store the values and rewrite on fields. save after, then check the toast
        edit_btn = "(.//*[normalize-space(text()) and normalize-space(.)='1UP CARGO LIMITED'])[2]/preceding::*[name()='svg'][4]"
        edit_ok= []
        accnt_field = "//input[@id='wayne_id_account name']"
        calc_method_field = "//input[@id='wayne_id_CALCULATION METHOD']"
        #check they are disabled or not
        self.waitForElement(self._total_count)
        self.elementClick(edit_btn, "xpath")
        self.waitForElement(self._origin, "xpath")
        edit_ok.append(not self.getElement(accnt_field, "xpath").is_enabled())
        calc_methd_bool = not self.getElement(calc_method_field, "xpath").is_enabled()
        print(calc_methd_bool)
        edit_ok.append(not self.getElement(calc_method_field, "xpath").is_enabled())
        origin_val = self.getElement(self._origin, "xpath").text
        destination_val = self.getElement(self._destination, "xpath").text
        service_val = self.getElement(self._service_type, "xpath").text
        self.waitForElement("//input[@id='wayne_id_schedule type']", "xpath")
        schedule = self.getElement("//input[@id='wayne_id_schedule type']", "xpath")
        schedule_val = schedule.text
        vol_val =self.getElement("//input[@id='wayne_id_MINIMUM VOLUME']", "xpath").text
        rate_val = self.getElement("//input[@id='wayne_id_Rate']", "xpath").text

# ADD NOTES SECTION AND DATES SECTION.
        self.driver.execute_script("arguments[0].value = ''", self.getElement(self._origin, "xpath"))
        self.sendKeys(origin_val, self._origin, "xpath")
        time.sleep(2)
        self.driver.execute_script("arguments[0].value = ''", self.getElement(self._destination, "xpath"))
        self.sendKeys(destination_val, self._destination, "xpath")
        time.sleep(2)
        self.driver.execute_script("arguments[0].value = ''", self.getElement(self._service_type, "xpath"))
        self.sendKeys(service_val, self._service_type, "xpath")
        time.sleep(2)
        self.driver.execute_script("arguments[0].value = ''", self.getElement("//input[@id='wayne_id_schedule type']", "xpath"))
        self.sendKeys(schedule_val, "//input[@id='wayne_id_schedule type']", "xpath")
        time.sleep(2)
        self.driver.execute_script("arguments[0].value = ''", self.getElement("//input[@id='wayne_id_MINIMUM VOLUME']", "xpath"))
        self.sendKeys(vol_val, "//input[@id='wayne_id_MINIMUM VOLUME']", "xpath")
        time.sleep(2)
        self.driver.execute_script("arguments[0].value = ''", self.getElement("//input[@id='wayne_id_Rate']", "xpath"))
        self.sendKeys(rate_val, "//input[@id='wayne_id_Rate']", "xpath")
        time.sleep(5)

        self.elementClick("//button[@id='wayne_id_Edit, ']", "xpath")
        edit_ok.append(self.isElementPresent("//div[contains(normalize-space(text()), 'Metro Schedule updated Successfully')]/parent::*/parent::*", "xpath"))
        print(edit_ok, all(edit_ok))
        return all(edit_ok)

