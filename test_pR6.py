
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestPR6():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_pR6(self):
    self.driver.get("https://idemo.bspb.ru/")
    self.driver.find_element(By.NAME, "username").click()
    self.driver.find_element(By.NAME, "username").send_keys("demo")
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("demo")
    self.driver.find_element(By.ID, "login-button").click()
    self.driver.find_element(By.ID, "otp-code").click()
    self.driver.find_element(By.ID, "otp-code").send_keys("0000")
    self.driver.find_element(By.ID, "login-otp-button").click()
    self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/div/ul[1]/li[5]/a/span").click()
    self.driver.find_element(By.ID, "btn-show-rates").click()
    self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div[4]/label[3]").click()
    self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/form/table/tbody/tr[1]/td[7]/a").click()
    self.driver.find_element(By.ID, "amount").click()
    self.driver.find_element(By.ID, "amount").send_keys("100000")
    self.driver.find_element(By.ID, "submit-button").click()
    self.driver.find_element(By.NAME, "condition.newDepositConditions").click()
    self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div/div/label/p/span/a").click()
    self.driver.find_element(By.ID, "accept-instant-deposit-agreement-button").click()
    self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/form/div[4]/button").click()
  
