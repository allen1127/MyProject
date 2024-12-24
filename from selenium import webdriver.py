# from selenium import webdriver
# wd = webdriver.Chrome()
# wd.get('https://scr.cyc.org.tw/tp10.aspx?module=login_page&files=login&PT=1')
# import os
# os.system("pause")
# //*[@id="ContentPlaceHolder1_Step2_data"]/table/tbody/tr[4]/td[3]/img
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from datetime import datetime, timedelta
from threading import Timer
import os
# from selenium.webdriver.remote.webelement import WebElement
# import selenium.webdriver.remote.webelement;
import time
from seleniumbase import Driver
driver = Driver(uc=True, headless=False)
url = "https://scr.cyc.org.tw/tp10.aspx?module=login_page&files=login&PT=1"

driver.get(url)
# driver.uc_open_with_reconnect(url, reconnect_time=6)

# element = driver.find_element(By.LINK_TEXT, "這只是提醒！！！\n請勿開啟2個網頁(含以上)頁面進行登入、預約場地或報名課程作業")
# element.click()

# wait = WebDriverWait(driver, timeout=2)
# alert = wait.until(lambda d : d.switch_to.alert)
# text = alert.text
# alert.accept()

# element = driver.find_element(By.LINK_TEXT, "這只是提醒！！！\n請勿開啟2個網頁(含以上)頁面進行登入、預約場地或報名課程作業")
# driver.execute_script("arguments[0].click();", element)

# wait = WebDriverWait(driver, timeout=2)
# alert = wait.until(lambda d : d.switch_to.alert)
# text = alert.text
# alert.dismiss()

# element = driver.find_element(By.LINK_TEXT, "這只是提醒！！！請勿開啟2個網頁(含以上)頁面進行登入、預約場地或報名課程作業")
# element.click()

# wait = WebDriverWait(driver, timeout=2)
# alert = wait.until(lambda d : d.switch_to.alert)
# text = alert.text
# alert.accept()


time.sleep(7)

driver.find_element(By.ID, "ContentPlaceHolder1_loginid").send_keys("E124442792")

driver.find_element(By.ID, "loginpw").send_keys("E124442792")

driver.find_element(By.ID, "login_but").click()

time.sleep(3)


currentDateAndTime = datetime.now() 
currentDateDay = datetime.now() + timedelta(days=13)

timeHH = currentDateAndTime.strftime('%H')

timeDD = currentDateAndTime.strftime('%d')

# if "00"==timeHH:
driver.get("https://scr.cyc.org.tw/tp10.aspx?module=net_booking&files=booking_place&StepFlag=2&PT=1&D="+currentDateDay.strftime('%Y/%m/%d')+"&D2=1")

# print(currentDateDay.strftime('%Y/%m/%d'))

# os.system("pause")

l =driver.find_element(by=By.XPATH, value="//*[@id=\"ContentPlaceHolder1_Step2_data\"]/table/tbody/tr[4]/td[3]/img")
test =l.get_attribute('onclick')

# t =driver.find_element_by_xpath("//*[@id=\"ContentPlaceHolder1_Step2_data\"]/table/tbody/tr[4]/td[3]/img").click()

print(test)
os.system("pause")
l.click()

try:
    WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                'Timed out waiting for PA creation ' +
                                'confirmation popup to appear.')

    alert = driver.switch_to.alert
    alert.accept()
    print("alert accepted")
except TimeoutException:
    print("no alert")

os.system("pause")
# driver.switchTo().alert().accept();

# driver.find_element_by_id('But_MemberApply').click()


# driver.find_element(By.ID, "But_MemberApply").click()


#But_MemberApply