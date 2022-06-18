# Necessary imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import no_graph_features as ngf
from course_details import tabulate_course_details
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options, service=Service(executable_path=GeckoDriverManager().install()))

# Navigating to the webpage
driver.get("https://www.iitm.ac.in/viewgrades/")



# Loop prompting correct login details
tried = False
while driver.current_url=="https://www.iitm.ac.in/viewgrades/index.html" or driver.current_url=="https://www.iitm.ac.in/viewgrades/":

    if tried == True:
        # Check if it is not the first iteration
        print("Incorrect Roll Number and/or Password")

    # Locate form fields
    rollno = driver.find_element(By.NAME, "rollno")
    pwd = driver.find_element(By.NAME, "pwd")

    roll = input("Enter your roll number:")
    password = getpass("Enter your password:")

    rollno.send_keys(roll)
    pwd.send_keys(password)
    driver.find_element(By.NAME, "submit").click()

    tried = True


# searching for releavent data using xpath
driver.get("https://www.iitm.ac.in/viewgrades/studentauth/btechdual.php")


# Intro greeting
name = driver.find_element(By.XPATH, "/html/body/center/table/tbody/tr/th[3]")
print("Hi,", name.text)

cg = driver.find_element(By.XPATH, "/html/body/center/center/table[1]/tbody/tr[last()]/td[last()]")
print("Your", cg.text)

courses, sem = tabulate_course_details(driver)
driver.close()


choice = ' '
while choice.lower() != 'x':
    choice = input('''\nHow do you want you visualize your grades:
    a) GPA for courses taken in a specific department

    Other features will come soon.

Enter x to exit
    ''')
    if choice.lower() == 'a':
        dept, gpa = ngf.Dept_GPA(courses)
        print("Your GPA of the courses done in", dept, "department is", gpa, "\n")
        dummy = input('''Press Enter to continue''')
