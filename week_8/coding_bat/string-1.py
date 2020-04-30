<<<<<<< HEAD
#hello_name
def hello_name(name):
  return "Hello " + name+"!"

#make_abba
def make_abba(a, b):
  return a + b + b + a

#make_tags
def make_tags(tag, word):
  return "<"+tag+">"+word+"</"+tag+">"

#make_out_word
def make_out_word(out, word):
  return out[:2] + word + out[2:]

#extra_end
def extra_end(str):
  substr = str[len(str)-2:]
  return substr+substr+substr

#first_two
def first_two(str):
  return str[:2]

#first_half
def first_half(str):
  half = len(str)/2
  return str[:half]

#without_end
def without_end(str):
  return str[1:len(str)-1]

#combo_string
def combo_string(a, b):
  if len(a)<len(b):
    return a+b+a
  else:
    return b+a+b

#non-start
def non_start(a, b):
  return a[1:]+b[1:]

#left2
def left2(str):
=======
#hello_name
def hello_name(name):
  return "Hello " + name+"!"

#make_abba
def make_abba(a, b):
  return a + b + b + a

#make_tags
def make_tags(tag, word):
  return "<"+tag+">"+word+"</"+tag+">"

#make_out_word
def make_out_word(out, word):
  return out[:2] + word + out[2:]

#extra_end
def extra_end(str):
  substr = str[len(str)-2:]
  return substr+substr+substr

#first_two
def first_two(str):
  return str[:2]

#first_half
def first_half(str):
  half = len(str)/2
  return str[:half]

#without_end
def without_end(str):
  return str[1:len(str)-1]

#combo_string
def combo_string(a, b):
  if len(a)<len(b):
    return a+b+a
  else:
    return b+a+b

#non-start
def non_start(a, b):
  return a[1:]+b[1:]

#left2
def left2(str):
>>>>>>> 02dce2f7d1883584c5b5f3cac5f0e37321f79bfe
  return str[2:] + str[:2]