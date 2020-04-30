<<<<<<< HEAD
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    sum = 0
    for i in range(3):
        sum+=student_marks[query_name][i]
    average = sum/3
    print("%.2f" % average)
=======
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    sum = 0
    for i in range(3):
        sum+=student_marks[query_name][i]
    average = sum/3
    print("%.2f" % average)
>>>>>>> 02dce2f7d1883584c5b5f3cac5f0e37321f79bfe
        