def average_grade(roster=[]):
    total = 0
    for i in range(len(roster)):
        total = total + roster[i].student_grade

    average = total/len(roster)
    return average
