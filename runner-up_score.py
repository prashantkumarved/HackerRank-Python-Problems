n = int(input())
arr = map(int, input().split())
arr = list(arr)
x = max(arr)
while max(arr) == x:
    arr.remove(max(arr))

print(max(arr))