<<<<<<< HEAD
#sleep-in
def sleep_in(weekday, vacation):
  if weekday==False and vacation==False:
      return True
  elif weekday==True and vacation==False:
      return False
  elif weekday==False and vacation==True:
      return True
  else:
    return True

#monkey trouble
def monkey_trouble(a_smile, b_smile):
  if (a_smile and b_smile) or (not a_smile and not b_smile):
    return True
  return False

#sum-double
def sum_double(a, b):
  if a==b:
    return 2*(a+b)
  return a+b

#diff21
def diff21(n):
  if n>21:
    return 2*abs(n-21)
  return abs(21-n)

#parrot_trouble
def parrot_trouble(talking, hour):
  if talking and (hour<7 or hour>20):
    return True
  return False

#makes10
def makes10(a, b):
  if a==10 or b==10 or a+b==10:
    return True
  return False

#near_hundred
def near_hundred(n):
  if abs(100-n)<=10 or abs(200-n)<=10:
    return True
  return False

#pos_neg
def pos_neg(a, b, negative):
  if (a<0 and b>0 and not negative) or (a>0 and b<0 and not negative) or (a<0 and b<0 and negative):
    return True
  return False

#not_string
def not_string(str):
  if len(str)>=3 and str[:3]=="not":
    return str
  return "not " + str

#missing_char
def missing_char(str, n):
  begin = str[:n]
  end = str[n+1:]
  return begin + end

#front_back
def front_back(str):
  if len(str)<=1:
    return str
  elif len(str)==2:
    return str[1]+str[0]
  return str[len(str)-1] + str[1:-1] + str[0]

#front3
def front3(str):
=======
#sleep-in
def sleep_in(weekday, vacation):
  if weekday==False and vacation==False:
      return True
  elif weekday==True and vacation==False:
      return False
  elif weekday==False and vacation==True:
      return True
  else:
    return True

#monkey trouble
def monkey_trouble(a_smile, b_smile):
  if (a_smile and b_smile) or (not a_smile and not b_smile):
    return True
  return False

#sum-double
def sum_double(a, b):
  if a==b:
    return 2*(a+b)
  return a+b

#diff21
def diff21(n):
  if n>21:
    return 2*abs(n-21)
  return abs(21-n)

#parrot_trouble
def parrot_trouble(talking, hour):
  if talking and (hour<7 or hour>20):
    return True
  return False

#makes10
def makes10(a, b):
  if a==10 or b==10 or a+b==10:
    return True
  return False

#near_hundred
def near_hundred(n):
  if abs(100-n)<=10 or abs(200-n)<=10:
    return True
  return False

#pos_neg
def pos_neg(a, b, negative):
  if (a<0 and b>0 and not negative) or (a>0 and b<0 and not negative) or (a<0 and b<0 and negative):
    return True
  return False

#not_string
def not_string(str):
  if len(str)>=3 and str[:3]=="not":
    return str
  return "not " + str

#missing_char
def missing_char(str, n):
  begin = str[:n]
  end = str[n+1:]
  return begin + end

#front_back
def front_back(str):
  if len(str)<=1:
    return str
  elif len(str)==2:
    return str[1]+str[0]
  return str[len(str)-1] + str[1:-1] + str[0]

#front3
def front3(str):
>>>>>>> 02dce2f7d1883584c5b5f3cac5f0e37321f79bfe
  return str[0:3] + str[0:3] + str[0:3]