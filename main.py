import time as t

print("Type the sentence given below:\n")
sentence = '''Hey there this is a program to test your typing speed in words per minute. I hope you would like it.\n'''
print(sentence)

input("Please press enter to start the timer and start typing.\n")
start_time = t.time()
words = input()
end_time = t.time()

time_lapsed = end_time - start_time
minutes = time_lapsed / 60

characters = len(words)

wpm = (characters/5) // minutes
print(f"\n\nYour Typing speed is {wpm} WPM")

# print(f"Time taken in seconds: {time_lapsed}\nCharacters in the sentence: {len(words)}")