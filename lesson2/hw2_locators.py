import nav as nav
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='https://github.com/ederbalthazar/python-selenium-automation.git')
driver.get('https://www.amazon.com/')

# Amazon logo

# By ID
driver.find_element(By.ID, 'a-icon a-icon-logo')

# By XPath
driver.find_element(By.XPATH, "//a[@href='/ref=ap frn logo']")
driver.find_element(By.XPATH, "//a[@class='a-section a-spacing-medium a-text-center']")
driver.find_element(By.XPATH, "//a[@class='a-link-nav-icon']")
driver.find_element(By.XPATH, "//a[@aria-label='Amazon']")

# By XPath, 2 attribute
# driver.find_element(By.XPATH, "//a[@class="a-link-nav-icon ' and @class="a-section a-spacing-none auth-navbar']")

# Email Field
# By ID

driver.find_element(By.ID, 'ap_email')

# By XPath
driver.find_element(By.XPATH, "//a[@class='a-input-text']")
driver.find_element(By.XPATH, "//a[@class='a-row a-spacing-base']")
driver.find_element(By.XPATH, "//a[@class='a-form-label]")

#Need help link
#By ID

driver.find_element(By.ID, 'a-expander-prompt')

# By XPath
driver.find_element(By.XPATH, "//a[@class='a-icon a-icon-expand']")
driver.find_element(By.XPATH, "//a[@class='a-expander-prompt']")
driver.find_element(By.XPATH, "//a[data-csa-c-func-deps='aui-da-a-expander-toggle']")

#Forgot your password link
#By ID

driver.find_element(By.ID, 'auth-fpp-link-bottom')

# By XPath
driver.find_element(By.XPATH, "//a[@class='a-link-normal']")
driver.find_element(By.XPATH, "//a[href='https://www.amazon.com/ap/forgotpassword?showRememberMe=true&openid']")
driver.find_element(By.XPATH, "//a['aria-expanded=true]'")

#Other issues with Sign-In link
#By ID

driver.find_element(By.ID, 'ap-other-signin-issues-link')

# By XPath
driver.find_element(By.XPATH, "//a[@class='a-link-normal']")
driver.find_element(By.XPATH, "//a[href='/gp/help/customer/account-issues/ref=ap_login_with_otp_claim_collection']")

#Create your Amazon account button
#By ID

driver.find_element(By.ID, 'createAccountSubmit')

# By XPath
driver.find_element(By.XPATH, "//a[href='https://www.amazon.com/ap/register?showRememberMe']")
driver.find_element(By.XPATH, "//a[@class='a-button-text']")

#Conditions of use link
#By ID

driver.find_element(By.ID, '508088')

#By XPath

driver.find_element(By.XPATH, "//a[@class='a-link-normal']")
driver.find_element(By.XPATH, "//a[href='/gp/help/customer/display.html/']")

#Privacy Notice link
#By ID

driver.find_element(By.ID, '468496')

#By XPath

driver.find_element(By.XPATH, "//a[@class='a-link-normal']")








