<<<<<<< HEAD
n = int(input())
nums = [int(i) for i in input().split()]
cnt=0
for i in range(1,n-1):
    if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
        cnt+=1
=======
n = int(input())
nums = [int(i) for i in input().split()]
cnt=0
for i in range(1,n-1):
    if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
        cnt+=1
>>>>>>> 02dce2f7d1883584c5b5f3cac5f0e37321f79bfe
print(cnt)