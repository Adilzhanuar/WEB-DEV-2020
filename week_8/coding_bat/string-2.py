<<<<<<< HEAD
#double_char
def double_char(str):
  new_str=""
  for i in str:
    new_str+=i+i
  return new_str

#count_hi
def count_hi(str):
  hi="hi"
  cnt=0
  for i in range(0,len(str)):
    if str[i:i+2]==hi:
      cnt+=1
  return cnt

#cat_dog
def cat_dog(str):
  dog = "dog"
  cat = "cat"
  cnt_dog = 0
  cnt_cat = 0
  for i in range(len(str)):
    if str[i:i+3] == dog:
      cnt_dog+=1
    elif str[i:i+3] == cat:
      cnt_cat+=1
  if cnt_dog==cnt_cat:
    return True
  return False

#count_code
def count_code(str):
  cnt=0
  for i in range(len(str)-3):
    if str[i:i+2] == "co" and str[i+3]=="e":
      cnt+=1
  return cnt

#end_other
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return (b.endswith(a) or a.endswith(b))

#xyz_there
def xyz_there(str):
  with_dot=0
  without_dot=0
  for i in range(len(str)):
    if "xyz"==str[i:i+3]:
      with_dot+=1
    elif ".xyz"==str[i:i+4]:
      without_dot+=1
  if with_dot>without_dot:
    return True
  return False
=======
#double_char
def double_char(str):
  new_str=""
  for i in str:
    new_str+=i+i
  return new_str

#count_hi
def count_hi(str):
  hi="hi"
  cnt=0
  for i in range(0,len(str)):
    if str[i:i+2]==hi:
      cnt+=1
  return cnt

#cat_dog
def cat_dog(str):
  dog = "dog"
  cat = "cat"
  cnt_dog = 0
  cnt_cat = 0
  for i in range(len(str)):
    if str[i:i+3] == dog:
      cnt_dog+=1
    elif str[i:i+3] == cat:
      cnt_cat+=1
  if cnt_dog==cnt_cat:
    return True
  return False

#count_code
def count_code(str):
  cnt=0
  for i in range(len(str)-3):
    if str[i:i+2] == "co" and str[i+3]=="e":
      cnt+=1
  return cnt

#end_other
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return (b.endswith(a) or a.endswith(b))

#xyz_there
def xyz_there(str):
  with_dot=0
  without_dot=0
  for i in range(len(str)):
    if "xyz"==str[i:i+3]:
      with_dot+=1
    elif ".xyz"==str[i:i+4]:
      without_dot+=1
  if with_dot>without_dot:
    return True
  return False
>>>>>>> 02dce2f7d1883584c5b5f3cac5f0e37321f79bfe
      