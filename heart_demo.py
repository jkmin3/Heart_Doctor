import csv
from heart_class import *
import matplotlib.pyplot as plt

with open('heart.csv', 'r') as filein:
    csvin = csv.reader(filein)
    headers = next(csvin)
    heart = [row for row in csvin]

# with open('heart2.csv', 'r') as filein:
#     csvin = csv.reader(filein)
#     headers2 = next(csvin)
#     data = [r for r in csvin]

for i, line in enumerate(heart):
    Heart("Patient " + str(i), line[0], line[1], line[11], line[2], line[3], line[4], line[5], line[6], line[7],
          line[8], line[9], line[10])

# for i, line in enumerate(data):
#     Heart("Patient " + str(i + len(heart)), line[0], line[1], line[13])

# all patients in a variable
patients = Heart.patients()
heart_disease = Heart.heart_disease_patients()
no_heart_disease = Heart.no_heart_disease_patients()
male = Heart.males()
female = Heart.females()

print(Heart.average_num([patient.resting_bp for patient in heart_disease]))
print(Heart.average_num([patient.resting_bp for patient in no_heart_disease]))

print(Heart.counter([patient.sex for patient in heart_disease]))
print(Heart.counter([patient.sex for patient in no_heart_disease]))

Heart.bar_graph('heart.csv', 'Sex', 'HeartDisease', 'Sex v. Heart Disease', 'MaxHR_for_Sex')

Heart.scatter('heart.csv', 'Age', 'RestingBP', 'Age v. RestingBP', 'Scatter')

fig, axes = plt.subplots(nrows=1, ncols=2)
Heart.make_histogram('heart.csv', axes[0], 'MaxHR')
Heart.make_histogram('heart.csv', axes[1], 'RestingBP')
plt.savefig('Two_Charts')


fig1, axes1 = plt.subplots(nrows=1, ncols=1)
Heart.bar_graph('heart.csv', 'ChestPainType', 'HeartDisease', 'CPT v. Heart Disease', 'CPT')
