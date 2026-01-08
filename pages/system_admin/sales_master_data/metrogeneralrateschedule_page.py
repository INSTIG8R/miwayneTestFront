import re
import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver import Keys
from datetime import datetime

from selenium.webdriver.support.select import Select


class MetroGeneralRSchedulePage(BasePage):
    log = cl.customLogger(logging.DEBUG)
    filter_field = []
    filter_field_val = None
    mapps = {
        "origin": 2,
        "destination": 3,
        "service": 6,
        "effective_date": 13,
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _origin = "//input[@id='wayne_id_ORIGIN']"
    _destination = "//input[@id='wayne_id_DESTINATION']"
    _service_type = "//input[@id='wayne_id_SERVICE TYPE']"
    _applied_charge = "//input[@id = 'wwayne_id_APPLIED CHARGES']"
    _effective_date = "//input[@id='wayne_id_EFFECTIVE DATE FROM']"
    _effective_date_to = "//input[@id='wayne_id_EFFECTIVE DATE TO']"
    _gri_applied = "//div[@id='wayne_id_GRI APPLIED']"
    _inactive_schedule = "//input[@id='wayne_id_INACTIVE SCHEDULES']"

    _find_btn = "//div/button[@id='wayne_id_Find, ']"
    _clear_filter_btn = "//div/button[@id='wayne_id_Clear, ']"


    _create_new_btn = "(.//*[normalize-space(text()) and normalize-space(.)='Clear'])[1]/following::*[name()='svg'][1]"
    _insideform_goback_btn = "wayne_id_Go back, "
    _insideform_save_btn = "wayne_id_Save, "

    # footers
    # _page_size = "//div[@tabindex='0'][@id='wayne_id_Page Size']"
    _page_total = "//p[@id = 'wayne_id_Current Count']"
    _total_count = "wayne_id_TOTAL Count"

    def verifyMetroGeneralRScheduleTitle(self):
        self.driver.execute_script("document.body.style.zoom='70%'")
        return self.verifyPageTitle("Express Cargo Ltd. | Metro General Cost Rate Schedule")

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

    def enterEffectiveDateTo(self, effectiveDateTo):
        if not effectiveDateTo:
            return
        self.filter_field.append("effective_date to")
        self.filter_field_val = effectiveDateTo
        self.waitForElement(self._effective_date_to, "xpath")
        self.elementClick(self._effective_date_to, "xpath")
        self.sendKeys(effectiveDateTo, self._effective_date_to, "xpath")
        time.sleep(3)
        ca = self.getElement(self._effective_date_to, "xpath")
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
        self.find()

    def find_schedule(self, accountName='', origin='', destination='', service='', effectiveDate='',
                      effectiveDateTo='', activity='', ):
        # remove filters first
        working = True
        self.waitForElement(self._clear_filter_btn, "xpath")
        if self.isElementPresent(self._clear_filter_btn, "xpath"):
            self.clearFilter()
        self.enterOrigin(origin)
        self.enterDestination(destination)
        self.clickService(service)
        self.enterEffectiveDate(effectiveDate)
        self.enterEffectiveDateTo(effectiveDateTo)
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
        if self.isElementPresent("//p[normalize-space()='No records to display']", "xpath"):
            self.log.info("#### SEARCHED ITEM IS NOT FOUND!!! ####")
            return False
        first_row = self.getElement(
            "//div[@id='root']/div/main/div[2]/div[2]/div[2]/div/table/tbody/tr/td[" + str(col) + "]/span", "xpath")
        col_values.append(first_row.text)
        # if self.isElementPresent(
        #         "//div[@id='root']/div/main/div[2]/div[2]/div[2]/div/table/tbody/tr[7]/td[" + str(col) + "]/span",
        #         "xpath"):
        #     sevnth_row = self.getElement(
        #         "//div[@id='root']/div/main/div[2]/div[2]/div[2]/div/table/tbody/tr[7]/td[" + str(col) + "]/span",
        #         "xpath")
        # else:
        #     sevnth_row = self.getElement(
        #         "//div[@id='root']/div/main/div[2]/div[2]/div[2]/div/table/tbody/tr[2]/td[" + str(col) + "]/span",
        #         "xpath")
        # col_values.append(sevnth_row.text)
        # if self.isElementPresent(
        #         "//div[@id='root']/div/main/div[2]/div[2]/div[2]/div/table/tbody/tr[15]/td[" + str(col) + "]/span",
        #         "xpath"):
        #     fiftnth_row = self.getElement(
        #         "//div[@id='root']/div/main/div[2]/div[2]/div[2]/div/table/tbody/tr[15]/td[" + str(col) + "]/span",
        #         "xpath")
        # else:
        #     fiftnth_row = self.getElement(
        #         "//div[@id='root']/div/main/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[" + str(col) + "]/span",
        #         "xpath")
        # col_values.append(fiftnth_row.text)
        # print(col_values)
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
        edit_btn = "//div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/button[1]/*[name()='svg'][1]"

        edit_ok = []
        calc_method_field = "//input[@id='wayne_id_CALCULATION METHOD']"
        min_rate_field = "//input[@id='wayne_id_MINIMUM RATE']"
        self.waitForElement(self._total_count)
        self.elementClick(edit_btn, "xpath")
        self.waitForElement(self._origin, "xpath")
        calc_methd_bool = not self.getElement(calc_method_field, "xpath").is_enabled()
        print(calc_methd_bool)
        edit_ok.append(not self.getElement(calc_method_field, "xpath").is_enabled())
        origin_val = self.getElement(self._origin, "xpath").text
        destination_val = self.getElement(self._destination, "xpath").text
        service_val = self.getElement(self._service_type, "xpath").text
        self.waitForElement("//input[@id='wayne_id_schedule type']", "xpath")
        schedule = self.getElement("//input[@id='wayne_id_schedule type']", "xpath")
        schedule_val = schedule.text
        # ratio_w_v_val = self.getElement("//div[@id='wayne_id_RATIO (W/V)']", "xpath").text
        vol_val = self.getElement("//input[@id='wayne_id_MINIMUM VOLUME']", "xpath").text
        rate_val = self.getElement("//input[@id='wayne_id_Rate']", "xpath").text

# ADD NOTES SECTION AND DATES SECTION.
        self.elementClick(self._origin, "xpath")
        time.sleep(2)
        self.elementClick("//div[@name='originLocation']//button[@title='Clear']//*[name()='svg']", "xpath")
        self.sendKeys(origin_val, self._origin, "xpath")
        self.getElement(self._origin, "xpath").send_keys(Keys.UP)
        self.getElement(self._origin, "xpath").send_keys(Keys.UP)
        self.getElement(self._origin, "xpath").send_keys(Keys.ENTER)
        time.sleep(1.5)
        self.elementClick(self._destination, "xpath")
        time.sleep(1.25)
        self.elementClick("//div[@name='destinationLocation']//button[@title='Clear']//*[name()='svg']", "xpath")
        self.sendKeys(destination_val, self._destination, "xpath")
        self.getElement(self._destination, "xpath").send_keys(Keys.UP)
        self.getElement(self._destination, "xpath").send_keys(Keys.UP)
        self.getElement(self._destination, "xpath").send_keys(Keys.ENTER)
        time.sleep(1.25)
        self.elementClick(self._service_type, "xpath")
        time.sleep(2)
        self.elementClick(
            "//div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/button[1]/*[name()='svg'][1]",
            "xpath")
        self.sendKeys(service_val, self._service_type, "xpath")
        self.getElement(self._service_type, "xpath").send_keys(Keys.ENTER)
        time.sleep(2)
        self.elementClick("//input[@id='wayne_id_schedule type']", "xpath")
        self.elementClick(
            "//div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/button[1]/*[name()='svg'][1]",
            "xpath")
        self.sendKeys(schedule_val, "//input[@id='wayne_id_schedule type']", "xpath")
        self.getElement("//input[@id='wayne_id_schedule type']", "xpath").send_keys(Keys.ENTER)
        time.sleep(2)

        # self.driver.execute_script("arguments[0].value = ''", self.getElement("//div[@id='wayne_id_RATIO (W/V)']", "xpath"))
        # self.sendKeys(ratio_w_v_val, "//div[@id='wayne_id_RATIO (W/V)']", "xpath")
        # time.sleep(2)
        vol:str = "//input[@id='wayne_id_MINIMUM VOLUME']"
        self.elementClick("//input[@id='wayne_id_MINIMUM VOLUME']", "xpath")
        self.driver.execute_script("arguments[0].value = '';", self.getElement("//input[@id='wayne_id_MINIMUM VOLUME']", "xpath"))
        self.sendKeys(vol_val, "//input[@id='wayne_id_schedule type']", "xpath")

        self.elementClick("//input[@id='wayne_id_Rate']", "xpath")
        self.driver.execute_script("arguments[0].value = '';", self.getElement("//input[@id='wayne_id_Rate']", "xpath"))
        self.sendKeys(rate_val, "//input[@id='wayne_id_Rate']", "xpath")
        time.sleep(2)
        # min_hrs_asterisk = self.isElementPresent("//div/label[@id='wayne_id_min hours-label']/span", "xpath")
        # if min_hrs_asterisk:
        #     # self.driver.execute_script("arguments[0].value = ''", self.getElement("//input[@id='wayne_id_min hours']", "xpath"))
        #     self.getElement("//input[@id='wayne_id_min hours']", "xpath").clear()
        #     self.sendKeys(2, "//input[@id='wayne_id_min hours']", "xpath")
        edit_ok.append(not self.getElement("//input[@id='wayne_id_MINIMUM RATE']", "xpath").is_enabled())
        self.elementClick("//button[@id='wayne_id_Save, ']", "xpath")
        edit_ok.append(self.isElementPresent("//div[contains(normalize-space(text()), 'Metro Schedule updated Successfully')]/parent::*/parent::*", "xpath"))
        print(edit_ok, all(edit_ok))
        return all(edit_ok)

