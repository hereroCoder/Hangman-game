
import random


def skeleton(count,word):
    if count ==1:
        print(" O")
    elif count ==2:
        print(" O")
        print('/')
    elif count ==3:
        print(" O")
        print('/' + '|')
    elif count ==4:
        print(" O")
        print('/' + '|' + '\\')
    elif count ==5:
        print(" O")
        print('/' + '|' + '\\')
        print('/')
    elif count == 6:
        print(" O")
        print('/' + '|' + '\\')
        print('/ ' + '\\')
    elif count == 7:
        print(" O")
        print('---')
        print('/' + '|' + '\\')
        print('/ ' + '\\')
        print(f'You lost! the word was {word}')



def find_index(word,char):
    #convert word to a list, loop through the list to get positions of the character
    # use count to determine how many rounds to loop
    x = list(word)
    positions = []
    for i in range(x.count(char)):
        position = x.index(char)
        positions.append(position)
        #after getting the postion replace the char with _ so index method can find the next char
        x[position] = '_' 
    return positions


def playing ():
    words = ["photosynthesis", "carbon", "america", "care", "love", "respect","biology"]
    the_word = random.choice(words)
    guessed_word = list(len(the_word)*'_')

    possible_choices = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    already_Guessed = []

    print(guessed_word)
    game_count = 1 
    while game_count < 8:
         
        character = input("Guess a character: ").lower()

        if character in already_Guessed:
            print('You already guessed that character')

        elif character in possible_choices:
            if character in the_word:
                #getting index of character and inserting it in the guessed word blanks
                positions = find_index(the_word,character)
                for the_index in positions:
                    guessed_word[the_index] = character
                print(guessed_word)

                if ''.join(guessed_word) == the_word:
                    #when user wins
                    print(f"Yay you won. {the_word} was indeed the word")
                    break

            else:
                 # draw skeleton when user guess a wrong character
                skeleton(game_count,the_word)
                game_count += 1
               
            already_Guessed.append(character)
            print()
        else:
            print("That is an invalid input, selelect a letter from the alphabets")
        print(f'Already guessed: {already_Guessed}')

playing()

