n, m = map(int,input().split())
for i in range(1,n//2 + 1):
    string = (i*2 - 1)*".|."
    print(string.center(m,"-"))
print("WELCOME".center(m,"-"))
for i in reversed(range(1,n//2 + 1)):
    string = (i * 2 - 1) * ".|."
    print(string.center(m,"-"))