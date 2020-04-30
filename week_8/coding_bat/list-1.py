<<<<<<< HEAD
#first_last6
def first_last6(nums):
  if nums[0]==6 or nums[len(nums)-1]==6:
      return True
  else:
    return False

#same_first_last
def same_first_last(nums):
  if len(nums)==1:
    return True
  else:
    if len(nums)>1 and nums[0]==nums[len(nums)-1]:
      return True
    return False

#make_pi
def make_pi():
  pi = [3,1,4]
  return pi

#common_end
def common_end(a, b):
  if a[len(a)-1]==b[len(b)-1] or a[0]==b[0]:
    return True
  return False

#sum3
def sum3(nums):
  return nums[0]+nums[1]+nums[2]

#rotate_left3
def rotate_left3(nums):
  nums = [nums[1], nums[2], nums[0]]
  return nums

#reverse3
def reverse3(nums):
  nums = nums[::-1]
  return nums

#max_end3
def max_end3(nums):
  maximum = max(nums[0],nums[2])
  new_array = [maximum,maximum,maximum]
  return new_array

#sum2
def sum2(nums):
  sum=0
  if len(nums)==1:
    return nums[0]
  elif len(nums)==0:
    return 0
  else:
    for i in range(2):
      sum+=nums[i]
  return sum

#middle_way
def middle_way(a, b):
  new_array = [a[1],b[1]]
  return new_array

#make_ends
def make_ends(nums):
  new_arr = [nums[0],nums[len(nums)-1]]
  return new_arr

#has23
def has23(nums):
  if nums[0]==2 or nums[1]==2 or nums[0]==3 or nums[1]==3:
    return True
=======
#first_last6
def first_last6(nums):
  if nums[0]==6 or nums[len(nums)-1]==6:
      return True
  else:
    return False

#same_first_last
def same_first_last(nums):
  if len(nums)==1:
    return True
  else:
    if len(nums)>1 and nums[0]==nums[len(nums)-1]:
      return True
    return False

#make_pi
def make_pi():
  pi = [3,1,4]
  return pi

#common_end
def common_end(a, b):
  if a[len(a)-1]==b[len(b)-1] or a[0]==b[0]:
    return True
  return False

#sum3
def sum3(nums):
  return nums[0]+nums[1]+nums[2]

#rotate_left3
def rotate_left3(nums):
  nums = [nums[1], nums[2], nums[0]]
  return nums

#reverse3
def reverse3(nums):
  nums = nums[::-1]
  return nums

#max_end3
def max_end3(nums):
  maximum = max(nums[0],nums[2])
  new_array = [maximum,maximum,maximum]
  return new_array

#sum2
def sum2(nums):
  sum=0
  if len(nums)==1:
    return nums[0]
  elif len(nums)==0:
    return 0
  else:
    for i in range(2):
      sum+=nums[i]
  return sum

#middle_way
def middle_way(a, b):
  new_array = [a[1],b[1]]
  return new_array

#make_ends
def make_ends(nums):
  new_arr = [nums[0],nums[len(nums)-1]]
  return new_arr

#has23
def has23(nums):
  if nums[0]==2 or nums[1]==2 or nums[0]==3 or nums[1]==3:
    return True
>>>>>>> 02dce2f7d1883584c5b5f3cac5f0e37321f79bfe
  return False