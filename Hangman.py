#hangman
import re


'''
1. Get a random word from a CSV file?
2. Show user how many letters are in the word 
Loop:
3. Prompt user guess
4. Evaluate
5. If wrong: add strike and draw new part of the hangman
6. If right: fill in letter in correct blank

When user reaches 7 strikes, they lose the game and are prompted to replay or quit.
When user fills in word, they win and are prompted to replay or quit.
'''

#https://stackoverflow.com/questions/18057962/regex-pattern-including-all-special-characters
def isSpecialCharacter(string):
    regex=re.compile("[^A-Za-z]")
    if(re.search(regex, string)):
        return True
    else:
       return False

#first attempt at Hangman ASCII art :)
game_string='''  -----\n  |    |\n  |\n__|__'''
want_to_play = True

while want_to_play == True:
    
    #currently the right answer is hardcoded
    game_answer="popcorn"
    user_guess= ""
    used_letters = []
    strikes = 0
    secret_word="_ "*len(game_answer)
    isYorN = False

    print("Your secret word has " + str(len(game_answer)) + " letters.")
    print(secret_word + "/n")
        
    while secret_word.replace(" ", "") != game_answer and strikes < 7:

        #prompt the user for input and make sure it is a single letter (no digits or special characters).
        user_guess_letter = input("Guess a letter!")
        if user_guess_letter.isdigit() or isSpecialCharacter(user_guess_letter):
            print("Please only guess letters.")
            continue
        elif len(user_guess_letter) > 1:
            print("Please only guess one letter at a time.")
            continue
        elif user_guess_letter in used_letters:
            print("You've already guessed that!")
            continue
        else:
            #keep track of guessed letters
            used_letters.append(user_guess_letter)

            #only start the FOR loop if the letter appears at all in the answer
            if game_answer.find(user_guess_letter) != -1:                 
                
                position = 0
                # Check each letter in the answer to see if it contains the user input letter. If it does, replace.
                for character in game_answer:
                    #for debugging
                    print("current character: " + character)
                    
                    if character == user_guess_letter:
                           secret_word = secret_word[:position] + user_guess_letter + secret_word[(position+1):]
                           #for debugging
                           print("current secret word is: " + secret_word)

                    #incrementing by 2 here because the underscores need to be separated by spaces to be readable, which adds one more position in the string
                    position += 2
                    
            else:
                strikes = strikes + 1
                print("That's not in the secret word.")
                print(secret_word)
                print("You have " + str(strikes)+ " strikes: " + strikes*"X ")
                
    #strip whitespace from the entire string to check the win condition
    if secret_word.replace(" ", "") == game_answer:
        print("You win! The secret word was " + game_answer + ".")
            
    else:
        print("You lose! The secret word was " + game_answer + ".")

    #while loop to continue prompting user for Y or N input until they enter valid input.
    while isYorN == False:
        
        play_again = input("Type Y to play again or N to quit.")
        #set flags to break out of this while loop and restart the game loop
        if play_again.upper() == "Y":
             want_to_play = True
             isYorN = True
             continue
            
        #set flags to break out of this loop but then DON'T restart the game loop and quit the program
        elif play_again.upper() == "N":
             want_to_play = False
             isYorN = True
             print("Goodbye!")
             quit
             
        #prompt for valid input
        else:
             print("Please enter Y or N.")
             continue
            
