from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=r"/home/murale/Downloads/geckodriver-v0.26.0-linux64/geckodriver")


driver.get("https://www.iitm.ac.in/viewgrades/")


rollno = driver.find_element_by_name("rollno")
pwd = driver.find_element_by_name("pwd")

rollno.send_keys("EP18B026")
pwd.send_keys("QRNT@w9J")

driver.find_element_by_name("submit").click()