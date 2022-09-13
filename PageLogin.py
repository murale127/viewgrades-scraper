# Necessary imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import no_graph_features as ngf
import graph_features as gf
from course_details import tabulate_course_details
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

# Specify Path to geckodriver for Firefox
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigating to the webpage
driver.get("https://www.iitm.ac.in/viewgrades/")


# Loop prompting correct login details
tried = False
while (
    driver.current_url == "https://www.iitm.ac.in/viewgrades/index.html"
    or driver.current_url == "https://www.iitm.ac.in/viewgrades/"
):

    if tried == True:
        # Check if it is not the first iteration
        print("Incorrect Roll Number and/or Password")

    # Locate form fields
    rollno = driver.find_element("name", "rollno")
    pwd = driver.find_element("name", "pwd")

    roll = input("Enter your roll number:")
    password = getpass("Enter your password:")

    rollno.send_keys(roll)
    pwd.send_keys(password)
    driver.find_element("name", "submit").click()

    tried = True


# searching for releavent data using xpath
driver.get("https://www.iitm.ac.in/viewgrades/studentauth/btechdual.php")


# Intro greeting
name = driver.find_element("xpath", "/html/body/center/table/tbody/tr/th[3]")
print("Hi,", name.text)

cg = driver.find_element(
    "xpath", "/html/body/center/center/table[1]/tbody/tr[last()]/td[last()]"
)
print("Your", cg.text)

courses, sem, gpas = tabulate_course_details(driver)
driver.close()


choice = " "
while choice.lower() != "x":
    choice = input(
        """\nHow do you want you visualize your grades:
    a) GPA for courses taken in a specific department
    b) Credits per stream in bar chart
    c) GPA per semester in bar chart
    d) Grade and credits in specific course

Enter x to exit
    """
    )
    if choice.lower() == "a":
        dept, gpa = ngf.Dept_GPA(courses)
        print("Your GPA of the courses done in", dept, "department is", gpa, "\n")
        dummy = input("""Press Enter to continue""")
    elif choice.lower() == "b":
        gf.Credits_stream(courses)
    elif choice.lower() == "c":
        gf.gpa_graph(gpas)
    elif choice.lower() == "d":
        course_check = input("Type course number to check: ")
        ngf.courseCheck(course_check, courses)
