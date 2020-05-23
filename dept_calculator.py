grade2point = {"S":10, "A":9, "B":8, "C":7, "D":6, "E":4, "U":0, "I":0, "W":0}

print("HS courses")
total_credits = 0
total_points = 0
for i in range(len(course_code)):
    if course_code[i][:2]=="HS":
        try:
            total_points += int(course_credits[i]) * grade2point[(course_grade[i])]
            total_credits += float(course_credits[i])
        except:
            pass
gpa = round(total_points/total_credits, 2)
print("GPA for HS courses is:", gpa)
