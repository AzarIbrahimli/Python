#from replit import clear
import random
import hangman_art     #from hangman_art import stages, logo                              
import hangman_words
chosen_word=random.choice(hangman_words.word_list)    #from hangman_words import word_list
print(hangman_art.logo)  #from hangman_art import logo
print(chosen_word)
display=[]
lives=6
list_guess=[]
for letter in chosen_word:    #for _ in range(len(chosen_word)):
    display +="_"             #   display.append("_")
while lives!=0:            #if "_" in not display
    guess=input("Guess a letter : ").lower()
#    clear()
    for position in range(len(chosen_word)):
        if guess==chosen_word[position]:
            list_guess+=guess
            find=list_guess.count(guess)
            if find>1:
                print(f"You have entered \"{guess}\" before") 
            display[position]=chosen_word[position]
    if not guess in chosen_word:
        list_guess+=guess
        find=list_guess.count(guess)
        if find>1:
            print(f"You have entered \"{guess}\" before and it's not in the word. You lose a life")    
        else:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives=lives-1    
    print(*display, sep=" ")
    print(hangman_art.stages[lives])
    if display==list(chosen_word):
        print("You Win!")
        lives=0
if not display==list(chosen_word):
    print("You Lost")















