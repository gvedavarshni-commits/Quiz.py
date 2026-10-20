
# Python Quiz Application

questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {
            "A": "function",
            "B": "def",
            "C": "define",
            "D": "fun"
        },
        "answer": "B"
    },
    {
        "question": "Which data type stores multiple key-value pairs in Python?",
        "options": {
            "A": "List",
            "B": "Tuple",
            "C": "Dictionary",
            "D": "Set"
        },
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": {
            "A": "//",
            "B": "/*",
            "C": "#",
            "D": "--"
        },
        "answer": "C"
    },
    {
        "question": "Which function displays output in Python?",
        "options": {
            "A": "input()",
            "B": "print()",
            "C": "display()",
            "D": "output()"
        },
        "answer": "B"
    },
    {
        "question": "Which loop is used to iterate over a sequence?",
        "options": {
            "A": "for",
            "B": "switch",
            "C": "case",
            "D": "define"
        },
        "answer": "A"
    }
]


def display_instructions():
    print("\n===== QUIZ INSTRUCTIONS =====")
    print("1. The quiz contains 5 questions.")
    print("2. Each question has four options: A, B, C, D.")
    print("3. Enter A, B, C, or D to answer.")
    print("4. Each correct answer earns 1 point.")
    print("5. Incorrect answers earn 0 points.")
    print("6. Invalid choices will not be accepted.")
    print("7. Your final score and percentage will be displayed.")


def display_results(correct, incorrect):
    total = len(questions)
    percentage = (correct / total) * 100

    print("\n===== QUIZ RESULTS =====")
    print("Total Questions:", total)
    print("Correct Answers:", correct)
    print("Incorrect Answers:", incorrect)
    print("Final Score:", str(round(percentage, 2)) + "%")

    if percentage == 100:
        print("Performance: Excellent! Perfect score!")
    elif percentage >= 80:
        print("Performance: Good job!")
    elif percentage >= 60:
        print("Performance: Well done! Keep practising.")
    elif percentage >= 40:
        print("Performance: Keep trying. You can improve!")
    else:
        print("Performance: Don't give up! Practise more.")


def start_quiz():
    # Reset scores for every new attempt
    correct = 0
    incorrect = 0

    print("\n===== WELCOME TO THE QUIZ =====")
    print("Are you ready to test your Python knowledge?")

    while True:
        ready = input("Start the quiz? (yes/no): ").strip().lower()

        if ready == "yes" or ready == "y":
            break
        elif ready == "no" or ready == "n":
            print("Quiz cancelled. Returning to the main menu.")
            return
        else:
            print("Invalid choice! Please enter yes or no.")

    # Display questions one at a time
    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")

        for option, text in q["options"].items():
            print(f"{option}. {text}")

        # Validate the user's answer
        while True:
            try:
                answer = input("Enter your answer (A-D): ").strip().upper()

                if answer in ["A", "B", "C", "D"]:
                    break
                else:
                    print("Invalid choice! Please enter A, B, C, or D.")

            except (EOFError, KeyboardInterrupt):
                print("\nInput interrupted. Returning to the main menu.")
                return

        # Check the answer
        if answer == q["answer"]:
            print("Correct answer!")
            correct += 1
        elif answer != q["answer"]:
            print("Incorrect answer!")
            print("Correct answer:", q["answer"])
            incorrect += 1
        else:
            print("Invalid answer.")

    # Display the final results
    display_results(correct, incorrect)


def main():
    print("===== QUIZ APPLICATION =====")

    while True:
        print("\n1. Start Quiz")
        print("2. View Quiz Instructions")
        print("3. Exit")

        try:
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                start_quiz()

            elif choice == "2":
                display_instructions()

            elif choice == "3":
                print("\nThank you for using the Quiz Application!")
                print("Goodbye!")
                break

            else:
                print("Invalid menu choice! Please enter 1, 2, or 3.")

        except (EOFError, KeyboardInterrupt):
            print("\nApplication closed gracefully. Goodbye!")
            break


if __name__ == "__main__":
    main()
