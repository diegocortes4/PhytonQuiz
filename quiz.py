print("Welcome to the Python Basics Quiz!")
print("You will answer 5 questions. Type A, B, C, or D to answer each question.")

# Initialize score and question number
score = 0
question_number = 1

while question_number <= 5:
    print("Question", question_number, ":", end=" ")

    if question_number == 1:
        print("Which data type is used to store text in Python?")
        print("A) int\nB) float\nC) str\nD) bool")
        correct_answer = "c"

    elif question_number == 2:
        print("What will be the output of print(10 // 3)?")
        print("A) 3.33\nB) 3\nC) 4\nD) 10")
        correct_answer = "b"

    elif question_number == 3:
        print("What keyword is used for an alternative condition in Python?")
        print("A) else\nB) elif\nC) elseif\nD) case")
        correct_answer = "b"

    elif question_number == 4:
        print("Which loop is used when the number of iterations is unknown?")
        print("A) for\nB) while\nC) do-while\nD) repeat")
        correct_answer = "b"

    elif question_number == 5:
        print("What will be the output of 'hello'.upper()?")
        print("A) hello\nB) Hello\nC) HELLO\nD) HeLLo")
        correct_answer = "c"

    answer = input("Your answer: ").strip().lower()

    if answer == correct_answer:
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect! The correct answer is", correct_answer.upper(), "\n")

    question_number += 1

# Final Score
print("Congratulations! You completed the quiz.")
print("Your final score is:", score, "out of 5")