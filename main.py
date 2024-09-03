import random as r
import hangman_art
import hangman_words
chosen_word = r.choice(hangman_words.word_list)
print(hangman_art.logo)
print(chosen_word) #can remove this
word_len = len(chosen_word)
display = []
end_of_game = False
lives = 6
for i in range(word_len):
  display.append('_')
while not end_of_game:
  guess = input("Guess a letter: ").lower()
  if guess in display:
    print(f"You've already guessed {guess}")
  for position in range(word_len):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = guess
  if guess not in chosen_word:
    print("Letter not in word!, You lose a life")
    lives -= 1
    if lives == 0:
       end_of_game = True
       print("You lose")
       print(f"The word was {chosen_word}")
      #join all the elments in a list and turn it into str
  print(f"{' '.join(display)}")
  if "_" not in display:
      end_of_game = True
      print("You win!")
  from hangman_art import stages
  print(stages[lives])