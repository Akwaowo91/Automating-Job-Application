from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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

email_phone.send_keys("your email")
password.send_keys("your password")
time.sleep(2)

signin_button = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
signin_button.click()

apply_for_job = driver.find_element(By.XPATH, value='//*[@id="ember50"]')
apply_for_job.click()

enter_phone_num = driver.find_element(By.XPATH, value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs'
                                                      '-applyformcommon-easyApplyFormElement-3918249887-122846549-'
                                                      'phoneNumber-nationalNumber"]'
                                      )
enter_phone_num.click()
enter_phone_num.send_keys("your number")

next_step = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Continue to next step']")
next_step.click()

new_step = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Continue to next step']")
new_step.click()

new_step = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Continue to next step']")
new_step.click()

Additional_question = driver.find_element(By.XPATH, value='//*[@id="single-line-text-form-component-formElement-urn'
                                                          '-li-jobs-applyformcommon-easyApplyFormElement-'
                                                          '3918249887-122846533-numeric"]'
                                          )
Additional_question.send_keys("2")

# Locate the dropdown element by its ID
dropdown = driver.find_element(By.ID, "text-entity-list-form-component-formElement-urn-li-jobs-applyformcommon"
                                      "-easyApplyFormElement-3918249887-336975493-multipleChoice")

# Create a Select object
select = Select(dropdown)

# Select the option by visible text
select.select_by_visible_text("Yes")
time.sleep(1)

submit = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Continue to next step']")
submit.click()

time.sleep(1)

review = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Review your application']")
review.click()

time.sleep(1)
submit_application = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Submit application']")
submit_application.click()

# next_step = driver.find_element(By.TAG_NAME, value="button")
# next_step.click()

# choose_resume = driver.find_element(By.XPATH, value='//*[@id="jobsDocumentCardToggleLabel-ember359"]')
# choose_resume.click()

# driver.quit()


# //*[@id="ember426"]
# //*[@id="ember464"]/span
