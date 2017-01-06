import random

code_len = 500
code = ''
for _ in range(code_len):
    code += str(random.randint(0,9))

guess = ''
for _ in range(code_len):
    guess += str(random.randint(0,9))

def num_correct():
    correct = 0
    for i in range(code_len):
        if code[i] == guess[i]:
            correct += 1
    return correct

for idx, char in enumerate(guess):
    init_correct = num_correct()
    guess_list = filter(lambda a: a!=guess[idx], [c for c in range(10)])
    for i in range(10):
        guess = guess[:idx] + str(random.choice(guess_list)) + guess[idx+1:]
        guess_list.remove(int(guess[idx]))
        if num_correct() < init_correct:
            guess = guess[:idx] + char + guess[idx+1:]
            break
        elif num_correct() > init_correct:
            break
            

if guess == code:
    print('You won!')
else:
    print('You lost!')

print('Actual code:', code)
print('Your guess:', guess)