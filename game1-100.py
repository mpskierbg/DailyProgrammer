from random import *

def main():
    print("Welcome to the guessing game. I will try to guess your number. All you need to do is answer Higher or Lower, depending on my guess.")
    rand = randint(1, 100)
    guess = False
    high = 100
    low = 1
    trys = 0
    while (guess == False):
        print("All right lets begin. My first guess is " + str(rand) + ".")
        hum_resp = input("Is my guess higher or lower than your number? Please use 'Higher', 'Lower', or 'Correct', thank you. Your selection:").lower()
        while (hum_resp != 'lower' and hum_resp != 'higher' and hum_resp != 'correct'):
            hum_resp = input("Invalid selection, please choose 'Higher', 'Lower', or 'Correct.' Please choose again. Your selection: ").lower()
        if (hum_resp == 'lower'):
            high = rand -1
            rand = randint(low, high)
            guess = False
            trys += 1
        elif (hum_resp == 'higher'):
            low = rand + 1
            rand = randint(low, high)
            guess = False
            trys += 1
        else:
            guess = True
            trys += 1

    print("Fantastic, I guessed it in " + str(trys) + " guess!")

if __name__ == "__main__":
    main()
