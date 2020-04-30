<<<<<<< HEAD
import math
x = int(input())
cnt = 0
for i in range(1,int(math.sqrt(x))):
    if x%i==0:
        cnt+=1
cnt*=2
if(x%math.sqrt(x)==0):
    cnt+=1
=======
import math
x = int(input())
cnt = 0
for i in range(1,int(math.sqrt(x))):
    if x%i==0:
        cnt+=1
cnt*=2
if(x%math.sqrt(x)==0):
    cnt+=1
>>>>>>> 02dce2f7d1883584c5b5f3cac5f0e37321f79bfe
print(cnt)