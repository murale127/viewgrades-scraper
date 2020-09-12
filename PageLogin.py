# Necessary imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import no_graph_features as ngf
from course_details import tabulate_course_details
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

# Specify Path to geckodriver for Firefox
driver = webdriver.Firefox(options=options, executable_path=r"./geckodriver-v0.26.0-linux64/geckodriver")

# Navigating to the webpage
driver.get("https://www.iitm.ac.in/viewgrades/")



# Loop prompting correct login details
tried = False
while driver.current_url=="https://www.iitm.ac.in/viewgrades/index.html" or driver.current_url=="https://www.iitm.ac.in/viewgrades/": 

    if tried == True:
        # Check if it is not the first iteration
        print("Incorrect Roll Number and/or Password")

    # Locate form fields
    rollno = driver.find_element_by_name("rollno")
    pwd = driver.find_element_by_name("pwd")

    roll = input("Enter your roll number:")
    password = getpass("Enter your password:")

    rollno.send_keys(roll)
    pwd.send_keys(password)
    driver.find_element_by_name("submit").click()

    tried = True


# searching for releavent data using xpath
driver.get("https://www.iitm.ac.in/viewgrades/studentauth/btechdual.php")


# Intro greeting
name = driver.find_element_by_xpath("/html/body/center/table/tbody/tr/th[3]")
print("Hi,", name.text)

cg = driver.find_element_by_xpath("/html/body/center/center/table[1]/tbody/tr[last()]/td[last()]")
print("Your", cg.text)

courses, sem = tabulate_course_details(driver)
driver.close()


choice = ' '
while choice.lower() != 'x':
    choice = input('''
How do you want you visualize your grades:
    a) GPA for courses taken in a specific department
<<<<<<< HEAD

    Other features will come soon.   
=======
  
>>>>>>> a23a184647e6ce241a2a6f4de2e4abc4e1ac1e2c
Enter x to exit
    ''')
    if choice.lower() == 'a':
        dept, gpa = ngf.Dept_GPA(courses)
        print("Your GPA of the courses done in", dept, "department is", gpa)
<<<<<<< HEAD
    _ = input("\nPress enter to continue")
=======
>>>>>>> a23a184647e6ce241a2a6f4de2e4abc4e1ac1e2c
