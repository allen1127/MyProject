from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from datetime import datetime, timedelta
from threading import Timer
import os
import time
from seleniumbase import Driver
sites = ["John", "Mary", "Peter"];
bookingHour1 = 9;
bookingHour2 = 15;
slot = "1";


driver = Driver(uc=True, headless=False)
url = "https://scr.cyc.org.tw/tp10.aspx?module=login_page&files=login&PT=1"
driver.get(url)
time.sleep(7)


driver.find_element(By.ID, "ContentPlaceHolder1_loginid").send_keys("E124442792")
driver.find_element(By.ID, "loginpw").send_keys("E124442792")
driver.find_element(By.ID, "login_but").click()
time.sleep(2)

def timer():
    print("1")
    datetimeNow = datetime.now() 
    if "00"==datetimeNow.strftime('%H'):   
        booking(slot,bookingHour1)
        booking(slot,bookingHour2)
    else:
        t = Timer(0.5, timer)
        t.start()
t = Timer(0.5, timer)
t.start()


def booking(rSlot,bookingHour):
    bookingday = datetime.now() + timedelta(days=13)
    driver.get("https://scr.cyc.org.tw/tp10.aspx?module=net_booking&files=booking_place&StepFlag=2&PT=1&D="+bookingday.strftime('%Y/%m/%d')+"&D2="+rSlot)
    timeout = 30
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"ContentPlaceHolder1_Date_Step2_lab\"]/select")))
    
    for i in range(bookingHour, bookingHour+1):
        l =driver.find_element(by=By.XPATH, value="//*[@id=\"ContentPlaceHolder1_Step2_data\"]/table/tbody/tr["+str(i)+"]/td[3]/img")
        if l.get_attribute('src') == "https://scr.cyc.org.tw/img/place01.png":
            # print(i)
            # driver.execute_script("window.open('https://www.google.com.tw/?hl=zh_TW')")
            

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
                

            WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"ContentPlaceHolder1_Step3Info_lab\"]/span[1]")))
            result =driver.find_element(by=By.XPATH, value="//*[@id=\"ContentPlaceHolder1_Step3Info_lab\"]/span[1]")
            print(result.text)
            
            if result.text == "預約成功":
                print("預約成功")
                break



print("hour")
os.system("pause")