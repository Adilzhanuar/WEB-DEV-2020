<<<<<<< HEAD
def xor(x,y):
    if((x==0 and y==0) or (x==1 and y==1)):
        return 0
    else:
        return 1

x, y = input().split()
x,y= int(x),int(y)
=======
def xor(x,y):
    if((x==0 and y==0) or (x==1 and y==1)):
        return 0
    else:
        return 1

x, y = input().split()
x,y= int(x),int(y)
>>>>>>> 02dce2f7d1883584c5b5f3cac5f0e37321f79bfe
print(xor(x,y))