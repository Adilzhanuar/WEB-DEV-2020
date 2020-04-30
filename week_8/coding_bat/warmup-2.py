<<<<<<< HEAD
#string_times
def string_times(str, n):
  new_str = ""
  for _ in range(n):
    new_str += str
  return new_str

#front_times
def front_times(str, n):
  new_str=""
  for _ in range(n):
    new_str+=str[:3]
  return new_str

#string_bits
def string_bits(str):
  new_str=""
  for i in range(0,len(str),2):
    new_str+=str[i]
  return new_str

#string_splosion
def string_splosion(str):
  new_str=""
  for i in range (len(str)):
    for j in range(i+1):
      new_str+=str[j]
  return new_str

#last2
def last2(str):
  if len(str)<2:
    return 0
  substr = str[len(str)-2:]
  cnt=0
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == substr:
      cnt += 1
  return cnt

#array_count9
def array_count9(nums):
  cnt=0
  for i in nums:
    if i==9:
      cnt+=1
  return cnt

#array_front9
def array_front9(nums):
  n = len(nums)
  if n>4:
    n=4
      
  for i in range(n):
    if nums[i]==9:
      return True
  return False

#array123
def array123(nums):
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False

#string_match
def string_match(a, b):
  cnt=0
  length = min(len(a),len(b))
  for i in range(length-1):
    a_substr = a[i:i+2]
    b_substr = b[i:i+2]
    if a_substr == b_substr:
      cnt += 1
  return cnt

=======
#string_times
def string_times(str, n):
  new_str = ""
  for _ in range(n):
    new_str += str
  return new_str

#front_times
def front_times(str, n):
  new_str=""
  for _ in range(n):
    new_str+=str[:3]
  return new_str

#string_bits
def string_bits(str):
  new_str=""
  for i in range(0,len(str),2):
    new_str+=str[i]
  return new_str

#string_splosion
def string_splosion(str):
  new_str=""
  for i in range (len(str)):
    for j in range(i+1):
      new_str+=str[j]
  return new_str

#last2
def last2(str):
  if len(str)<2:
    return 0
  substr = str[len(str)-2:]
  cnt=0
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == substr:
      cnt += 1
  return cnt

#array_count9
def array_count9(nums):
  cnt=0
  for i in nums:
    if i==9:
      cnt+=1
  return cnt

#array_front9
def array_front9(nums):
  n = len(nums)
  if n>4:
    n=4
      
  for i in range(n):
    if nums[i]==9:
      return True
  return False

#array123
def array123(nums):
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False

#string_match
def string_match(a, b):
  cnt=0
  length = min(len(a),len(b))
  for i in range(length-1):
    a_substr = a[i:i+2]
    b_substr = b[i:i+2]
    if a_substr == b_substr:
      cnt += 1
  return cnt

>>>>>>> 02dce2f7d1883584c5b5f3cac5f0e37321f79bfe
