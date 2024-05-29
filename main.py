from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# THIS IS TO KEEP CHROME OPEN AFTER PROGRAM FINISHES
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3918249887&f_AL=true&keywords=software%"
           "20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

# /html/body/div[1]/header/nav/div/a[2] (X-PATH)

signin_button = driver.find_element(By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
signin_button.click()
time.sleep(1)

email_phone = driver.find_element(By.ID, value="username")
password = driver.find_element(By.ID, value="password")

email_phone.send_keys("your email or number")
password.send_keys("your password")
time.sleep(2)

signin_button = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
signin_button.click()



# driver.quit()


