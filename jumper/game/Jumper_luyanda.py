import random
import time
from puzzle import puzzle

# Initial Steps to invite in the game:
print("\nWelcome to the jumper game! \n")
first_half_name = input("Enter a three letter word: ")
second_half_name = input("Enter a four letter word: ")

print()

print(f"Hello {second_half_name.capitalize() + first_half_name}! Best of luck!")
time.sleep(2)
print("The game is about to start!\nLet's play in...")
time.sleep(2)
print("3")
time.sleep(1)
print("3, 2")
time.sleep(1)
print("3, 2, 1")
time.sleep(1)
print("Let's Go!")
time.sleep(1)

 
#Class which generates random words from the module puzzle.
class words():
    def __init__(self, word):
        self.word = word

    def show(self):
        print(self.word)


#random_word = words(puzzle[random.randint(0,19)])

random_word = words(random.choice(puzzle))

#random_word.show()


#This is a class that creates the jumper guy with his parachute.
print()

class man():

    def __init__(self, guy):
        self._guy = guy


    def jumper_guy():

        guy = [
                   [" _"," ","_"," ", "_"],
                   ["/"," " ," " ," ", " ", " ","\\"],
                   [" _"," ", "_"," ","_"],
                   ["\\"," "," "," "," "," ","/"],
                   [" \\"," "," "," ","/"],
                   [" "," ", " ","O"],
                   [" "," ","/", " ","\\"],
                   [" ", " "," ", "|"], 
                   [" ","/", " ", " ", " ", "\\"]]

        for each_list in guy:
            print ("".join(each_list))


def main():
    global count
    global display
    global random_word
    global already_guessed
    global length
    global play_game
    length = random_word
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""
    
    

def loop():#loop for re-excecuting the game once the round ends.
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! Come back for more fun guessing experience!")
        exit()

def jumper():#The function which the entire game is run. 
    
    global count
    global display
    global random_word
    global already_guessed
    global play_game
    limit = 10
    guess = input("This is the Word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        jumper()

    elif guess in puzzle:
        already_guessed.extend([guess])
        index = random_word.find(guess)
        random_word = random_word[:index] + "_" + random_word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            man.jumper_guy()
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            guy = (
                   ["/"," " ," " ," ", " ", " ","\\"],
                   [" _"," ", "_"," ","_"],
                   ["\\"," "," "," "," "," ","/"],
                   [" \\"," "," "," ","/"],
                   [" "," ", " ","O"],
                   [" "," ","/", " ","\\"],
                   [" ", " "," ", "|"], 
                   [" ","/", " ", " ", " ", "\\"])

            for each_list in guy:
                print ("".join(each_list))

            # print(guy)

            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
            time.sleep(1)
            guy = (
                   ["/"," " ," " ," ", " ", " ",],
                   [" _"," ", "_"," ","_"],
                   ["\\"," "," "," "," "," ","/"],
                   [" \\"," "," "," ","/"],
                   [" "," ", " ","O"],
                   [" "," ","/", " ","\\"],
                   [" ", " "," ", "|"], 
                   [" ","/", " ", " ", " ", "\\"])

            for each_list in guy:
                print ("".join(each_list))

            # print(guy)

            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(2)
            guy = (
                   [" _"," ", "_"," ","_"],
                   ["\\"," "," "," "," "," ","/"],
                   [" \\"," "," "," ","/"],
                   [" "," ", " ","O"],
                   [" "," ","/", " ","\\"],
                   [" ", " "," ", "|"], 
                   [" ","/", " ", " ", " ", "\\"])

            for each_list in guy:
                print("".join(each_list))

            # print(guy)

            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            guy = (
                   ["\\"," "," "," "," "," ","/"],
                   [" \\"," "," "," ","/"],
                   [" "," ", " ","O"],
                   [" "," ","/", " ","\\"],
                   [" ", " "," ", "|"], 
                   [" ","/", " ", " ", " ", "\\"])

            for each_list in guy:
                print("".join(each_list))

            # print(guy)

            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 6:
            time.sleep(1)
            guy = (
                   ["\\"," "," "," "," "," ",],
                   [" \\"," "," "," ","/"],
                   [" "," ", " ","O"],
                   [" "," ","/", " ","\\"],
                   [" ", " "," ", "|"], 
                   [" ","/", " ", " ", " ", "\\"])

            for each_list in guy:
                print("".join(each_list))

            # print(guy)

            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 7:
            time.sleep(1)
            guy = (
                   ["\\"," "," "," ","/"],
                   [" "," ", " ","O"],
                   [" "," ","/", " ","\\"],
                   [" ", " "," ", "|"], 
                   [" ","/", " ", " ", " ", "\\"])

            for each_list in guy:
                print("".join(each_list))

            # print(guy)

            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 8:
            time.sleep(1)
            guy = (
                   ["\\"," "," "," "," "],
                   [" "," ", " ","O"],
                   [" "," ","/", " ","\\"],
                   [" ", " "," ", "|"], 
                   [" ","/", " ", " ", " ", "\\"])

            for each_list in guy:
                print("".join(each_list))

            # print(guy)

            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")


        elif count == 9:
            time.sleep(1)
            guy = (
                   [" "," ", " ","O"],
                   [" "," ","/", " ","\\"],
                   [" ", " "," ", "|"], 
                   [" ","/", " ", " ", " ", "\\"])

            for each_list in guy:
                print("".join(each_list))

            # print(guy)

            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 10:
            time.sleep(1)
            guy = (
                   [" "," ", " ","X"],
                   [" "," ","/", " ","\\"],
                   [" ", " "," ", "|"], 
                   [" ","/", " ", " ", " ", "\\"])

            for each_list in guy:
                print("".join(each_list))



            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

            print("Wrong guess. You are dead!!!\n")
            print("The word was:",already_guessed,random_word)
            loop()
    if random_word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        loop()

    elif count != limit:
        jumper()

main()

jumper()