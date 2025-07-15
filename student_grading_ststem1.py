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

    print(f"\n📊 Report for Student {i+1}:")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")
