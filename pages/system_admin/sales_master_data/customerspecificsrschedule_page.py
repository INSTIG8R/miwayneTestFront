import re
import time

from flask.globals import app_ctx

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver import Keys
from datetime import datetime

from selenium.webdriver.support.select import Select


class CustomerSSRSchedulePage(BasePage):
    log = cl.customLogger(logging.DEBUG)
    filter_field = []
    filter_field_val = None
    mapps = {
        "accountName": 3,
        "origin": 4,
        "destination": 5,
        "schedule": 6,
        "service": 8,
        "effective_date": 10,
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _account_name = "//input[@id='wayne_id_account name']"
    _origin = "//input[@id='wayne_id_ORIGIN']"
    _destination = "//input[@id='wayne_id_DESTINATION']"
    _service_type = "//input[@id='wayne_id_SERVICE TYPE']"
    _schedule_type = "//input[@id='wayne_id_SCHEDULE Type']"
    _applied_charge = "//input[@id = 'wwayne_id_APPLIED CHARGES']"
    _effective_date_from = "//input[@id='wayne_id_EFFECTIVE DATE FROM']"
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

    def verifyCustomerSSRScheduleTitle(self):
        self.driver.execute_script("document.body.style.zoom='70%'")
        return self.verifyPageTitle("Express Cargo Ltd. | Customer Specific Sell Rate Schedule")

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

    def clickSchedule(self, schedule):
        if not schedule:
            return
        self.filter_field.append("schedule")
        self.filter_field_val = schedule
        self.waitForElement(self._schedule_type, "xpath")
        sel = self.getElement(self._schedule_type, "xpath")
        self.elementClick(self._schedule_type, "xpath")
        self.sendKeys(schedule, self._schedule_type, "xpath")
        time.sleep(2)
        sel.send_keys(Keys.ARROW_DOWN)
        sel.send_keys(Keys.ARROW_DOWN)
        sel.send_keys(Keys.ENTER)

    def enterEffectiveDateFrom(self, effectiveDate):
        if not effectiveDate:
            return
        self.filter_field.append("effective_date")
        self.filter_field_val = effectiveDate
        self.waitForElement(self._effective_date_from, "xpath")
        self.elementClick(self._effective_date_from, "xpath")
        self.sendKeys(effectiveDate, self._effective_date_from, "xpath")
        time.sleep(3)
        ca = self.getElement(self._effective_date_from, "xpath")
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
        time.sleep(1)
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
        time.sleep(2)
        dc = self.getElement(self._destination, "xpath")
        dc.send_keys(Keys.ARROW_UP)
        dc.send_keys(Keys.ARROW_UP)
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

    def find_schedule(self, accountName='', origin='', destination='', service='', scheduleType='', effectiveDateFrom='', effectiveDateTo='', activity='', ):
        # remove filters first
        working = True
        self.waitForElement(self._clear_filter_btn, "xpath")
        if self.isElementPresent(self._clear_filter_btn, "xpath"):
            self.clearFilter()
        self.enterAccountName(accountName)
        self.enterOrigin(origin)
        self.enterDestination(destination)
        self.clickService(service)
        self.clickSchedule(scheduleType)
        self.enterEffectiveDateFrom(effectiveDateFrom)
        self.enterEffectiveDateTo(effectiveDateTo)
        self.clickInactiveSchedule(activity)
        time.sleep(2)
        # self.find()
        # print("********************************")
        # print(self.filter_field)
        if len(self.filter_field) ==0 :
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

    def findMatch(self, col): # (2,12)
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
        first_row = self.getElement("//div[@id='root']/div/main/div[2]/div[2]/div[2]/div/table/tbody/tr/td["+str(col)+"]", "xpath")
        col_values.append(first_row.text)
        if self.isElementPresent("//div[@id='root']/div/main/div[2]/div[2]/div[2]/div/table/tbody/tr[7]/td["+str(col)+"]","xpath"):
            sevnth_row = self.getElement("//div[@id='root']/div/main/div[2]/div[2]/div[2]/div/table/tbody/tr[7]/td["+str(col)+"]", "xpath")
        else:
            sevnth_row = self.getElement(
                "//div[@id='root']/div/main/div[2]/div[2]/div[2]/div/table/tbody/tr[2]/td["+str(col)+"]", "xpath")
        col_values.append(sevnth_row.text)
        if self.isElementPresent("//div[@id='root']/div/main/div[2]/div[2]/div[2]/div/table/tbody/tr[15]/td["+str(col)+"]", "xpath"):
            fiftnth_row = self.getElement("//div[@id='root']/div/main/div[2]/div[2]/div[2]/div/table/tbody/tr[15]/td["+str(col)+"]", "xpath")
        else:
            fiftnth_row = self.getElement(
                "//div[@id='root']/div/main/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td[" + str(col) + "]", "xpath")
        col_values.append(fiftnth_row.text)
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
        edit_btn = "(.//*[normalize-space(text()) and normalize-space(.)='1UP CARGO LIMITED'])[2]/preceding::*[name()='svg'][7]"
        edit_ok= []
        accnt_field = "//input[@id='wayne_id_account name']"
        schedule_field = "//input[@id='wayne_id_SCHEDULE Type']"
        ratio_field = "//div[@id='wayne_id_RATIO (W/V)']/following-sibling::*[1]"
        weight1_field = "(//input[@id='wayne_id_WEIGHT'])[1]"
        volume1_field = "(//input[@id='wayne_id_VOLUME'])[1]"
        weight2_field = "(//input[@id='wayne_id_WEIGHT'])[2]"
        volume2_field = "(//input[@id='wayne_id_VOLUME'])[2]"
        self.waitForElement(self._total_count)
        self.elementClick(edit_btn, "xpath")
        self.waitForElement(self._origin, "xpath")
        edit_ok.append(not self.getElement(accnt_field, "xpath").is_enabled())
        edit_ok.append(not self.getElement(schedule_field, "xpath").is_enabled())
        edit_ok.append(not self.getElement(ratio_field, "xpath").is_enabled())
        edit_ok.append(not self.getElement(weight1_field, "xpath").is_enabled())
        edit_ok.append(not self.getElement(volume1_field, "xpath").is_enabled())
        edit_ok.append(not self.getElement(weight2_field, "xpath").is_enabled())
        edit_ok.append(not self.getElement(volume2_field, "xpath").is_enabled())
        vol2_val = float(self.getElement(volume2_field, "xpath").get_attribute("value"))
        vol1_val = float(self.getElement(volume1_field, "xpath").get_attribute("value"))
        print(vol1_val, vol2_val)
        ratio = round(float(vol2_val / vol1_val),2)
        print("#####################" +str(ratio) + "##################")

        origin_val = self.getElement(self._origin, "xpath").text
        destination_val = self.getElement(self._destination, "xpath").text
        service_val = self.getElement(self._service_type, "xpath").text
        effectivedate_val = self.getElement("//input[@id='wayne_id_EFFECTIVE DATE']", "xpath").text
        rate1 = self.getElement("(//input[@id='wayne_id_RATE'])[1]", "xpath")
        rate2 = self.getElement("(//input[@id='wayne_id_RATE'])[2]", "xpath")
        rate1_val =float(rate1.get_attribute("value"))
        rate2_val = float(rate2.get_attribute("value"))
        min1_val = self.getElement("(//input[@id='wayne_id_MIN CHARGE'])[1]", "xpath").text
        min2_val = self.getElement("(//input[@id='wayne_id_MIN CHARGE'])[2]", "xpath").text

        rate_ratio = round(float(rate2_val/rate1_val),2)
        rate1_asterisk = self.isElementPresent("(//div/label[@id='wayne_id_RATE-label']/span)[1]", "xpath")
        rate2_asterisk = self.isElementPresent("(//div/label[@id='wayne_id_RATE-label']/span)[2]", "xpath")

# ADD NOTES SECTION AND DATES SECTION.
        self.elementClick(self._origin, "xpath")
        time.sleep(2)
        self.elementClick("//div[@name='originLocation']//button[@title='Clear']//*[name()='svg']", "xpath")
        self.sendKeys(origin_val, self._origin, "xpath")
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
            "//div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/button[1]/*[name()='svg'][1]/*[name()='path'][1]",
            "xpath")
        self.sendKeys(service_val, self._service_type, "xpath")
        self.getElement(self._service_type, "xpath").send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.execute_script("arguments[0].value = ''", self.getElement("//input[@id='wayne_id_EFFECTIVE DATE']", "xpath"))
        self.sendKeys(effectivedate_val, "//input[@id='wayne_id_EFFECTIVE DATE']", "xpath")
        time.sleep(2)
        #
        self.elementClick("(// input[@id='wayne_id_RATE'])[1]", "xpath")
        self.driver.execute_script("arguments[0].value = '';", self.getElement("(// input[@id='wayne_id_RATE'])[1]", "xpath"))

        # self.getElement("(// input[@id='wayne_id_RATE'])[1]", "xpath").clear()
        self.sendKeys(rate1_val, "(// input[@id='wayne_id_RATE'])[1]", "xpath")
        print(rate1.get_attribute("value"), rate1_val)
        time.sleep(2)

        self.elementClick("(// input[@id='wayne_id_RATE'])[2]", "xpath")
        self.driver.execute_script("arguments[0].value = '';", self.getElement("(// input[@id='wayne_id_RATE'])[2]", "xpath"))
        # self.getElement("(//input[@id='wayne_id_RATE'])[2]", "xpath").clear()
        self.sendKeys(rate2_val, "(// input[@id='wayne_id_RATE'])[2]", "xpath")
        print(rate2.get_attribute("value"), rate2_val)
        time.sleep(2)
        if (rate1_asterisk and rate2_asterisk) and (ratio == rate_ratio):
            edit_ok.append(True)
            self.log.info("Rates are required field, calculation is correct.... Working!")
        else:
            edit_ok.append(False)
            self.log.error("Rates are either not required field (asterisk missing) or calculation is wrong... NOT WORKING!")

        time.sleep(2)
        if (min1_val is None) and (min2_val == "0.00"):
            edit_ok.append(True)
            self.log.info("Min Rate Value 1 missing and min rate value 2 is not ZERO.. Working!!")
        elif (min1_val is None) and (min2_val != "0.00"):
            edit_ok.append(False)
            self.log.error("Min Rate Value 1 missing but min rate value 2 is not ZERO.. NOT Working!!")

        else:
            equal_or_not = (min2_val == min1_val)
            edit_ok.append(equal_or_not)
            self.log.info("Minimum Values Check!! ")
        time.sleep(2)
        self.elementClick("//button[@id='wayne_id_Save, ']", "xpath")

        edit_successfull: bool = self.isElementPresent("//div[contains(normalize-space(text()), 'Customer Schedule Updated Successfully')]/parent::*/parent::*", "xpath")

        print(edit_ok, edit_successfull)
        return edit_successfull

