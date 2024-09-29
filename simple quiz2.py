def simple_quiz():
    answer = input("What is the capital of France? ")
    if answer.lower() == "paris":
        print("Correct!")
    else:
        print("Incorrect! The correct answer is Paris.")

simple_quiz()