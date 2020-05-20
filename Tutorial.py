from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=r"/home/murale/Downloads/geckodriver-v0.26.0-linux64/geckodriver")


driver.get("https://www.iitm.ac.in/viewgrades/")


rollno = driver.find_element_by_name("rollno")
pwd = driver.find_element_by_name("pwd")

roll = input("Enter your roll number:")
password = input("Enter your password:")

rollno.send_keys(roll)
pwd.send_keys(password)

driver.find_element_by_name("submit").click()
