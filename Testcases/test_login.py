import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from PageObjects.LoginPage import Catelog_list
from PageObjects.LoginPage import sales_list

class Test_1_loginnop:
    baseURL = 'https://admin-demo.nopcommerce.com/'
    username  = 'admin@yourstore.com'
    password = 'admin'
    def test_homepagetitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        assert act_title=='Your store. Login'

    @pytest.mark.skip
    def test_login_1(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=loginpageofnoc(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        assert act_title=='Dashboard / nopCommerce administration'
        time.sleep(8)
    def test_catalog(self,setuplogin):
        self.driver = setuplogin
        aa = Catelog_list(self.driver)
        aa.catelog_elm().click()
        time.sleep(3)
        # self.driver.find_element(By.XPATH,'//*[@id="SearchProductName"]').send_keys('Build your own computer')
        aa.product_elm().click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="SearchProductName"]').send_keys('Build your own computer')
        el = self.driver.find_element(By.XPATH,'//*[@id="SearchWarehouseId"]')
        drp = Select(el)
        drp.select_by_visible_text('Warehouse 1 (New York)')
        self.driver.find_element(By.XPATH,'//*[@id="search-products"]').click()
        time.sleep(5)
    def test_category(self,setuplogin):
        self.driver = setuplogin
        aa = Catelog_list(self.driver)
        aa.catelog_elm().click()
        time.sleep(3)
        aa.category_elm().click()
        self.driver.find_element(By.XPATH,'//*[@id="SearchCategoryName"]').send_keys('Computers')
        el = self.driver.find_element(By.XPATH,'//*[@id="SearchPublishedId"]')
        drp = Select(el)
        drp.select_by_visible_text('Published only')
        self.driver.find_element(By.XPATH,'//*[@id="search-categories"]').click()
        time.sleep(5)
    def test_manufacturer(self,setuplogin):
        self.driver = setuplogin
        aa = Catelog_list(self.driver)
        aa.catelog_elm().click()
        time.sleep(8)
        aa.manufacturer_elm().click()
        self.driver.find_element(By.XPATH,'//*[@id="SearchManufacturerName"]').send_keys('Apple')
        el =  self.driver.find_element(By.XPATH,'//*[@id="SearchPublishedId"]')
        drp = Select(el)
        drp.select_by_visible_text('Published only')
        self.driver.find_element(By.XPATH,'//*[@id="search-manufacturers"]').click()
        time.sleep(3)
    def test_product_Review(self,setuplogin):
        self.driver = setuplogin
        aa = Catelog_list(self.driver)
        aa.catelog_elm().click()
        time.sleep(5)
        aa.product_reviews_elm().click()
        time.sleep(3)
    def test_product_tag(self,setuplogin):
        self.driver = setuplogin
        aa = Catelog_list(self.driver)
        aa.catelog_elm().click()
        time.sleep(3)
        aa.product_tags_elm().click()
        time.sleep(2)
    def test_attributes(self,setuplogin):
        self.driver = setuplogin
        aa = Catelog_list(self.driver)
        aa.catelog_elm().click()
        time.sleep(2)
        aa.attributes_elm().click()
        time.sleep(2)

    def test_sales_elm(self,setuplogin):
        self.driver = setuplogin
        bb = sales_list(self.driver)
        bb.sales_elm().click()
        time.sleep(2)
        bb.orders_elm().click()
        time.sleep(2)
