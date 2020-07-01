# guessthenumber.py
# A simple game that gives you 5 guesses to find a random number between 1 and 20
 
import random

print("Hi there! What's your name?")
name = input()
print ("Nice to meet you, " + name + ".")

play = True
while play:
    guesses_taken = 0
    number = random.randint(1, 20)
    print ("I am thinking of a number between 1 and 20.")
        
    while guesses_taken < 5:
        print ("Enter your guess:")
        guess = int(input())

        guesses_taken = guesses_taken + 1
        if guess < 1:
            print("The number is between 1 and 20. Please try a little higher!")
        elif guess < number:
            low = ["Too low!", "That's too low.", "Try going higher!", "Too low! Try again"]
            print(random.choice(low))
        elif guess > 20:
            print("The number is between 1 and 20. Please try a little lower!")
        elif guess > number:
            high = ["Too high!", "That's too high.", "Try going lower!", "Too high! Try again"]
            print(random.choice(high))
        elif guess == number:
            break

    if (guess == number and guesses_taken < 2):
            guesses_taken = str(guesses_taken)
            print("Wow, " + name + ", you must have read my mind! You guessed the number in " + guesses_taken + " guess!")

    elif (guess == number and guesses_taken > 1):
            guesses_taken = str(guesses_taken)
            print(name + ", you're a star! You guessed the number in " + guesses_taken + " guesses!")

    if guess != number:
            number = str(number)
            guesses_taken = str(guesses_taken)
            print("Sorry, " + name + ", you've used all " + guesses_taken + " guesses. The number was " + number + "!")    

    again=str(input("Do you want to play again? "))
    if again == "no":
        play = False
