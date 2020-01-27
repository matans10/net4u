from random import randint

print("Welcom to the Gussing game")
random_number = randint(1,10)
while 1 == 1:
    print("now try to guess the number [1-10]")
    guess = input()
    if (random_number==int(guess)):
        print("congrajolation you guessed right")
        break
    else:
        print("try again")
