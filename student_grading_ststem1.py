# Function to calculate grade based on average

def get_grade(avg):
    if avg >= 85:
        return "A"
    
    elif avg >= 70:
        return "B"
    
    elif avg >= 55:
        return "C"
    
    elif avg >= 40:
        return "D"
    
    else:
        return "F"

# Ask how many students

num_students = int(input("Enter total number of students: "))

# Loop for each student

for i in range(num_students):
    print(f"\n📄 Enter marks for Student {i+1}:")

    math = float(input("Math marks: "))
    science = float(input("Science marks: "))
    english = float(input("English marks: "))
    computer = float(input("Computer marks: "))

    total = math + science + english + computer
    
    average = total / 4
    grade = get_grade(average)

  
    
    
    
    #output
    Enter total number of students: 2

📄 Enter marks for Student 1:
Math marks: 87
Science marks: 88
English marks: 68
Computer marks: 98

📊 Report for Student 1:
Total Marks: 341.0
Average Marks: 85.25
Grade: A

📄 Enter marks for Student 2:
Math marks: 77
Science marks: 87
English marks: 67
Computer marks: 95

📊 Report for Student 2:
Total Marks: 326.0
Average Marks: 81.50
Grade: B


    print(f"\n📊 Report for Student {i+1}:")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")
