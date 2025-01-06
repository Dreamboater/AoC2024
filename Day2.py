f = open("Day 2 Input", "r")
safe = 0
reports = []

for i in range(0,1000):
    report = f.readline().split()
    print(report)
    reports.append(report)

for report in reports:
    for i in range(0,len(report)-2):
        if (int(report[i])-int(report[i+1]))<0 and (int(report[i+1])-int(report[i+2]))<0:
            if

            continue


