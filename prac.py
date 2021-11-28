# def print_full_name(first, last):
#     print("Hello " +first +" "+ last + "! You just delved into python.")
#
# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)

# x = 'From marquard@uct.ac.za'
# print(x[9])
# print(x[8])
# print(x[7])
#
#
# print(x[14:17])


# text = "X-DSPAM-Confidence:    0.8475"
# num = text.find('0')
# print(float(text[num: ]))
#
# take = True
# while take is True:
#     input()

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
length = len(student_marks[query_name])
print(length)
sum, i = 0,0
while i < length :
    sum = sum + student_marks[query_name][i]
    i = i + 1

avg = (sum/length)
average = "{:.2f}".format(avg)
print(average)