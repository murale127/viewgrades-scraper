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