<<<<<<< HEAD
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(dict.fromkeys(arr))
    arr.sort()
=======
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(dict.fromkeys(arr))
    arr.sort()
>>>>>>> 02dce2f7d1883584c5b5f3cac5f0e37321f79bfe
    print(arr[len(arr)-2])