import random
import string

code_len = 2000
guesses = 0

code = raw_input('Enter your secret code:')
code_len = len(code)

guess = ''
for _ in range(code_len):
    guess += str(random.choice(string.letters + string.digits))

def num_correct():
    correct = 0
    for i in range(code_len):
        if code[i] == guess[i]:
            correct += 1
    return correct

for idx, char in enumerate(guess):
    init_correct = num_correct()
    guess_list = filter(lambda a: a!=guess[idx], [c for c in string.letters + string.digits])
    for i in range(len(string.letters + string.digits)):
        guesses += 1
        guess = guess[:idx] + random.choice(guess_list) + guess[idx+1:]
        guess_list.remove(guess[idx])
        if num_correct() < init_correct:
            guess = guess[:idx] + char + guess[idx+1:]
            break
        elif num_correct() > init_correct:
            break

print('Your code:', code)
print("Computer's guess:", guess)
print('Number of guesses:', guesses)