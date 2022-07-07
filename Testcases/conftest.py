from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path=r"C:\Users\HP\OneDrive\Desktop\vani\chromedriver_win32\chromedriver.exe")
    yield driver
    driver.close()

@pytest.fixture()
def setuplogin(setup):
    driver = setup
    driver.get('https://admin-demo.nopcommerce.com/')
    driver.find_element(By.ID, 'Email').clear()
    driver.find_element(By.ID, 'Email').send_keys('admin@yourstore.com')
    driver.find_element(By.ID, 'Password').clear()
    driver.find_element(By.ID, 'Password').send_keys('admin')
    driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button').click()
    yield driver