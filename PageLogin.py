#necessary imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass

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

    #roll = input("Enter your roll number:")
    #password = getpass("Enter your password:")
    rollno.send_keys("EP18B026")
    pwd.send_keys("QRNT@w9J")
    driver.find_element_by_name("submit").click()

    tried = True

#login done succesfully

# searching for releavent data using xpath
driver.get("https://www.iitm.ac.in/viewgrades/studentauth/btechdual.php")

name = driver.find_element_by_xpath("/html/body/center/table/tbody/tr/th[3]")
print("Hi,", name.text)

main_table_path = "/html/body/center/center/table[1]/tbody"

cg = driver.find_element_by_xpath(main_table_path + "/tr[last()]/td[last()]")
print("Your", cg.text)

courses = driver.find_element_by_xpath(main_table_path).text
course_list = courses.split('\n')

#print(course_list)

course_list = [i.split() for i in course_list]

course_code = []
course_name = []
course_category = []
course_credits = []
course_grade = []
credits = []
sem = []

for i in course_list:
    if i[0].isnumeric():
        course_code.append(i[1])
        course_name.append(' '.join(i[2:-4]))
        course_category.append(i[-4])
        course_credits.append(i[-3])
        course_grade.append(i[-2])
        count += 1
    elif i[0] == "Earned":
        if i[1][-2:].isnumeric():
            credits.append((int(i[1][-2:]), count))
        else:
            credits.append((int(i[1][-1]), count))
        
    else:
        count = 0
        sem.append(' '.join(i[:2]))


driver.close()