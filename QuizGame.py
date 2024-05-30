# Task 1 Question and Answer

questions = ["What is the capital of United States?",
            "What year did the movie Titanic came our?",
            "What year did the Freddit Mercury from Queens last perform?",
            "Who was the first president of the United States?",
            "What year was the United States of America discovered?"]
answers = ["Washington, D.C",
          "1997",
          "1986",
          "George Washington",
          "1492"]
# Task 2 Write a function that quizzes the user and takes their answers

def quiz(questions, answers):
    score = 0
    for question, correct_answer in zip(questions, answers):
        user_answer = input(question + " ")
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", correct_answer)
    return score

# Task 3 Score the quiz and give the user feedback on their performance
def score_quiz(score, total_questions):
    percentage = (score / total_questions) * 100
    print("You scored", score, "out of", total_questions, "questions.")
    print("Your score:", percentage, "%")
    if percentage >= 70:
        print("Congratulations! You passed the quiz.")
    else:
        print("Sorry, you did not pass the quiz. Better luck next time.")
def main():
    total_questions = len(questions)
    user_score = quiz(questions, answers)
    score_quiz(user_score, total_questions)

if __name__ == "__main__":
    main()
