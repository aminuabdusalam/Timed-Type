
#my feature changes the difficulty of the game as the level increases

import dictionary
import timer

def get_num_words_by_level(level):
  """Returns the number of words to type for the given level."""
  if level == 1:
    words = 1
  if level == 2:
    words = 1
  if level == 3:
    words = 1
  if level == 4:
    words = 2
  if level == 5:
    words = 3
  if level == 6:
    words = 1
  return words

def get_timeout_by_level(level):
  """Returns the time limit, in seconds, for the given level."""
  if level == 1:
    timeout = 10
  if level == 2:
    timeout = 8
  if level == 3:
    timeout = 6
  if level == 4:
    timeout = 6
  if level == 5:
    timeout = 6
  if level == 6:
    timeout = 3
  return timeout

#changes the difficulty as the level increases 
def difficulty_for_a_given_level(level):
  if level == 1:
    difficulty = 1
  if level == 2:
    difficulty = 1 
  if level == 3:
    difficulty = 2 
  if level == 4:
    difficulty = 2 
  if level == 5:
    difficulty = 2 
  if level == 6:
    difficulty = 2 
  return difficulty

def get_phrase(level):
  """Returns a phrase to type based on the level."""
  # Get the number of words that are supposed to be in
  # the phrase to type, according to the level.
  num_words_in_phrase = get_num_words_by_level(level)
  phrase = ''
  while num_words_in_phrase > 0:
    # Continue adding words to the phrase until it has
    # the appropriate number of words.
    word = dictionary.get_random_word(difficulty_for_a_given_level(level))
    phrase = phrase + ' ' + word
    num_words_in_phrase = num_words_in_phrase - 1
  return phrase.strip() 

level = 0  
round = 0 
phrase = ''
user_input = ''
while phrase == user_input:
  round = round + 1 
  if round <= 5: 
    level = 1
    if round < 1:
      print('LEVEL 1 STARTS NOW!')
    else:
      phrase = get_phrase(level)
      print('Type:',phrase)
      print('You have',get_timeout_by_level(level),'seconds!')
      user_input = timer.input_with_timeout(get_timeout_by_level(level))
      print('----------------------')
  elif round < 10:
    level = 2
    round = round + 1
    phrase = get_phrase(level)
    print('Type:',phrase)
    print('You have',get_timeout_by_level(level),'seconds!')
    user_input = timer.input_with_timeout(get_timeout_by_level(level))
    print('----------------------')  
  elif round < 15:
    level = 3
    round = round + 1
    phrase = get_phrase(level)
    print('Type:',phrase)
    print('You have',get_timeout_by_level(level),'seconds!')
    user_input = timer.input_with_timeout(get_timeout_by_level(level))
    print('----------------------')  
  elif round < 20:
    level = 4
    round = round + 1
    phrase = get_phrase(level)
    print('Type:',phrase)
    print('You have',get_timeout_by_level(level),'seconds!')
    user_input = timer.input_with_timeout(get_timeout_by_level(level))
    print('----------------------')
  elif round < 25:
    level = 5
    round = round + 1
    phrase = get_phrase(level)
    print('Type:',phrase)
    print('You have',get_timeout_by_level(level),'seconds!')
    user_input = timer.input_with_timeout(get_timeout_by_level(level))
    print('----------------------')  
  else:
    level = 6
    round = round + 1
    phrase = get_phrase(level)
    print('Type:',phrase)
    print('You have',get_timeout_by_level(level),'seconds!')
    user_input = timer.input_with_timeout(get_timeout_by_level(level))
    print('----------------------')
print('GAME OVER')
print('You completed',round,'rounds!')
  
    
  