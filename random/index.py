trials = 0
number = 3

overTrials = False


while overTrials == False:
    guess = input("Guess: ")
    trials = trials + 1
    print(trials)

    if number == int(guess):
        print("Got it! Wanna continue or not?")
        choice = input("1 for yes, 0 for no")
        if int(choice) == 1:
            pass
        elif int(choice) == 0:
            exit()
        else:
            print("Input the correct choice:")

    if trials == 3:
        print("Got it")
        overTrials = True