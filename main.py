import html
from question_model import Question
from data import QuestionProvider
from quiz_brain import QuizBrain
from prettytable import PrettyTable

print("---------Welcome to the Quiz Game.---------")

new_data = QuestionProvider()
api_response = new_data.get_data()

live_question_data = api_response["results"]

question_bank = []
table = PrettyTable()

for item in live_question_data:
    question = item["question"]
    clean_question = html.unescape(question)
    answer = item["correct_answer"]

    new_question = Question(clean_question,answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.another_question():
    quiz.next_question()

print("Thanks for playing Quiz Game.")
table.field_names = ["Final Score", "Total Question Played", "Accuracy Grade"]

"""if player quit the game on current question, current question number 
will be decreased from total number of questions has answered."""
if quiz.question_number > 1:
    questions_answered = quiz.question_number -1
else:
    questions_answered = quiz.question_number
accuracy = (quiz.score/quiz.question_number)*100

table.add_row([quiz.score,questions_answered, f"{accuracy:.1f}%"])
print(table)