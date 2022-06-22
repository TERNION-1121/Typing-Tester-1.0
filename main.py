import time as t
import random

def typing_test():
    will = 1
    while will == 1:
        '''This function prints the sentence(pre-defined by the user in the program), then starts the timer as soon as enter is pressed.
        The timer stops as soon as the enter is pressed after typing.
        At last it displays the typing speed(WPM) and typing accuracy(%)'''
        dict_key = random.randint(1,10)
        print("\nType the sentence given below:\n")

        sentences = { 1 : 'Hey there this is a program to test your typing speed in words per minute. I hope you would like it.',
                    2 : 'His thought process was on so many levels that he gave himself a phobia of heights.',
                    3 : 'The sunblock was handed to the girl before practice, but the burned skin was proof she did not apply it.',
                    4 : 'Acres of almond trees lined the interstate highway which complimented the crazy driving nuts.',
                    5 : 'You\'re unsure whether or not to trust him, but very thankful that you wore a turtle neck.',
                    6 : 'She always had an interesting perspective on why the world must be flat.',
                    7 : 'If I could, I would make ammends. And today I wrote a list of them.',
                    8 : 'You are not missing them, yet the older version of yourself; the one that was happier then, than now.',
                    9 : 'To the surprise of everyone, the Rapture happened yesterday but it didn\'t quite go as expected.',
                    10: 'She had that tint of craziness in her soul that made her believe she could actually make a difference.' }

        print(f"\"{sentences[dict_key]}\"")
        print()

        input("Please press Enter to start the timer and start typing.\n")
        start_time = t.time()
        words = input()
        end_time = t.time()

        time_lapsed = end_time - start_time
        minutes = time_lapsed / 60

        characters = len(words)
        wpm = (characters / 5) // minutes # each word would be 5 keystrokes

        sen_lst = sentences[dict_key].split(' ')
        words_lst = words.split(' ')
        words_entered = len(words_lst)
        errors = 0

        try:
            for i in range(len(sen_lst)):
                if words_lst[i] != sen_lst[i]:
                    errors+=1

        except Exception as e:
            print("The program failed to process ahead because of this error -->", e)

        correct_words =  words_entered - errors
        accuracy = (correct_words / words_entered) * 100 # typing accuracy here is taken as correct words / total words

        print(f"\t\t\t\tYour Typing speed is {wpm} WPM")
        print("\t\t\t\tYour Accuracy is %.2f" % accuracy, "%")
        # print(f"Time taken in seconds: {time_lapsed}\nCharacters in the sentence: {len(words)}") # extra information to confirm the typing speed
        # print(f"Words in total {words_entered}\nCorrect Words {correct_words}\nErrors {errors}") # extra information to confirm the typing accuracy
        
        try:
            will = int(input('\t\t\t\t\n\nDo you want to continue using the program?\n\t\t\tEnter 0 to exit\n\t\t\tEnter 1 to continue\n\n'))
        except Exception as e:
            print("\nOops! Looks like you have entered a wrong input! Have a look -->", e)
        break

typing_test()