import random

top_of_range = input('type a number: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('please type a number larger than 0 next time.')
        quit()
else:
    print('please input a number next time')
    quit()
    
random_number = random.randint(0, top_of_range)
print(random_number)
guesses = 0

while True:
    guesses += 1
    user_guess = input('make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('input a number next time')
        continue

    if user_guess == random_number:
        print('you got it')
        break
    else:
        print('you got it wrong')

print('you go it in ', guesses, 'guesses')
