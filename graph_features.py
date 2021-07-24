import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i],ha = 'center')

def Credits_stream(courses):    
    # plt.savefig("mygraph.png")
    count_eng = 0
    count_pro = 0
    count_sci = 0
    count_hum = 0
    credit_eng = 0
    credit_pro = 0
    credit_sci = 0
    credit_hum = 0
    for i in range(len(courses[0])):
        # print (courses[2][i])
        if courses[2][i] == 'Engineering':
            count_eng=count_eng+1
            credit_eng=credit_eng+int(courses[3][i])
        elif courses[2][i] == 'Professional':
            count_pro=count_pro+1
            credit_pro=credit_pro+int(courses[3][i])
        elif courses[2][i] == 'Science':
            count_sci=count_sci+1
            credit_sci=credit_sci+int(courses[3][i])
        elif courses[2][i] == 'Humanities':
            count_hum=count_hum+1
            credit_hum=credit_hum+int(courses[3][i])
    data=[credit_eng,credit_pro,credit_sci,credit_hum]
    labels = ['Engineering', 'Professional', 'Science', 'Humanities']
    addlabels(labels, data)
    plt.xticks(range(len(data)), labels)
    plt.xlabel('Category')
    plt.ylabel('Credits')
    plt.title('title')
    plt.bar(range(len(data)), data) 
    plt.show()
        
def gpa_graph(gpas):
    labels=[]
    for i in range(len(gpas)):
        # print(gpas[i])
        labels.append("Sem "+str(i))
    data = gpas
    addlabels(labels, data)
    plt.xticks(range(len(data)), labels)
    plt.xlabel('Semester')
    plt.ylabel('GPAs')
    plt.title('title')
    plt.bar(range(len(data)), data) 
    plt.show()

