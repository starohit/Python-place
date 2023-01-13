# Develop a quiz game like KBC which will ask user at least 10 questions with 4
# options and show the score after closure of game.

questions = \
    {
        "What is the global warming controversy about?": {
            "A": "the public debate over whether global warming is occuring",
            "B": "how much global warming has occured in modern times",
            "C": "what global warming has caused",
            "D": "all of the above"
        },
        "What movie was used to publicize the controversial issue of global warming?": {
            "A": "the bitter truth",
            "B": "destruction of mankind",
            "C": "the inconvenient truth",
            "D": "the depletion"
        },
        "In what year did former Vice President Al Gore and a U.N. network of scientists share the Nobel Peace Prize?": {
            "A": "1996",
            "B": "1998",
            "C": "2003",
            "D": "2007"
        },
        "Many European countries took action to reduce greenhouse gas before what year?": {
            "A": "1985",
            "B": "1990",
            "C": "1759",
            "D": "2000"
        },
        "Who first proposed the theory that increases in greenhouse gas would lead to an increase in temperature?": {
            "A": "Svante Arrhenius",
            "B": "Niccolo Machiavelli",
            "C": "Jared Bayless",
            "D": "Jacob Thornton"
        }
    }

print("\nGlobal Warming Facts Quiz")
prompt = ">>> "
correct_options = ['D', 'C', 'D', 'B', 'A']
score_count = 0
i = 0
for question, options in questions.items():
    print("\n", question, "\n")
    for option, answer in options.items():
        print(option, ":", answer)
    print("\nWhat's your answer?")
    choice = str(input(prompt))

    if choice.upper() == correct_options[i]:
        score_count += 1
    i = i + 1

print(score_count)
