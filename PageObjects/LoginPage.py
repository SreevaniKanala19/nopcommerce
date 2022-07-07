from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class Catelog_list:
    def __init__(self, driver):
        self.driver = driver

    def catelog_elm(self):
        return self.driver.find_element(By.XPATH,'/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/a')
    def product_elm(self):
        return self.driver.find_element(By.XPATH,'/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/ul/li[1]/a/p')
    def category_elm(self):
        return self.driver.find_element(By.XPATH,'/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/ul/li[2]/a/p')
    def manufacturer_elm(self):
        return self.driver.find_element(By.XPATH,'/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/ul/li[3]/a/p')
    def product_reviews_elm(self):
        return self.driver.find_element(By.XPATH,'/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/ul/li[4]/a/p')
    def product_tags_elm(self):
        return self.driver.find_element(By.XPATH,'/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/ul/li[5]/a/p')
    def attributes_elm(self):
        return self.driver.find_element(By.XPATH,'/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/ul/li[6]/a/p')
class sales_list:
    def __init__(self, driver):
        self.driver = driver
    def sales_elm(self):
        return self.driver.find_element(By.XPATH,'/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[3]/a')
    def orders_elm(self):
        return self.driver.find_element(By.XPATH,'/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[3]/ul/li[1]/a/p')
    def shipment_elm(self):
        return self.driver.find_element(By.XPATH,'/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[3]/ul/li[2]/a/p')
    def return_requests_elm(self):
        return self.driver.find_element(By.XPATH,'/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[3]/ul/li[3]/a/p')
    def recurring_elm(self):
        return self.driver.find_element(By.XPATH,'/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[3]/ul/li[4]/a/p')
    def gifts_elm(self):
        return self.driver.find_element(By.XPATH,'/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[3]/ul/li[5]/a/p')
    def shopping_Carts_elm(self):
        return self.driver.find_element(By.XPATH,'/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[3]/ul/li[6]/a/p')


