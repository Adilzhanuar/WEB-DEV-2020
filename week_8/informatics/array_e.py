<<<<<<< HEAD
n = int(input())
nums = [int(i) for i in input().split()]
couple = False
for i in range(n-1):
    if (nums[i]>0 and nums[i+1]>0) or (nums[i]<0 and nums[i+1]<0):
        couple = True
if couple:
    print("YES")
else:
=======
n = int(input())
nums = [int(i) for i in input().split()]
couple = False
for i in range(n-1):
    if (nums[i]>0 and nums[i+1]>0) or (nums[i]<0 and nums[i+1]<0):
        couple = True
if couple:
    print("YES")
else:
>>>>>>> 02dce2f7d1883584c5b5f3cac5f0e37321f79bfe
    print("NO")