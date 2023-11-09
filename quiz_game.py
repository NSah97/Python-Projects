# Quiz Game

while True:
    print("Welcome to my computer quiz!")

    playing = input("Do you want to play? (yes/no) ")

    if playing != "yes":
        break

    print("Okay! Let's play :)")
    score = 0

    # Frage 1
    answer = input("What does CPU stand for? (Make sure to use only lowercase letters in your answer) ")
    if answer.lower() == "central processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    # Frage 2
    answer = input("What does wwww. stand for? (Make sure to use only lowercase letters in your answer) ")
    if answer.lower() == "world wide web":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    # Frage 3
    answer = input("What does GPU stand for? (Make sure to use only lowercase letters in your answer) ")
    if answer.lower() == "graphics processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    # Frage 4
    answer = input("What does PSU stand for? (Make sure to use only lowercase letters in your answer) ")
    if answer.lower() == "power supply":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    # Frage 5
    answer = input("What does RAM stand for? (Make sure to use only lowercase letters in your answer) ")
    if answer.lower() == "random access memory":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print("You got " + str(score) + " questions correct!")
    print("So you got " + str((score/5) * 100) + "% of the questions correct.")

    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower() != "yes":
        break