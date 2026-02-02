from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Setup the browser (Chrome)
driver = webdriver.Chrome()

# 2. Open the OrangeHRM Website
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(10)

# 3. Find Username and Password fields
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")

# 4. Click Login Button
driver.find_element(By.TAG_NAME, "button").click()

# 5. Verify Login
time.sleep(5)
if "dashboard" in driver.current_url.lower():
    print("Test Passed: Login Successful!")
else:
    print("Test Failed: Login Unsuccessful.")

# 6. Close Browser
driver.quit()