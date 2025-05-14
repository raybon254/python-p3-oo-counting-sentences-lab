#!/usr/bin/env python3

class MyString:
  def __init__(self,value = ''):
     self._value = ''
     self.value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, new_value):
      if isinstance(new_value, str):
          self._value = new_value
      else:
          print("The value must be a string.")
          
  def is_sentence(self):
    return self.value.endswith('.')
    pass
  def is_question(self):
    return self.value.endswith('?')
    pass
  def is_exclamation(self):
    return self.value.endswith('!')
    pass
  def count_sentences(self):
    sentences = [s for s in self.value.replace("!", ".").replace("?", ".").split(".") if s.strip()]
    return len(sentences)
  pass
