questions = [
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["function", "def", "define", "fun"],
        "answer": "B"
    },
    {
        "question": "Which data type stores key-value pairs?",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "answer": "C"
    },
    {
        "question": "Which function displays output?",
        "options": ["input()", "print()", "display()", "output()"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments?",
        "options": ["//", "#", "!", "&"],
        "answer": "B"
    },
    {
        "question": "Which loop iterates over a sequence?",
        "options": ["if", "while", "for", "else"],
        "answer": "C"
    }
]


def start_quiz():
    score = 0
    correct = 0
    incorrect = 0

    print("\nWelcome to the Python Quiz!")
    print("Enter A, B, C, or D to answer.")

    start = input("Start quiz? (yes/no): ").lower()

    if start != "yes":
        print("Quiz cancelled!")
        return

    for i, q in enumerate(questions, 1):
        print("\nQuestion", i, ":", q["question"])

        for j, option in enumerate(q["options"]):
            print(chr(65 + j) + ".", option)

        while True:
            answer = input("Your answer: ").strip().upper()

            if answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid choice! Enter A, B, C, or D.")

        if answer == q["answer"]:
            print("Correct answer!")
            score += 1
            correct += 1
        else:
            print("Wrong answer!")
            print("Correct answer:", q["answer"])
            incorrect += 1

    percentage = (score / len(questions)) * 100

    print("\n===== QUIZ RESULTS =====")
    print("Total Questions:", len(questions))
    print("Correct Answers:", correct)
    print("Incorrect Answers:", incorrect)
    print("Final Score:", percentage, "%")

    if percentage >= 80:
        print("Excellent job!")
    elif percentage >= 50:
        print("Good effort! Keep practising.")
    else:
        print("Keep trying! You can improve.")


while True:
    print("\n===== QUIZ APPLICATION =====")
    print("1. Start Quiz")
    print("2. View Instructions")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        start_quiz()

    elif choice == "2":
        print("\nThere are 5 questions.")
        print("Choose A, B, C, or D.")
        print("Each correct answer gets 1 point.")

    elif choice == "3":
        print("Thank you! Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")