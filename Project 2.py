quiz_questions = [
    {"question": "What color is the sky?", "answer": "blue"},
    {"question": "What is a dog?", "answer": "an animal"},
    {"question": "What is 5+5", "answer": "10"}
]

leaderboard = {}

while True:
    print("Welcome to the game!!!!")
    score = 0
    for q in quiz_questions:
        print(q["question"])
        answer = input("What is the correct answer?: ")
        if answer.lower() == q["answer"].lower():
            print("Correct")
            score += 1
        else:
            print("Incorrect")
    name = input("What is your name?: ")
    leaderboard[name] = score

    repeat = input("Does anyone else want to play?: ")
    if repeat.lower() == "no":
        break

for key, value in leaderboard.items():
    print(f"{key}: {value}")
print("Thank you for playing!")