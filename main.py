import time as t

def typing_test():
    '''This function prints the sentence(pre-defined by the user), then starts the timer as soon as enter is pressed.
    The timer stops as soon as the enter is pressed after typing.
    At last it displays the typing speed(WPM) and the accuracy(%)'''
    print("Type the sentence given below:\n")
    sentence = '''Hey there this is a program to test your typing speed in words per minute. I hope you would like it.'''
    print(f"\"{sentence}\"")
    print()

    input("Please press Enter to start the timer and start typing.\n")
    start_time = t.time()
    words = input()
    end_time = t.time()

    time_lapsed = end_time - start_time
    minutes = time_lapsed / 60

    characters = len(words)

    wpm = (characters/5) // minutes
    print(f"\n\n\t\t\t\tYour Typing speed is {wpm} WPM")

    sen_lst = sentence.split(' ')
    words_lst = words.split(' ')
    errors = 0

    for i in range(len(sen_lst)):
        if words_lst[i] != sen_lst[i]:
            errors+=1

    correct_chars = characters - errors
    accuracy = (correct_chars / characters) * 100

    print("\t\t\t\tYour Accuracy is %.2f" % accuracy, "%")
    # print(f"Time taken in seconds: {time_lapsed}\nCharacters in the sentence: {len(words)}")
    # print(f"Characters in total {characters}\nCorrect Characters {correct_chars}\nErrors {errors}")

typing_test()