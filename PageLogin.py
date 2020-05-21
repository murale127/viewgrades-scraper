#necessary imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Specify Path to geckodriver for Firefox
driver = webdriver.Firefox(executable_path=r"/home/murale/Downloads/geckodriver-v0.26.0-linux64/geckodriver")

#Navigating to viewgrades webpage
driver.get("https://www.iitm.ac.in/viewgrades/")

# loop prompting correct login details
tried = False
while driver.current_url=="https://www.iitm.ac.in/viewgrades/index.html" or driver.current_url=="https://www.iitm.ac.in/viewgrades/": 

    if tried == True:
        #check if it is not the first iteration
        print("Incorrect Roll Number and/or Password")

    rollno = driver.find_element_by_name("rollno")
    pwd = driver.find_element_by_name("pwd")

    roll = input("Enter your roll number:")
    password = input("Enter your password:")
    rollno.send_keys(roll)
    pwd.send_keys(password)
    driver.find_element_by_name("submit").click()

    tried = True

#login done succesfully

# searching for releavent data using xpath
driver.get("https://www.iitm.ac.in/viewgrades/studentauth/btechdual.php")

name = driver.find_element_by_xpath("/html/body/")

print(name)