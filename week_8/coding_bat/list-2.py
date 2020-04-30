<<<<<<< HEAD
#count_events
def count_evens(nums):
  cnt=0
  for i in nums:
    if i%2==0:
      cnt+=1
  return cnt

#big_diff
def big_diff(nums):
  minimum = min(nums)
  maximum = max(nums)
  return maximum - minimum

#centered_average
def centered_average(nums):
  maxim = max(nums)
  minim = min(nums)
  nums.remove(maxim)
  nums.remove(minim)
  sum = 0
  for i in nums:
    sum+=i
  return int(sum/len(nums))

#sum13
def sum13(nums):
  sum = 0
  is_13 = False
  for i in nums:
    if is_13:
      is_13 = False
      continue
    if i<13:
      sum+=i
    elif i>=13:
      is_13 = True
  return sum

#sum67
def sum67(nums):
  sum = 0
  is_false = False
  for i in nums:
    if i==6:
      is_false = True
      continue
    elif not is_false:
      sum+=i
    if i==7:
      is_false = False
      continue
    if is_false:
      continue
  return sum

#has22
def has22(nums):
  if len(nums)==2:
    if nums[0]==nums[1]==2:
      return True
    else:
      return False
  for i in range(1,len(nums)-1):
    if nums[i]==2 and (nums[i+1]==2 or nums[i-1]==2):
      return True
=======
#count_events
def count_evens(nums):
  cnt=0
  for i in nums:
    if i%2==0:
      cnt+=1
  return cnt

#big_diff
def big_diff(nums):
  minimum = min(nums)
  maximum = max(nums)
  return maximum - minimum

#centered_average
def centered_average(nums):
  maxim = max(nums)
  minim = min(nums)
  nums.remove(maxim)
  nums.remove(minim)
  sum = 0
  for i in nums:
    sum+=i
  return int(sum/len(nums))

#sum13
def sum13(nums):
  sum = 0
  is_13 = False
  for i in nums:
    if is_13:
      is_13 = False
      continue
    if i<13:
      sum+=i
    elif i>=13:
      is_13 = True
  return sum

#sum67
def sum67(nums):
  sum = 0
  is_false = False
  for i in nums:
    if i==6:
      is_false = True
      continue
    elif not is_false:
      sum+=i
    if i==7:
      is_false = False
      continue
    if is_false:
      continue
  return sum

#has22
def has22(nums):
  if len(nums)==2:
    if nums[0]==nums[1]==2:
      return True
    else:
      return False
  for i in range(1,len(nums)-1):
    if nums[i]==2 and (nums[i+1]==2 or nums[i-1]==2):
      return True
>>>>>>> 02dce2f7d1883584c5b5f3cac5f0e37321f79bfe
  return False