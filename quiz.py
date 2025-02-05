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

# Question 2: 
print("Question", question_number, ": What will be the output of print(10 // 3)?")
print("A) 3.33")
print("B) 3")
print("C) 4")
print("D) 10")
answer = input("Your answer: ").strip().lower()
if answer == "b":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer is B) 3.\n")
question_number += 1

# Question 3: 
print("Question", question_number, ": What keyword is used for an alternative condition in Python?")
print("A) else")
print("B) elif")
print("C) elseif")
print("D) case")
answer = input("Your answer: ").strip().lower()
if answer == "b":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer is B) elif.\n")
question_number += 1

# Question 4: 
print("Question", question_number, ": Which loop is used when the number of iterations is unknown?")
print("A) for")
print("B) while")
print("C) do-while")
print("D) repeat")
answer = input("Your answer: ").strip().lower()
if answer == "b":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect! The correct answer is B) while.\n")
question_number += 1
