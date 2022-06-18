from selenium.webdriver.common.by import By

def tabulate_course_details(driver):
    '''
    driver: Webdriver element

    returns: Course and Semester details in a tabular format
    '''
    courses = driver.find_element(By.XPATH, "/html/body/center/center/table[1]/tbody").text
    course_list = courses.split('\n')

    #print(course_list)

    course_list = [i.split() for i in course_list]

    count = 0
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
            count += 1                   # Number of courses taken in a particular sem
        elif i[0] == "Earned":
            if i[1][-2:].isnumeric():
                credits.append((int(i[1][-2:]), count))
            else:
                credits.append((int(i[1][-1]), count))

        else:
            count = 0
            sem.append(' '.join(i[:]))

    course_summary = (course_code, course_name, course_category, course_credits, course_grade)
    sem_summary = (sem, credits)

    return course_summary, sem_summary
