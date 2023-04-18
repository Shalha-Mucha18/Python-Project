#guess the number
import random

n=random.randint(1,5)
guess=int(input("Enter an integer from 1 t0 99: "))


while True:
    print()
    if guess  < n:
        print("guess is low")
        guess=int(input("Enter an integer from 1 t0 99: "))
    elif guess>n:
        print("guess is high")
        guess=int(input("Enter an integer from 1 t0 99: "))
    else:
        print('You guessed it')
        break
    print()
