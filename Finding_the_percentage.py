n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
length = len(student_marks[query_name])

sum, i = 0,0
while i < length :
    sum = sum + student_marks[query_name][i]
    i = i + 1

avg = (sum/length)
average = "{:.2f}".format(avg)
print(average)