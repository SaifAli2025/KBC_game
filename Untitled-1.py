print("Wellcome To,   KON BANE GA CRORPATI    ")
print("Rs1000/-")
def ask_questions():
    questions = [
        {  
            "question": "What is the capital of India?",
            "options": ["1. Pune", "2. Solapur", "3. Delhi", "4. Hyderabad"],
            "answer": "3"
        },
        {  
            "question": "Which language is simplest programming laguage ?",
            "options": ["1. c", "2. b", "3. python", "4. java"],
            "answer": "3"
        },
        {  
            "question": "Who is the founder of python?",
            "options": ["1. Guido van Rossum ", "2.habibi", "3. shajaha", "4. khilji"],
            "answer": "1"
        },
        {  
            "question": "Who made Qutb Minar?",
            "options": ["1. SaifAli", "2. shaikh", "3. shajaha", "4. khilji"],
            "answer": "4"
        }, 
    ] 

    prize_money = [1000,10000 ,89000, 100000,700000]
    total_winnings = 0 

    for i, q in enumerate(questions):
        print(f"Question {i+1}: {q['question']}")
        for option in q['options']:
            print(option)

        answer = input("Enter the option number (or press Enter to stop): ")
        if not answer:
            print("No answer provided. Stopping the quiz.")
            break
        if answer == q['answer']:
            print(f"Correct! You have won sathcarod ${prize_money[i]}!\n")
            total_winnings += prize_money[i]
        else:
            print("Incorrect.\n")
            print(f"Total prize money: ${total_winnings}")
            return  # Exit the function to end the quiz

    print(f"KBC completed! Total prize money: ${total_winnings}")

# To start the quiz
ask_questions()
