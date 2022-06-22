import time as t
import random

def typing_test():
    will = 1
    while will == 1:
        '''Prints the sentence(pre-defined by the user in the program), then starts the timer as soon as enter is pressed.
        The timer stops as soon as the enter is pressed after typing.
        At last it displays the typing speed(WPM), typing accuracy(%) and standard net typing speed(WPM)'''

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

        print(f"{sentences[dict_key]}\n")
        input("Please press Enter to start the timer and start typing.\n")

        start_time = t.time()
        words = input()
        end_time = t.time()

        time_lapsed = end_time - start_time
        minutes = time_lapsed / 60

        characters = len(words)
        wpm = (characters / 5) // minutes # each word would be 5 keystrokes

        words_lst = words.split()
        sen_lst = sentences[dict_key].split()
        words_count = len(words_lst)

        correct_words =  0
        try:
            for word in words_lst:
                if word in sen_lst:
                    correct_words+=1

        except Exception as e:
            print("The program failed to process ahead properly because of this error -->", e)
        
        accuracy = (correct_words / words_count) * 100

        net_wpm = (wpm * accuracy) / 100

        print(f"\nYour Typing speed is {wpm} WPM")
        print("Your Accuracy is %.2f" % accuracy, "%")
        print("Your Standard Net Typing speed is %.2f" % net_wpm, "WPM")
        # print(f"\n|\tTime taken in seconds: {time_lapsed}\n|\tCharacters in the sentence: {len(words)}") # extra information to confirm the typing speed
        # print(f"|\n|\tTotal words typed {words_count}\n|\tTotal words in the sentence {len(sen_lst)}\n|\tCorrect Words {correct_words}") # extra information to confirm the typing accuracy
        
        try:
            will = int(input('\nDo you want to continue using the program?\nEnter 0 to exit\nEnter 1 to continue\n\n'))
        except Exception as e:
            print("\nOops! Looks like you have entered a wrong input! Have a look -->", e)
            break

typing_test()