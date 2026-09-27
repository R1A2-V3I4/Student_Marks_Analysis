import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = [
    ["S001", "Ravi", "Male", "CSE", 85, 78, 82, 88, 92, 91],
    ["S002", "Priya", "Female", "CSE", 92, 89, 94, 90, 96, 97],
    ["S003", "Arjun", "Male", "ECE", 72, 68, 75, 79, 70, 84],
    ["S004", "Sneha", "Female", "EEE", 88, 91, 86, 85, 89, 93],
    ["S005", "Kiran", "Male", "CSE", 65, 72, 68, 74, 80, 78],
    ["S006", "Anjali", "Female", "IT", 95, 93, 91, 94, 97, 98],
    ["S007", "Rahul", "Male", "ECE", 78, 75, 80, 72, 76, 86],
    ["S008", "Divya", "Female", "CSE", 84, 88, 86, 91, 90, 92],
    ["S009", "Vijay", "Male", "EEE", 58, 62, 65, 68, 60, 71],
    ["S010", "Meena", "Female", "IT", 89, 94, 92, 87, 93, 95],
    ["S011", "Ajay", "Male", "CSE", 76, 81, 73, 79, 85, 88],
    ["S012", "Keerthi", "Female", "ECE", 91, 87, 89, 93, 88, 96],
    ["S013", "Varun", "Male", "IT", 69, 74, 71, 70, 78, 80],
    ["S014", "Pooja", "Female", "EEE", 82, 79, 84, 86, 81, 89],
    ["S015", "Manoj", "Male", "CSE", 55, 61, 58, 65, 67, 69],
    ["S016", "Lakshmi", "Female", "IT", 94, 90, 96, 92, 95, 97],
    ["S017", "Harsha", "Male", "ECE", 73, 77, 69, 75, 72, 83],
    ["S018", "Nandini", "Female", "CSE", 87, 85, 90, 89, 94, 94],
    ["S019", "Suresh", "Male", "EEE", 63, 67, 61, 70, 65, 75],
    ["S020", "Swathi", "Female", "IT", 91, 96, 94, 90, 98, 99]
]

df = pd.DataFrame(
    data,
    columns=[
        "ID", "Name", "Gender", "Department",
        "Maths", "Physics", "Chemistry",
        "English", "Computer_Science", "Attendance"
    ]
)
subjects = ['Maths', 'Physics', 'Chemistry', 'English', 'Computer_Science']

df['Total'] = df[subjects].sum(axis=1)

print(df[['Name', 'Total']])
df['Average'] = df[subjects].mean(axis=1)

print(df[['Name', 'Average']])
df['Percentage'] = df['Total'] / 5

print(df[['Name', 'Percentage']])
def grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    else:
        return 'F'

df['Grade'] = df['Percentage'].apply(grade)

print(df[['Name', 'Percentage', 'Grade']])
# Top Students
top_students = df.sort_values('Total', ascending=False).head(5)
print(top_students[['Name', 'Total', 'Percentage']])
low_students = df.sort_values('Total').head(5)
# Low Students
print(low_students[['Name', 'Total', 'Percentage']])
subject_average = df[subjects].mean()    # Subect Average
print(subject_average)
best_subject = subject_average.idxmax()  # Best Subject
print("Best Subject:", best_subject)
weakest_subject = subject_average.idxmin()  # Weakest Subject
print("Weakest Subject:", weakest_subject)
department_average = df.groupby('Department')['Percentage'].mean() # Department Average
print(department_average)
# Gender Average
gender_average = df.groupby('Gender')['Percentage'].mean()
print(gender_average)
# Low Attendence
low_attendance = df[df['Attendance'] < 75]
print(low_attendance[['Name', 'Attendance', 'Percentage']])
# Correlation
print(df[['Attendance', 'Percentage']].corr())
df['Result'] = df['Percentage'].apply(
    lambda x: 'Pass' if x >= 40 else 'Fail'
)
# Analysis of Data
print(df[['Name', 'Percentage', 'Result']])
print(df['Grade'].value_counts())
subject_average.plot(kind='bar')

plt.title('Average Marks by Subject')
plt.xlabel('Subject')
plt.ylabel('Average Marks')
plt.xticks(rotation=45)
plt.show()
# Top 10 students
top10 = df.sort_values('Total', ascending=False).head(10)

plt.bar(top10['Name'], top10['Total'])

plt.title('Top 10 Students')
plt.xlabel('Student')
plt.ylabel('Total Marks')
plt.xticks(rotation=45)

plt.show()
# Grade Distribution
df['Grade'].value_counts().plot(kind='bar')

plt.title('Grade Distribution')
plt.xlabel('Grade')
plt.ylabel('Number of Students')

plt.show()
# Attendence vs Marks
sns.scatterplot(
    data=df,
    x='Attendance',
    y='Percentage'
)

plt.title('Attendance vs Percentage')
plt.show()
#Heat Map
correlation = df[subjects + ['Attendance', 'Percentage']].corr()

sns.heatmap(correlation, annot=True)

plt.title('Student Performance Correlation')
plt.show()