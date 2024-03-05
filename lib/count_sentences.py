#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self.value = value

  def is_sentence(self):
    if not isinstance(self.value, str):
      return "The value must be a string."
    if self.value and self.value[-1] == '.':
      return True
    else:
      return False
    
  def is_question(self):
    if not isinstance(self.value, str):
      return "The value must be a string."
    if self.value and self.value[-1] == '?':
      return True
    else:
      return False
    
  def is_exclamation(self):
    if not isinstance(self.value, str):
      return "The value must be a string."
    if self.value and self.value[-1] == '!':
      return True
    else:
      return False
    
  def count_sentences(self):
    if not isinstance(self.value, str):
      return "The value must be a string."
    return len(self.value.split('.'))
    