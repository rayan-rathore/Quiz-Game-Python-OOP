import requests


class QuestionProvider:
    """it fetches questions direct form  Open Trivia Database """
    def __init__(self):
        pass

    def get_data(self):
        user_choice = input("On Which topic do you want to play quiz today?: \ntype '1' for General Knowledge"
                            "\ntype '2' for Science: Nature \ntype '3' for Science:Computer "
                            "\ntype '4' for Celebrities \ntype '5' for Mythology"
                            "\ntype '6' for Geography \ntype '7' for History\n")
        if user_choice == "1":
            category_id = 9
            amount = 50
        elif user_choice == "2":
            category_id = 17
            amount = 40
        elif user_choice == "3":
            category_id = 18
            amount = 40
        elif user_choice == "4":
            category_id = 26
            # set amount at 5, as there is lot less questions on Celebrities
            amount = 5
        elif user_choice == "5":
            category_id = 20
            # set amount at 13, as there is lot less questions on Mythology
            amount = 13
        elif user_choice == "6":
            category_id = 22
            amount = 40
        else:
            category_id = 23
            amount = 40

        """create the unique URL link for the api request"""
        URL = f"https://opentdb.com/api.php?amount={amount}&category={category_id}&type=boolean"
        # https://opentdb.com/api.php?amount=50&category=17&difficulty=medium&type=boolean
        # https://opentdb.com/api.php?amount=50&category=9&difficulty=medium&type=boolean

        try:
            response = requests.get(URL)
            response.raise_for_status()
            data = response.json()  # translate internet data into the useful python dictionary
            return data
        except requests.RequestException:
            print("Failed to fetch the quiz data.")
            return {"results": []}