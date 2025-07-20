
import pandas as pd
import matplotlib.pyplot as plt

def calculate_result(marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = 'A'
    elif average >= 70:
        grade = 'B'
    else:
        grade = 'C'
    
    return total, average, grade

print("🎓 Welcome to the Mini Student Report Card Generator!\n")

# no. of students
num_students = int(input(" How many students are in your class?  "))

#  collecting data 
student_data = []

for i in range(num_students):
    print(f"\n Entering details for Student {i+1}:")

    name = input(" Student Name: ")
    marks = []

    # Input marks for 3 subjects
    for j in range(1, 4):
        mark = float(input(f"   📘 Enter marks for Subject {j}: "))
        marks.append(mark)

    total, average, grade = calculate_result(marks)

    student_data.append({
        'Name': name,
        'Subject1': marks[0],
        'Subject2': marks[1],
        'Subject3': marks[2],
        'Total': total,
        'Average': round(average, 2),
        'Grade': grade
    })


df = pd.DataFrame(student_data)
#summary of the class
print("\n Final Report Summary:")
print(" Total Students: {num_students}")
print(" Class Average Score: {df['Average'].mean():.2f}")
print("\n Grade Distribution:")
print(df['Grade'].value_counts())

df.to_csv("student_report_card.csv", index=False)
print("\n The report has been saved as 'student_report_card.csv'!")

#  grade distribution using a bar chart
print("\n Generating Grade Distribution Chart...")

df['Grade'].value_counts().plot(
    kind='bar',
    color='lightgreen',
    edgecolor='black'
)

plt.title(' Grade Distribution of the Class')
plt.xlabel('Grade')
plt.ylabel('Number of Students')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


#output
 How many students are in your class?  3

 Entering details for Student 1:
 Student Name: priyanshu
   📘 Enter marks for Subject 1: 88
   📘 Enter marks for Subject 2: 98
   📘 Enter marks for Subject 3: 92

 Entering details for Student 2:
 Student Name: rahul
   📘 Enter marks for Subject 1: 89
   📘 Enter marks for Subject 2: 78
   📘 Enter marks for Subject 3: 95

 Entering details for Student 3:
 Student Name: prince
   📘 Enter marks for Subject 1: 90
   📘 Enter marks for Subject 2: 67
   📘 Enter marks for Subject 3: 78

 Final Report Summary:
 Total Students: {num_students}
 Class Average Score: {df['Average'].mean():.2f}

 Grade Distribution:
Grade
B    2
A    1
Name: count, dtype: int64

 The report has been saved as 'student_report_card.csv'!

 Generating Grade Distribution Chart...


