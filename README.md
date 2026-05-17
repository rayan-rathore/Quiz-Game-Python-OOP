# Quiz-Game-Python-OOP
A command-line True/False quiz game built with Python using Object-Oriented Programming principles and the Open Trivia Database API.
# Quiz Game 🎯

A command-line True/False quiz game built with Python using Object-Oriented Programming principles and the Open Trivia Database API.

## Features

* Multiple quiz categories
* Live trivia questions from API
* True/False gameplay
* Score tracking
* Input validation
* Quit option during gameplay
* Final score summary table
* Clean OOP-based project structure

---

## Technologies Used

* Python
* OOP (Object-Oriented Programming)
* Requests Library
* PrettyTable
* Open Trivia Database API

---

## Project Structure

```text
quiz-game/
│
├── main.py
├── data.py
├── question_model.py
├── quiz_brain.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How It Works

1. User selects a quiz category
2. The program fetches questions from the Open Trivia Database API
3. Questions are converted into Question objects
4. QuizBrain manages:

   * game loop
   * scoring
   * user input
   * answer checking
5. Final score and accuracy are displayed in a table

---

## Categories Available

* General Knowledge
* Science: Nature
* Science: Computers
* Celebrities
* Mythology
* Geography
* History

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/quiz-game.git
```

Move into the project folder:

```bash
cd quiz-game
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

---

## Example Gameplay

```text
---------Welcome to the Quiz Game.---------

1. Python was released in 1991?
True

That's right answer!
your current score is: 1/1
```

---

## Concepts Practiced

* Classes and Objects
* Constructors
* Methods
* Encapsulation
* API handling
* Loops and conditionals
* Input validation
* Working with external libraries
* Modular code organization

---

## Future Improvements

* Difficulty selection
* Multiple-choice questions
* Timed quiz mode
* GUI version with Tkinter
* Leaderboard system
* Question caching

---

## Acknowledgements

* Angela Yu's 100 Days of Code
* Open Trivia Database API

API:
https://opentdb.com/

---

## Author

Built by [Your Name]
