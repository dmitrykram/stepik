from inspect import classify_class_attrs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math, time
import os
import pyperclip

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

bookin = browser.find_element(By.ID, "book")
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

bookin.click()

form = browser.find_element(By.CLASS_NAME, "form-control")
browser.execute_script("return arguments[0].scrollIntoView(true);", form)

x = browser.find_element(By.ID, 'input_value').text
y = calc(x)

form.send_keys(y)

browser.find_element(By.ID, "solve").click()

time.sleep(3)

pyperclip.copy(browser.switch_to.alert.text.split(': ')[-1])

browser.quit()


