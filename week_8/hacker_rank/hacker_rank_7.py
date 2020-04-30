<<<<<<< HEAD
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input()) 
    ar = [] 
    p = 0 
    for i in range ( x + 1 ) : 
        for j in range( y + 1): 
            for k in range ( z + 1):
                if i+j+k != n: 
                    ar.append([]) 
                    ar[p] = [ i , j, k ] 
                    p+=1
=======
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input()) 
    ar = [] 
    p = 0 
    for i in range ( x + 1 ) : 
        for j in range( y + 1): 
            for k in range ( z + 1):
                if i+j+k != n: 
                    ar.append([]) 
                    ar[p] = [ i , j, k ] 
                    p+=1
>>>>>>> 02dce2f7d1883584c5b5f3cac5f0e37321f79bfe
    print(ar) 