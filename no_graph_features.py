grade2point = {"S":10, "A":9, "B":8, "C":7, "D":6, "E":4, "U":0, "I":0, "W":0}

def Dept_GPA(courses):
    '''
    course: summary of the courses obtained from the webpage

    returns: GPA of the required department
    '''
    while True:
        dept = input("Enter the department code: ")
        total_credits = 0 
        total_points = 0
        for i in range(len(courses[0])):
            if courses[0][i][:2] == dept:
                try:
                    total_points += int(courses[3][i]) * grade2point[(courses[4][i])]
                    total_credits += float(courses[3][i])
                except:
                    pass
        gpa = round(total_points/total_credits, 2)

        return dept, gpa

def courseCheck(name,courses):
    flag=False
    for i in range(len(courses[0])):
            if courses[0][i] == name:
                print("Course name is "+courses[1][i])
                print("Your grade in "+name+" is: "+courses[4][i])
                print("Your credits in "+name+" is: "+courses[3][i])
                flag=True
    if flag == False:
        print("No such course found")