n = int(input())
l = []
for i in range(0, n):
    inputs = input().split()
    command = inputs[0]
    if len(inputs) > 1:
        position = int(inputs[1])
    if len(inputs) > 2:
        value = int(inputs[2])
    if command == "insert":
        l.insert(position, value)
    elif command == "remove":
        l.remove(position)
    elif command == "append":
        l.append(position)
    elif command == "sort":
        l.sort()
    elif command == "pop":
        l.pop()
    elif command == "reverse":
        l.reverse()
    else :
        print(l)













