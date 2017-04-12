#Hangman App
from random import randint

def new_word():
  r = randint(0,8)
  words = ['tulip', 'camel', 'daisy', 'zebra', 'imagine', 'purple', 'mushroom', 'chocolate', 'rabbit']
  return words[r]

def hide_word(answer, letters_found):
  blanked_word = ""
  for letter in answer:
    if letter in letters_found:
      blanked_word += letter 
    else:
      blanked_word += "_"
    blanked_word += " "
  return blanked_word
  
def format_list(my_list):
  string_list = ""
  my_list.sort()
  for letter in my_list:
    string_list += "%s " % letter
  return string_list

def play(answer):
  blanked_word = hide_word(answer, [])
  letters_found = []
  letters_guessed = []
  turns_remaining = 10
  while ( "_" in blanked_word ) and ( turns_remaining > 0 ):
    print blanked_word
    if len(letters_guessed) > 0:
      print "Letters guessed: %s" % format_list(letters_guessed)
    print "You have %d incorrect guesses remaining\n" % turns_remaining
    letter = guess_letter(answer)
    if letter != False:
      if letter in letters_guessed:
        print "\nLetter previously guessed\n"
        turns_remaining -= 1
      else:
        if letter in answer:
          letters_found += letter
          blanked_word = hide_word(answer, letters_found)
          print "\nCorrect!\n"
        else:
          turns_remaining -= 1
          print "\nIncorrect!\n"
        letters_guessed += letter
    else:
      turns_remaining -= 1
  if turns_remaining == 0:
    print "You lose"
  else:
    print "You win, the word was %s." % answer
    
def guess_letter(answer):
  letter = raw_input("Guess a letter: ").lower()
  if letter_validation(letter) != -1:
    return letter
  return False

def letter_validation(letter):
  if letter.isalpha():
    return letter
  else:
    print "\nPlease enter a valid letter\n"
    return -1
  
answer = new_word()
print answer
play(answer)