
class QuizBrain:
    """manage the quiz game loop, scoring and user input."""
    def __init__(self,question_bank):
        self.question_list = question_bank
        self.question_number =  0
        self.score = 0
        self.game_continues = True


    def another_question(self):
        """check the conditions for the asking another question."""
        current_question = self.question_number
        all_questions = len(self.question_list)
        if current_question < all_questions and self.game_continues == True:
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        """check and compare the user answer to correct answer and update the score."""
        if user_answer.lower() == correct_answer.lower():
            print("That's right answer!")
            self.score += 1
        else:
            print(f"Ohh, no. Your answer is wrong. Right answer was: {correct_answer}")


    def next_question(self):

        current_question = self.question_list[self.question_number]
        self.question_number += 1
        q = input(f"{self.question_number}. {current_question.question}/ [True/False or 'quit' to exit]").lower()
        if q == "quit":
            self.game_continues = False
            return
        while q not in ["true", "false", "quit"]:
            print("Invalid input. Please type True/False or 'quit' to exit.")
            q = input(f"{self.question_number}. {current_question.question}/ [True/False or 'quit' to exit]").lower()
        self.check_answer(q, current_question.answer)
        print(f"your current score is: {self.score}/{self.question_number}\n")
