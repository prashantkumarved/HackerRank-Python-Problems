def swap_case(s):
    S = ''
    for word in s:
        if word == word.upper():
            string = word.lower()
        else:
            string = word.upper()
        S = S + string
    return S
s = input()
result = swap_case(s)
print(result)

# or you can simply use the below code to solve

def swap_case(s):
    return s.swapcase()
s = input()
result = swap_case(s)
print(result)