<<<<<<< HEAD
#make_bricks
def make_bricks(small, big, goal):
  return goal%5 >= 0 and goal%5 - small <= 0 and small + 5*big >= goal

#lone_sum
def lone_sum(a, b, c):
  if a==b==c:
    return 0
  if a==b:
    return c
  if c==b:
    return a
  if a==c:
    return b
  return a+b+c

#lucky_sum
def lucky_sum(a, b, c):
  if a==13:
    a=0
    b=0
    c=0
  if b==13:
    b=0
    c=0
  if c==13:
    c=0
  sum = a+b+c
  return sum

#no_teen_sum
def no_teen_sum(a, b, c):
  a = fix_teen(a)
  b = fix_teen(b)
  c = fix_teen(c)
  sum = a+b+c
  return sum
  
  
def fix_teen(n):
  if n==15 or n==16:
    return n
  elif n>=10:
    return 0
  else:
    return n

#round_sum
def round_sum(a, b, c):
  a = round10(a)
  b = round10(b)
  c = round10(c)
  return a+b+c
  
def round10(num):
  if num%10>=5:
      num+=(10-(num%10))
  else:
    num-=(num%10)
  return num

#close_far
def close_far(a, b, c):
  arr = [a,b,c]
  arr.sort()
  maxi = arr[2]
  mini = arr[0]
  mid = arr[1]
  if (maxi-mid<2 and mid-mini<2):
    return False
  if (maxi-mid<2 and maxi-mini>=2) or (mid-mini<2 and maxi-mini>=2):
    return True
  return False

#make_chocolate
def make_chocolate(small, big, goal):
  maxBig = goal / 5
   
  if big >= maxBig:
    if small >= (goal - maxBig * 5):
      return goal - maxBig * 5
  if big < maxBig:
    if small >= (goal - big * 5):
      return goal - big * 5
  return -1

=======
#make_bricks
def make_bricks(small, big, goal):
  return goal%5 >= 0 and goal%5 - small <= 0 and small + 5*big >= goal

#lone_sum
def lone_sum(a, b, c):
  if a==b==c:
    return 0
  if a==b:
    return c
  if c==b:
    return a
  if a==c:
    return b
  return a+b+c

#lucky_sum
def lucky_sum(a, b, c):
  if a==13:
    a=0
    b=0
    c=0
  if b==13:
    b=0
    c=0
  if c==13:
    c=0
  sum = a+b+c
  return sum

#no_teen_sum
def no_teen_sum(a, b, c):
  a = fix_teen(a)
  b = fix_teen(b)
  c = fix_teen(c)
  sum = a+b+c
  return sum
  
  
def fix_teen(n):
  if n==15 or n==16:
    return n
  elif n>=10:
    return 0
  else:
    return n

#round_sum
def round_sum(a, b, c):
  a = round10(a)
  b = round10(b)
  c = round10(c)
  return a+b+c
  
def round10(num):
  if num%10>=5:
      num+=(10-(num%10))
  else:
    num-=(num%10)
  return num

#close_far
def close_far(a, b, c):
  arr = [a,b,c]
  arr.sort()
  maxi = arr[2]
  mini = arr[0]
  mid = arr[1]
  if (maxi-mid<2 and mid-mini<2):
    return False
  if (maxi-mid<2 and maxi-mini>=2) or (mid-mini<2 and maxi-mini>=2):
    return True
  return False

#make_chocolate
def make_chocolate(small, big, goal):
  maxBig = goal / 5
   
  if big >= maxBig:
    if small >= (goal - maxBig * 5):
      return goal - maxBig * 5
  if big < maxBig:
    if small >= (goal - big * 5):
      return goal - big * 5
  return -1

>>>>>>> 02dce2f7d1883584c5b5f3cac5f0e37321f79bfe
