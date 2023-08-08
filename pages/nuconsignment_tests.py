# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class NewconsignmentTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.blazedemo.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_newconsignment_tests(self):
        driver = self.driver
        # Label: Test
        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1536,745 | ]]
        driver.get("https://stage.test-wayne.com/consignment/new")
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"CONSIGNMENT NOTE *\"])]").click()
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"CONSIGNMENT NOTE *\"])]").clear()
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"CONSIGNMENT NOTE *\"])]").send_keys("FATIN01")
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"ACCOUNT NAME *\"])]").click()
        driver.find_element_by_xpath("//*[text() = \"4WD BITS\"]").click()
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"ACCOUNT NAME *\"])]").clear()
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"ACCOUNT NAME *\"])]").send_keys("4WD BITS")
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"STATUS *\"])]").click()
        driver.find_element_by_xpath("//*[text() = \"DELIVERED\"]").click()
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"STATUS *\"])]").clear()
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"STATUS *\"])]").send_keys("DELIVERED")
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"COMPANY *\"])]").click()
        driver.find_element_by_xpath("//*[text() = \"4WD BITSAFLORDLAND CANVAS AND SAILSAFLORDLAND CANVAS AND SAILSAFLORDLAND CANVAS AND SAILS - 2, NICCOL AVENUE, NARROW NECK, AUCKLAND, AUCKLAND, 0624, NEW ZEALAND\"]").click()
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"COMPANY *\"])]").clear()
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"COMPANY *\"])]").send_keys("4WD BITSaFLORDLAND CANVAS AND SAILSaFLORDLAND CANVAS AND SAILSaFLORDLAND CANVAS AND SAILS")
        driver.find_element_by_css_selector("div.MuiInputBase-root.MuiOutlinedInput-root.jss944.MuiInputBase-fullWidth.Mui-focused.Mui-focused.MuiInputBase-formControl.MuiInputBase-adornedEnd.MuiOutlinedInput-adornedEnd.MuiInputBase-marginDense.MuiOutlinedInput-marginDense > #wayne_id_Company").click()
        driver.find_element_by_xpath("//*[text() = \"DAVID STEVENSON AUTO C/O BASCIK TRANSPORT INVERCARGILL - B, 1, FOX STREET, WEST INVERCARGILL, INVERCARGILL, SOUTHLAND, 9810, NEW ZEALAND\"]").click()
        driver.find_element_by_css_selector("div.MuiInputBase-root.MuiOutlinedInput-root.jss944.MuiInputBase-fullWidth.Mui-focused.Mui-focused.MuiInputBase-formControl.MuiInputBase-adornedEnd.MuiOutlinedInput-adornedEnd.MuiInputBase-marginDense.MuiOutlinedInput-marginDense > #wayne_id_Company").clear()
        driver.find_element_by_css_selector("div.MuiInputBase-root.MuiOutlinedInput-root.jss944.MuiInputBase-fullWidth.Mui-focused.Mui-focused.MuiInputBase-formControl.MuiInputBase-adornedEnd.MuiOutlinedInput-adornedEnd.MuiInputBase-marginDense.MuiOutlinedInput-marginDense > #wayne_id_Company").send_keys("DAVID STEVENSON AUTO C/O BASCIK TRANSPORT INVERCARGILl")
        driver.find_element_by_css_selector("div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-md-12 > div.MuiAutocomplete-root.MuiAutocomplete-hasClearIcon > div.MuiFormControl-root.MuiTextField-root.jss943.MuiFormControl-fullWidth > div.MuiInputBase-root.MuiOutlinedInput-root.jss944.MuiInputBase-fullWidth.MuiInputBase-formControl.MuiInputBase-adornedEnd.MuiOutlinedInput-adornedEnd.MuiInputBase-marginDense.MuiOutlinedInput-marginDense > div.MuiAutocomplete-endAdornment > button.MuiButtonBase-root.MuiIconButton-root.MuiAutocomplete-clearIndicator.MuiAutocomplete-clearIndicatorDirty > span.MuiIconButton-label > svg.MuiSvgIcon-root.MuiSvgIcon-fontSizeSmall").click()
        driver.find_element_by_xpath("//*[text() = \"EDIT ADDRESS\"]").click()
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"COMPANY *\"])]").click()
        driver.find_element_by_xpath("//*[text() = \"FLORDLAND CANVAS AND SAILS - 23, FOX STREET, INVERCARGILL, SOUTHLAND, 9810, NEW ZEALAND\"]").click()
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"COMPANY *\"])]").clear()
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"COMPANY *\"])]").send_keys("FLORDLAND CANVAS AND SAILS")
        driver.find_element_by_id("wayne_id_Address Type").click()
        Select(driver.find_element_by_id("wayne_id_Address Type")).select_by_visible_text("BUSINESS")
        driver.find_element_by_xpath("//*[text() = \"EDIT ADDRESS\"]").click()
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"ROAD NO *\"])]").click()
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"ROAD NO *\"])]").clear()
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"ROAD NO *\"])]").send_keys("22")
        driver.find_element_by_xpath(u"//*[text() = \"STREET *\"]").click()
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"STREET *\"])]").clear()
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"STREET *\"])]").send_keys("te anau")
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"CITY *\"])]").click()
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"CITY *\"])]").click()
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"CITY *\"])]").clear()
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"CITY *\"])]").send_keys("Auckland")
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"POST CODE *\"])]").click()
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"POST CODE *\"])]").clear()
        driver.find_element_by_xpath(u"//input[@id=string(//label[text() = \"POST CODE *\"])]").send_keys("9600")
        driver.find_element_by_xpath("//*[text() = \"EDIT ADDRESS\"]").click()
        driver.find_element_by_xpath("//div[@id='root']/div/main/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div/div/div/div/button/span/svg/path").click()
        driver.find_element_by_xpath("//*[text() = \"EDIT ADDRESS\"]").click()
        driver.find_element_by_css_selector("div.MuiInputBase-root.MuiOutlinedInput-root.jss944.MuiInputBase-fullWidth.Mui-focused.Mui-focused.MuiInputBase-formControl.MuiInputBase-adornedEnd.MuiOutlinedInput-adornedEnd.MuiInputBase-marginDense.MuiOutlinedInput-marginDense > #wayne_id_Company").click()
        driver.find_element_by_css_selector("div.MuiInputBase-root.MuiOutlinedInput-root.jss944.MuiInputBase-fullWidth.Mui-focused.Mui-focused.MuiInputBase-formControl.MuiInputBase-adornedEnd.MuiOutlinedInput-adornedEnd.MuiInputBase-marginDense.MuiOutlinedInput-marginDense > #wayne_id_Company").clear()
        driver.find_element_by_css_selector("div.MuiInputBase-root.MuiOutlinedInput-root.jss944.MuiInputBase-fullWidth.Mui-focused.Mui-focused.MuiInputBase-formControl.MuiInputBase-adornedEnd.MuiOutlinedInput-adornedEnd.MuiInputBase-marginDense.MuiOutlinedInput-marginDense > #wayne_id_Company").send_keys("NAT")
        driver.find_element_by_css_selector("div.MuiInputBase-root.MuiOutlinedInput-root.jss944.MuiInputBase-fullWidth.Mui-focused.Mui-focused.MuiInputBase-formControl.MuiInputBase-adornedEnd.MuiOutlinedInput-adornedEnd.MuiInputBase-marginDense.MuiOutlinedInput-marginDense > #wayne_id_Company").send_keys(Keys.ENTER)
        driver.find_element_by_css_selector("div.MuiInputBase-root.MuiOutlinedInput-root.jss944.MuiInputBase-fullWidth.Mui-focused.Mui-focused.MuiInputBase-formControl.MuiInputBase-adornedEnd.MuiOutlinedInput-adornedEnd.MuiInputBase-marginDense.MuiOutlinedInput-marginDense > #wayne_id_Company").clear()
        driver.find_element_by_css_selector("div.MuiInputBase-root.MuiOutlinedInput-root.jss944.MuiInputBase-fullWidth.Mui-focused.Mui-focused.MuiInputBase-formControl.MuiInputBase-adornedEnd.MuiOutlinedInput-adornedEnd.MuiInputBase-marginDense.MuiOutlinedInput-marginDense > #wayne_id_Company").send_keys("NATHAN SORRELL")
        driver.find_element_by_xpath("(//select[@id='wayne_id_Address Type'])[2]").click()
        Select(driver.find_element_by_xpath("(//select[@id='wayne_id_Address Type'])[2]")).select_by_visible_text("RESIDENTIAL")
        driver.find_element_by_xpath("//*[text() = \"EDIT ADDRESS\"]").click()
        driver.find_element_by_xpath("(//input[@id='wayne_id_Road No'])[2]").click()
        driver.find_element_by_xpath("(//input[@id='wayne_id_Road No'])[2]").clear()
        driver.find_element_by_xpath("(//input[@id='wayne_id_Road No'])[2]").send_keys("23")
        driver.find_element_by_css_selector("div.MuiInputBase-root.MuiOutlinedInput-root.jss944.MuiInputBase-fullWidth.Mui-focused.Mui-focused.MuiInputBase-formControl.MuiInputBase-marginDense.MuiOutlinedInput-marginDense > #wayne_id_Street").click()
        driver.find_element_by_css_selector("div.MuiInputBase-root.MuiOutlinedInput-root.jss944.MuiInputBase-fullWidth.Mui-focused.Mui-focused.MuiInputBase-formControl.MuiInputBase-marginDense.MuiOutlinedInput-marginDense > #wayne_id_Street").clear()
        driver.find_element_by_css_selector("div.MuiInputBase-root.MuiOutlinedInput-root.jss944.MuiInputBase-fullWidth.Mui-focused.Mui-focused.MuiInputBase-formControl.MuiInputBase-marginDense.MuiOutlinedInput-marginDense > #wayne_id_Street").send_keys("FOX STREET")
        driver.find_element_by_css_selector("div.MuiInputBase-root.MuiOutlinedInput-root.jss944.MuiInputBase-fullWidth.Mui-focused.Mui-focused.MuiInputBase-formControl.MuiInputBase-marginDense.MuiOutlinedInput-marginDense > #wayne_id_City").click()
        driver.find_element_by_css_selector("div.MuiInputBase-root.MuiOutlinedInput-root.jss944.MuiInputBase-fullWidth.Mui-focused.Mui-focused.MuiInputBase-formControl.MuiInputBase-marginDense.MuiOutlinedInput-marginDense > #wayne_id_City").clear()
        driver.find_element_by_css_selector("div.MuiInputBase-root.MuiOutlinedInput-root.jss944.MuiInputBase-fullWidth.Mui-focused.Mui-focused.MuiInputBase-formControl.MuiInputBase-marginDense.MuiOutlinedInput-marginDense > #wayne_id_City").send_keys("INVERCARGILL")
        driver.find_element_by_xpath("(//input[@id='wayne_id_Post Code'])[2]").click()
        driver.find_element_by_xpath("(//input[@id='wayne_id_Post Code'])[2]").clear()
        driver.find_element_by_xpath("(//input[@id='wayne_id_Post Code'])[2]").send_keys("9810")
        driver.find_element_by_xpath("(//*[text() = \"EDIT ADDRESS\"])[2]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
