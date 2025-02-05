print("Welcome to the Python Basics Quiz!")
print("You will answer 5 questions. Type A, B, C, or D to answer each question.")

# Initialize score and question number
score = 0
question_number = 1

# Question 1
print("Question", question_number, ": Which data type is used to store text in Python?")
print("A) int")
print("B) float")
print("C) str")
print("D) bool")
answer = input("Your answer: ").strip().lower()
if answer == "c":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer is C) str.\n")
question_number += 1

print("Congratulations! You completed the quiz.")