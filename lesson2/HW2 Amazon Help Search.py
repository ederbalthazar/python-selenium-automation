import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\Cheddah\\Desktop\\Careerist Python course\\python-selenium-automation\\chromedriver.exe")
driver.get('https://www.amazon.com/gp/help/customer/display.html')

elem = driver.find_element(By.ID, 'helpsearch')

elem.send_keys("Cancel order")
elem.send_keys(Keys.RETURN)

expected_result = 'Cancel Items or Orders'
actual_result = driver.find_element(By.XPATH, "//h1").text

assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match expected {expected_result}'

print('Test case passed')

driver.close()
