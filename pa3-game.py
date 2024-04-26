import random

secret_number = random.randint(1,100)

print("I'm thinking of a number between 1-100. Can you guess it in 3 tries?")

num_guesses = 3
while True:
    user_guess = input("Enter guess: ")
    num_guesses -= 1

    if user_guess == secret_number:
            print("Correct! You Win! :)")
            break

    if num_guesses == 0:
            print("Out of tries. You Lost! :(")
            break

    print("Wrong! Number of tries left: " + str(num_guesses))

print("Secret number = " + str(secret_number))

