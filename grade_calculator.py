# Student Grade Calculator Project

def calculate_grade(marks):
    """Function to calculate grade and message based on marks"""
    
    if 90 <= marks <= 100:
        return "A", "Outstanding! You are amazing! 🌟"
    elif 80 <= marks <= 89:
        return "B", "Very Good! Keep it up! 👍"
    elif 70 <= marks <= 79:
        return "C", "Good job! You can do even better! 💪"
    elif 60 <= marks <= 69:
        return "D", "Keep working hard! Improvement is possible! 📘"
    else:
        return "F", "Don’t give up! Practice makes perfect! ✨"


# Input Section with Validation
while True:
    name = input("Enter student name: ")
    
    try:
        marks = int(input("Enter marks (0-100): "))
        
        if 0 <= marks <= 100:
            break
        else:
            print("❌ Marks must be between 0 and 100. Try again.")
            
    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")


# Calculate grade
grade, message = calculate_grade(marks)

# Output
print("\n📊 RESULT FOR", name.upper() + ":")
print("Marks:", marks, "/100")
print("Grade:", grade)
print("Message:", message)
